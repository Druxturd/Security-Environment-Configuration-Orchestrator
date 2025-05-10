import asyncio
from collections import defaultdict
import shutil
from tempfile import NamedTemporaryFile, mkdtemp

import ansible_runner
from models.target import Target
import os

AUTO_HARDEN_PLAYBOOK_OS_VERSION = {
    "debian-11": "hardening_debian11.yml",
    "debian-12": "hardening_debian12.yml",
    "ubuntu-20": "hardening_ubuntu20.yml",
    "ubuntu-22": "hardening_ubuntu22.yml",
    "ubuntu-24": "hardening_ubuntu24.yml"
}

PLAYBOOK_START = "playbook_on_play_start"
RECAP_EVENT = "playbook_on_stats"
RUNNER_OK = "runner_on_ok"
RUNNER_FAILED = "runner_on_failed"
RUNNER_UNREACHABLE  = "runner_on_unreachable"
RUNNER_SKIPPED = "runner_on_skipped"
RUNNER_EVENTS = [
    RUNNER_OK,
    RUNNER_FAILED,
    RUNNER_UNREACHABLE,
    RUNNER_SKIPPED,
]


HARDEN_FILES = "harden_files"

async def execute_auto_harden_on_single_target(os_version_name: str, target: Target):
    runner_dir = mkdtemp(prefix="runner_")
    project_dir = os.path.join(runner_dir, "project")
    os.makedirs(project_dir, exist_ok=True)

    key_file = NamedTemporaryFile(delete=False, mode='w', dir=runner_dir)
    key_file.write(target.SSHKey.strip() + "\n")
    key_file.close()
    os.chmod(key_file.name, 0o600)
    key_path = key_file.name

    inventory_lines = ["[target]"]
    inventory_lines.append(
        f"{target.IPAddress} ansible_port={target.SSHPort} ansible_user={target.SSHUsername} ansible_ssh_private_key_file={key_path}"
    )
    
    inventory_path = os.path.join(runner_dir, "inventory")
    with open(inventory_path, "w") as f:
        f.write("\n".join(inventory_lines).strip() + "\n")
    
    loop = asyncio.get_running_loop()
    playbook_results = []
    all_success = True

    try:
        playbook_path = os.path.join(os.getcwd(), "auto_harden", AUTO_HARDEN_PLAYBOOK_OS_VERSION[os_version_name])

        runner_result = await loop.run_in_executor(
            None,
            lambda pb=playbook_path: ansible_runner.run(
                private_data_dir=runner_dir,
                playbook=pb,
                inventory=inventory_path,
                ident=f"{target.IPAddress}_{AUTO_HARDEN_PLAYBOOK_OS_VERSION[os_version_name]}"
            )
        )

        artifact_dir = os.path.join(runner_dir, "artifacts", f"{target.IPAddress}_{AUTO_HARDEN_PLAYBOOK_OS_VERSION[os_version_name]}")
        rc_path = os.path.join(artifact_dir, "rc")

        if os.path.exists(rc_path):
            with open(rc_path) as f:
                rc = int(f.read().strip())
        else:
            rc = runner_result.rc

        playbook_results.append({
            "playbook": AUTO_HARDEN_PLAYBOOK_OS_VERSION[os_version_name],
            "status": runner_result.status,
            "rc": rc,
            "stdout": runner_result.stdout.read() if runner_result.stdout else "No output" # type: ignore
        })
        
        if rc != 0:
            all_success = False
        
        return {
            "host": target.IPAddress,
            "results": playbook_results
        }
    
    finally:
        if all_success:
            if os.path.exists(key_path):
                os.remove(key_path)
            if os.path.exists(runner_dir):
                shutil.rmtree(runner_dir)
        else:
            print(f"⚠️ Skipping cleanup for debugging, {runner_dir}.")

async def execute_selected_playbook_on_single_target(playbooks: list[str], target: Target):
    runner_dir = mkdtemp(prefix="runner_")
    project_dir = os.path.join(runner_dir, "project")
    os.makedirs(project_dir, exist_ok=True)

    key_file = NamedTemporaryFile(delete=False, mode='w', dir=runner_dir)
    key_file.write(target.SSHKey.strip() + "\n")
    key_file.close()
    os.chmod(key_file.name, 0o600)
    key_path = key_file.name

    inventory_lines = ["[target]"]
    inventory_lines.append(
        f"{target.IPAddress} ansible_port={target.SSHPort} ansible_user={target.SSHUsername} ansible_ssh_private_key_file={key_path}"
    )
    
    inventory_path = os.path.join(runner_dir, "inventory")
    with open(inventory_path, "w") as f:
        f.write("\n".join(inventory_lines).strip() + "\n")
    
    loop = asyncio.get_running_loop()
    playbook_results = []
    all_success = True

    try:
        for playbook in playbooks:
            playbook_path = os.path.join(os.getcwd(), HARDEN_FILES, playbook)

            playbook_start = []
            event_list = {
                "all": [],
                "ok": [],
                "failed": [],
                "unreachable": [],
                "skipped": []
            }
            recap = []
            
            def event_handler(event):
                _event = event.get('event')
                if _event in RUNNER_EVENTS:
                    event_list["all"].append(event)
                    if _event == RUNNER_OK:
                        event_list["ok"].append(event)
                    elif _event == RUNNER_FAILED:
                        event_list["failed"].append(event)
                    elif _event == RUNNER_UNREACHABLE:
                        event_list["unreachable"].append(event)
                    elif _event == RUNNER_SKIPPED:
                        event_list["skipped"].append(event)
                elif _event == RECAP_EVENT:
                    recap.append(event)
                elif _event == PLAYBOOK_START:
                    playbook_start.append(event)


            runner_result = await loop.run_in_executor(
                None,
                lambda pb=playbook_path: ansible_runner.run(
                    private_data_dir=runner_dir,
                    playbook=pb,
                    inventory=inventory_path,
                    ident=f"{target.hostName}_{target.IPAddress}_{playbook}",
                    event_handler=event_handler,
                    # quiet=True
                )
            )

            artifact_dir = os.path.join(runner_dir, "artifacts", f"{target.hostName}_{target.IPAddress}_{playbook}")
            rc_path = os.path.join(artifact_dir, "rc")

            if os.path.exists(rc_path):
                with open(rc_path) as f:
                    rc = int(f.read().strip())
            else:
                rc = runner_result.rc
            
            playbook_results.append({
                "playbook": playbook,
                "status": runner_result.status,
                "rc": rc,
                "playbook_start": playbook_start,
                "events": event_list, # type: ignore
                "recap": recap,
                "stdout": runner_result.stdout.read() if runner_result.stdout else "No output", # type: ignore
            })

        return {
            "host": f"{target.hostName}",
            "ip": f"{target.IPAddress}",
            "playbook_results": playbook_results
        }

    finally:
        if os.path.exists(key_path):
            os.remove(key_path)
        if os.path.exists(runner_dir):
            shutil.rmtree(runner_dir)

def event_validation(_event):
    pass
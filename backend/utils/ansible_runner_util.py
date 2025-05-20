import asyncio
import os
import shutil
from tempfile import NamedTemporaryFile, mkdtemp

import ansible_runner
from models.target import Target

AUTO_HARDEN_PLAYBOOK_OS_VERSION = {
    "debian_11": "auto_hardening_debian11.yml",
    "debian_12": "auto_hardening_debian12.yml",
    "ubuntu_22": "auto_hardening_ubuntu22.yml",
    "ubuntu_24": "auto_hardening_ubuntu24.yml",
}
SELECTED_HARDEN_PLAYBOOK_OS_VERSION = {
    "debian_11": "selected_hardening_debian11.yml",
    "debian_12": "selected_hardening_debian12.yml",
    "ubuntu_22": "selected_hardening_ubuntu22.yml",
    "ubuntu_24": "selected_hardening_ubuntu24.yml",
}

PLAYBOOK_START = "playbook_on_play_start"
RECAP_EVENT = "playbook_on_stats"
RUNNER_OK = "runner_on_ok"
RUNNER_FAILED = "runner_on_failed"
RUNNER_UNREACHABLE = "runner_on_unreachable"
RUNNER_SKIPPED = "runner_on_skipped"
RUNNER_EVENTS = [
    RUNNER_OK,
    RUNNER_FAILED,
    RUNNER_UNREACHABLE,
    RUNNER_SKIPPED,
]


HARDEN_FILES = "harden_files"
PATCH_FILES = "patch_files"


async def execute_auto_harden_on_single_target(os_version_name: str, target: Target):
    runner_dir = mkdtemp(prefix="runner_")
    project_dir = os.path.join(runner_dir, "project")
    os.makedirs(project_dir, exist_ok=True)

    key_file = NamedTemporaryFile(delete=False, mode="w", dir=runner_dir)
    key_file.write(target.ssh_private_key.strip() + "\n")
    key_file.close()
    os.chmod(key_file.name, 0o600)
    key_path = key_file.name

    inventory_lines = ["[target]"]
    inventory_lines.append(
        f"{target.ip_address} ansible_port={target.ssh_port} ansible_user={target.ssh_username} ansible_ssh_private_key_file={key_path}"
    )

    inventory_path = os.path.join(runner_dir, "inventory")
    with open(inventory_path, "w") as f:
        f.write("\n".join(inventory_lines).strip() + "\n")

    loop = asyncio.get_running_loop()
    playbook_results = []

    try:
        playbook_path = os.path.join(
            os.getcwd(), "auto_harden", AUTO_HARDEN_PLAYBOOK_OS_VERSION[os_version_name]
        )

        playbook_start = []
        event_list = {
            "all": [],
            "ok": [],
            "failed": [],
            "unreachable": [],
            "skipped": [],
        }
        recap = []

        def event_handler(event):
            _event = event.get("event")
            _event_validation(_event, event, event_list, recap, playbook_start)

        runner_result = await loop.run_in_executor(
            None,
            lambda pb=playbook_path: ansible_runner.run(
                private_data_dir=runner_dir,
                playbook=pb,
                inventory=inventory_path,
                ident=f"{target.host_name}_{target.ip_address}_{AUTO_HARDEN_PLAYBOOK_OS_VERSION[os_version_name]}",
                event_handler=event_handler,
                quiet=True,
            ),
        )

        artifact_dir = os.path.join(
            runner_dir,
            "artifacts",
            f"{target.host_name}_{target.ip_address}_{AUTO_HARDEN_PLAYBOOK_OS_VERSION[os_version_name]}",
        )
        rc_path = os.path.join(artifact_dir, "rc")

        if os.path.exists(rc_path):
            with open(rc_path) as f:
                rc = int(f.read().strip())
        else:
            rc = runner_result.rc

        playbook_results.append(
            {
                "name": AUTO_HARDEN_PLAYBOOK_OS_VERSION[os_version_name],
                "status": runner_result.status,
                "rc": rc,
                "playbook_start": playbook_start,
                "events": event_list,
                "recap": recap,
                "stdout": runner_result.stdout.read()  # type: ignore
                if runner_result.stdout  # type: ignore
                else "No output",
            }
        )

        return {
            "host": f"{target.host_name}",
            "ip": f"{target.ip_address}",
            "playbook_results": playbook_results,
        }

    finally:
        if os.path.exists(key_path):
            os.remove(key_path)
        if os.path.exists(runner_dir):
            shutil.rmtree(runner_dir)


async def execute_selected_playbook_on_single_target(
    playbooks: list[str], target: Target
):
    runner_dir = mkdtemp(prefix="runner_")
    project_dir = os.path.join(runner_dir, "project")
    os.makedirs(project_dir, exist_ok=True)

    key_file = NamedTemporaryFile(delete=False, mode="w", dir=runner_dir)
    key_file.write(target.ssh_private_key.strip() + "\n")
    key_file.close()
    os.chmod(key_file.name, 0o600)
    key_path = key_file.name

    inventory_lines = ["[target]"]
    inventory_lines.append(
        f"{target.ip_address} ansible_port={target.ssh_port} ansible_user={target.ssh_username} ansible_ssh_private_key_file={key_path}"
    )

    inventory_path = os.path.join(runner_dir, "inventory")
    with open(inventory_path, "w") as f:
        f.write("\n".join(inventory_lines).strip() + "\n")

    loop = asyncio.get_running_loop()
    playbook_results = []

    try:
        for playbook in playbooks:
            playbook_path = os.path.join(os.getcwd(), HARDEN_FILES, playbook)

            playbook_start = []
            event_list = {
                "all": [],
                "ok": [],
                "failed": [],
                "unreachable": [],
                "skipped": [],
            }
            recap = []

            def event_handler(event):
                _event = event.get("event")
                _event_validation(_event, event, event_list, recap, playbook_start)

            runner_result = await loop.run_in_executor(
                None,
                lambda pb=playbook_path: ansible_runner.run(
                    private_data_dir=runner_dir,
                    playbook=pb,
                    inventory=inventory_path,
                    ident=f"{target.host_name}_{target.ip_address}_{playbook}",
                    event_handler=event_handler,
                    quiet=True,
                ),
            )

            artifact_dir = os.path.join(
                runner_dir,
                "artifacts",
                f"{target.host_name}_{target.ip_address}_{playbook}",
            )
            rc_path = os.path.join(artifact_dir, "rc")

            if os.path.exists(rc_path):
                with open(rc_path) as f:
                    rc = int(f.read().strip())
            else:
                rc = runner_result.rc

            playbook_results.append(
                {
                    "name": playbook,
                    "status": runner_result.status,
                    "rc": rc,
                    "playbook_start": playbook_start,
                    "events": event_list,
                    "recap": recap,
                    "stdout": runner_result.stdout.read()  # type: ignore
                    if runner_result.stdout  # type: ignore
                    else "No output",
                }
            )

        return {
            "host": f"{target.host_name}",
            "ip": f"{target.ip_address}",
            "playbook_results": playbook_results,
        }

    finally:
        if os.path.exists(key_path):
            os.remove(key_path)
        if os.path.exists(runner_dir):
            shutil.rmtree(runner_dir)


async def execute_selected_control_on_single_target(
    os_version_name: str, target: Target, controls: list[dict]
):
    runner_dir = mkdtemp(prefix="runner_")
    project_dir = os.path.join(runner_dir, "project")
    os.makedirs(project_dir, exist_ok=True)

    key_file = NamedTemporaryFile(delete=False, mode="w", dir=runner_dir)
    key_file.write(target.ssh_private_key.strip() + "\n")
    key_file.close()
    os.chmod(key_file.name, 0o600)
    key_path = key_file.name

    inventory_lines = ["[target]"]
    inventory_lines.append(
        f"{target.ip_address} ansible_port={target.ssh_port} ansible_user={target.ssh_username} ansible_ssh_private_key_file={key_path}"
    )

    inventory_path = os.path.join(runner_dir, "inventory")
    with open(inventory_path, "w") as f:
        f.write("\n".join(inventory_lines).strip() + "\n")

    loop = asyncio.get_running_loop()
    playbook_results = []

    try:
        for control in controls:
            playbook_path = os.path.join(
                os.getcwd(),
                "selected_harden",
                SELECTED_HARDEN_PLAYBOOK_OS_VERSION[os_version_name],
            )

            playbook_start = []
            event_list = {
                "all": [],
                "ok": [],
                "failed": [],
                "unreachable": [],
                "skipped": [],
            }
            recap = []

            def event_handler(event):
                _event = event.get("event")
                _event_validation(_event, event, event_list, recap, playbook_start)

            runner_result = await loop.run_in_executor(
                None,
                lambda pb=playbook_path: ansible_runner.run(
                    private_data_dir=runner_dir,
                    playbook=pb,
                    inventory=inventory_path,
                    ident=f"{target.host_name}_{target.ip_address}_{SELECTED_HARDEN_PLAYBOOK_OS_VERSION[os_version_name]}",
                    event_handler=event_handler,
                    extravars=control.dict()["os_version_name"][os_version_name],  # type: ignore
                    quiet=True,
                ),
            )

            artifact_dir = os.path.join(
                runner_dir,
                "artifacts",
                f"{target.host_name}_{target.ip_address}_{SELECTED_HARDEN_PLAYBOOK_OS_VERSION[os_version_name]}",
            )
            rc_path = os.path.join(artifact_dir, "rc")

            if os.path.exists(rc_path):
                with open(rc_path) as f:
                    rc = int(f.read().strip())
            else:
                rc = runner_result.rc

            playbook_results.append(
                {
                    "name": SELECTED_HARDEN_PLAYBOOK_OS_VERSION[os_version_name],
                    "status": runner_result.status,
                    "rc": rc,
                    "playbook_start": playbook_start,
                    "events": event_list,
                    "recap": recap,
                    "stdout": runner_result.stdout.read()  # type: ignore
                    if runner_result.stdout  # type: ignore
                    else "No output",
                }
            )

        return {
            "host": f"{target.host_name}",
            "ip": f"{target.ip_address}",
            "playbook_results": playbook_results,
        }

    finally:
        if os.path.exists(key_path):
            os.remove(key_path)
        if os.path.exists(runner_dir):
            shutil.rmtree(runner_dir)


async def execute_selected_patch_on_single_target(
    playbook: str, extravars, target: Target
):
    runner_dir = mkdtemp(prefix="runner_")
    project_dir = os.path.join(runner_dir, "project")
    os.makedirs(project_dir, exist_ok=True)

    key_file = NamedTemporaryFile(delete=False, mode="w", dir=runner_dir)
    key_file.write(target.ssh_private_key.strip() + "\n")
    key_file.close()
    os.chmod(key_file.name, 0o600)
    key_path = key_file.name

    inventory_lines = ["[target]"]
    inventory_lines.append(
        f"{target.ip_address} ansible_port={target.ssh_port} ansible_user={target.ssh_username} ansible_ssh_private_key_file={key_path}"
    )

    inventory_path = os.path.join(runner_dir, "inventory")
    with open(inventory_path, "w") as f:
        f.write("\n".join(inventory_lines).strip() + "\n")

    loop = asyncio.get_running_loop()
    playbook_results = []

    try:
        playbook_path = os.path.join(os.getcwd(), PATCH_FILES, playbook)

        playbook_start = []
        event_list = {
            "all": [],
            "ok": [],
            "failed": [],
            "unreachable": [],
            "skipped": [],
        }
        recap = []

        def event_handler(event):
            _event = event.get("event")
            _event_validation(_event, event, event_list, recap, playbook_start)

        runner_result = await loop.run_in_executor(
            None,
            lambda pb=playbook_path: ansible_runner.run(
                private_data_dir=runner_dir,
                playbook=pb,
                inventory=inventory_path,
                ident=f"{target.host_name}_{target.ip_address}_{playbook}",
                event_handler=event_handler,
                extravars=extravars,
                quiet=True,
            ),
        )

        artifact_dir = os.path.join(
            runner_dir,
            "artifacts",
            f"{target.host_name}_{target.ip_address}_{playbook}",
        )
        rc_path = os.path.join(artifact_dir, "rc")

        if os.path.exists(rc_path):
            with open(rc_path) as f:
                rc = int(f.read().strip())
        else:
            rc = runner_result.rc

        playbook_results.append(
            {
                "name": playbook,
                "status": runner_result.status,
                "rc": rc,
                "playbook_start": playbook_start,
                "events": event_list,
                "recap": recap,
                "stdout": runner_result.stdout.read()  # type: ignore
                if runner_result.stdout  # type: ignore
                else "No output",
            }
        )

        return {
            "host": f"{target.host_name}",
            "ip": f"{target.ip_address}",
            "playbook_results": playbook_results,
        }

    finally:
        if os.path.exists(key_path):
            os.remove(key_path)
        if os.path.exists(runner_dir):
            shutil.rmtree(runner_dir)


def _event_validation(_event, event, event_list, recap, playbook_start):
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

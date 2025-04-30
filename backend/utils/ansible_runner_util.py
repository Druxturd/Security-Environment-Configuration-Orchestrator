import asyncio
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

async def execute_auto_harden_on_single_target(os_version_name: str, target: Target):
    runner_dir = mkdtemp(prefix="runner_")
    project_dir = os.path.join(runner_dir, "project")
    os.makedirs(project_dir, exist_ok=True)

    key_file = NamedTemporaryFile(delete=False, mode='w', dir=runner_dir)
    key_file.write(target.SSHKey.strip() + "\n")
    key_file.close()
    os.chmod(key_file.name, 0o600)
    key_path = key_file.name

    inventory_lines = [f"[{os_version_name}]"]
    if target.hostName == "test-debian-12": # test unit debian 12
        inventory_lines.append(
            f"{target.IPAddress} ansible_port=2222 ansible_user=root ansible_ssh_private_key_file={key_path}"
        )
    elif target.hostName == "test-ubuntu-24": # test unit ubuntu 24
        inventory_lines.append(
            f"{target.IPAddress} ansible_port=2223 ansible_user=root ansible_ssh_private_key_file={key_path}"
        )
    else:
        inventory_lines.append(
            f"{target.IPAddress} ansible_user={target.hostName} ansible_ssh_private_key_file={key_path}"
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
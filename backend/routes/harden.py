import asyncio
import shutil
from tempfile import NamedTemporaryFile, mkdtemp
import ansible_runner
from fastapi import APIRouter
from dotenv import load_dotenv
from models.target import TargetList, Target
from utils.model_util import grouping_os
from utils.ansible_runner_util import execute_auto_harden_on_single_target
import os

router = APIRouter()

load_dotenv()
FILE_DIR = os.getenv("HARDEN_FILE_DIR")
BASE_HARDEN_URL = "/harden"
HARDEN_FILES = "harden_files"

@router.get(BASE_HARDEN_URL)
def list_harden_files():
    try:
        files = os.listdir(FILE_DIR)
        return {"harden_list": files}
    except FileNotFoundError:
        return {"error": "File not found"}

@router.post(f"{BASE_HARDEN_URL}/execute")
async def execute_selected_playbook_on_target_list(playbooks: list[str], targets: TargetList):

    async def execute_selected_playbook_on_single_target(target: Target):
        runner_dir = mkdtemp(prefix="runner_")
        project_dir = os.path.join(runner_dir, "project")
        os.makedirs(project_dir, exist_ok=True)


        key_file = NamedTemporaryFile(delete=False, mode='w', dir=runner_dir)
        key_file.write(target.SSHKey.strip() + '\n')
        key_file.close()
        os.chmod(key_file.name, 0o600)
        key_path = key_file.name

        inventory_lines = ["[target]"]
        # """
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
        # """

        inventory_path = os.path.join(runner_dir, "inventory")
        with open(inventory_path, "w") as f:
            f.write("\n".join(inventory_lines).strip() + '\n')

        loop = asyncio.get_running_loop()
        playbook_results = []
        all_success = True

        try:
            for playbook in playbooks:
                playbook_path = os.path.join(os.getcwd(), HARDEN_FILES, playbook)

                runner_result = await loop.run_in_executor(
                    None,
                    lambda pb=playbook_path: ansible_runner.run(
                        private_data_dir=runner_dir,
                        playbook=pb,
                        inventory=inventory_path,
                        ident=f"{target.IPAddress}_{playbook}"
                    )
                )

                artifact_dir = os.path.join(runner_dir, "artifacts", f"{target.IPAddress}_{playbook}")
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
                    "stdout": runner_result.stdout.read() if runner_result.stdout else "No output"  # type: ignore
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

    tasks = [execute_selected_playbook_on_single_target(target) for target in targets.target_list]
    results = await asyncio.gather(*tasks)
    return {"results": results}

@router.post(f"{BASE_HARDEN_URL}/auto-execute")
async def execute_auto_harden_on_target_list(targets: TargetList):
    grouped_OS = grouping_os(targets)
    results = []

    async def execute_auto_harden_on_supported_version(os_version_name: str):
        tasks = [execute_auto_harden_on_single_target(os_version_name, target) for target in grouped_OS[os_version_name]]
        return await asyncio.gather(*tasks)

    if len(grouped_OS["debian-11"]) != 0:
        results.append(execute_auto_harden_on_supported_version("debian-11"))
    if len(grouped_OS["debian-12"]) != 0:
        results.append(execute_auto_harden_on_supported_version("debian-12"))
    if len(grouped_OS["ubuntu-20"]) != 0:
        results.append(execute_auto_harden_on_supported_version("ubuntu-20"))
    if len(grouped_OS["ubuntu-22"]) != 0:
        results.append(execute_auto_harden_on_supported_version("ubuntu-22"))
    if len(grouped_OS["ubuntu-24"]) != 0:
        results.append(execute_auto_harden_on_supported_version("ubuntu-24"))

    return {"results": results}
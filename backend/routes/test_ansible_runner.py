import asyncio
import shutil
from tempfile import NamedTemporaryFile, mkdtemp
from fastapi import APIRouter
from pydantic import BaseModel
import ansible_runner
import os

router = APIRouter()

class Target(BaseModel):
    IPAddress: str
    hostName: str
    SSHKey: str

class TargetList(BaseModel):
    target_list: list[Target]

@router.post("/install-nginx")
async def run_on_multiple_target(payload: TargetList):    
    
    async def run_on_single_target(target: Target):
        runner_dir = mkdtemp(prefix="runner_")
        project_dir = os.path.join(runner_dir, "project")
        os.makedirs(project_dir, exist_ok=True)

        playbook_src = os.path.join(os.getcwd(), "test_ansible", "install_nginx.yml")
        playbook_dst = os.path.join(project_dir, "install_nginx.yml")
        shutil.copyfile(playbook_src, playbook_dst)

        key_file = NamedTemporaryFile(delete=False, mode='w', dir=runner_dir)
        key_file.write(target.SSHKey.strip() + '\n')
        key_file.close()
        os.chmod(key_file.name, 0o600)
        key_path = key_file.name


        inventory_lines = ["[target]"]
        # """
        if target.hostName == "ansible-debian": # test unit debian 12
            inventory_lines.append(
                f"{target.IPAddress} ansible_port=2222 ansible_user=root ansible_ssh_private_key_file={key_path}"
            )
        elif target.hostName == "ansible-ubuntu": # test unit ubuntu 24
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

        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None,
                lambda: ansible_runner.run(
                private_data_dir=runner_dir,
                playbook=playbook_dst,
                inventory=inventory_path
                )
            )

            return {
                # "tes": 1
                "target": target.IPAddress,
                "status": result.status,
                "rc": result.rc,
                "stdout": result.stdout.read() if result.stdout else "No output"
            }

        finally:
            # return 1
            if result.rc == 0:
                if os.path.exists(key_path):
                    os.remove(key_path)
                if os.path.exists(runner_dir):
                    shutil.rmtree(runner_dir)
            else:
                print(f"⚠️ Skipping cleanup for debugging, {runner_dir}.")
    
    tasks = [run_on_single_target(target) for target in payload.target_list]
    results = await asyncio.gather(*tasks)

    return {"results": results}

@router.post("/uninstall-nginx")
async def run_on_multiple_target(payload: TargetList):    
    
    async def run_on_single_target(target: Target):
        runner_dir = mkdtemp(prefix="runner_")
        project_dir = os.path.join(runner_dir, "project")
        os.makedirs(project_dir, exist_ok=True)

        playbook_src = os.path.join(os.getcwd(), "test_ansible", "uninstall_nginx.yml")
        playbook_dst = os.path.join(project_dir, "install_nginx.yml")
        shutil.copyfile(playbook_src, playbook_dst)

        key_file = NamedTemporaryFile(delete=False, mode='w', dir=runner_dir)
        key_file.write(target.SSHKey.strip() + '\n')
        key_file.close()
        os.chmod(key_file.name, 0o600)
        key_path = key_file.name


        inventory_lines = ["[target]"]
        if target.hostName == "ansible-debian": # test unit
            inventory_lines.append(
                f"{target.IPAddress} ansible_port=2222 ansible_user=root ansible_ssh_private_key_file={key_path}"
            )
        elif target.hostName == "ansible-ubuntu": # test unit
            inventory_lines.append(
                f"{target.IPAddress} ansible_port=2223 ansible_user=root ansible_ssh_private_key_file={key_path}"
            )
        else:
            inventory_lines.append(
                f"{target.IPAddress} ansible_user={target.hostName} ansible_ssh_private_key_file={key_path}"
            )

        inventory_path = os.path.join(runner_dir, "inventory")
        with open(inventory_path, "w") as f:
            f.write("\n".join(inventory_lines).strip() + '\n')

        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None,
                lambda: ansible_runner.run(
                private_data_dir=runner_dir,
                playbook=playbook_dst,
                inventory=inventory_path
                )
            )

            return {
                # "tes": 1
                "target": target.IPAddress,
                "status": result.status,
                "rc": result.rc,
                "stdout": result.stdout.read() if result.stdout else "No output"
            }

        finally:
            # return 1
            if result.rc == 0:
                if os.path.exists(key_path):
                    os.remove(key_path)
                if os.path.exists(runner_dir):
                    shutil.rmtree(runner_dir)
            else:
                print(f"⚠️ Skipping cleanup for debugging, {runner_dir}.")
    
    tasks = [run_on_single_target(target) for target in payload.target_list]
    results = await asyncio.gather(*tasks)

    return {"results": results}
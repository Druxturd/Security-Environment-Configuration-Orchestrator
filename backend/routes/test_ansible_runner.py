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
async def run_on_multiple_hosts(payload: TargetList):    
    temp_keys = []
    runner_dir = mkdtemp(prefix="runner_")
    project_dir = os.path.join(runner_dir, "project")
    os.makedirs(project_dir, exist_ok=True)

    try:
        playbook_src = os.path.join(os.getcwd(), "test_ansible", "install_nginx.yml")
        playbook_dst = os.path.join(project_dir, "install_nginx.yml")
        shutil.copyfile(playbook_src, playbook_dst)

        print(len(payload.target_list))

        inventory_lines = ["[target]"]
        for host in payload.target_list:
            key_file = NamedTemporaryFile(delete=False, mode='w', dir=runner_dir)
            key_file.write(host.SSHKey.strip() + '\n')
            key_file.close()
            os.chmod(key_file.name, 0o600)
            temp_keys.append(key_file.name)

            key_path = key_file.name
            if host.hostName == "ansible-debian":
                inventory_lines.append(
                    f"{host.IPAddress} ansible_port=2222 ansible_user={host.hostName} ansible_ssh_private_key_file={key_path}"
                )
            elif host.hostName == "ansible-ubuntu":
                inventory_lines.append(
                    f"{host.IPAddress} ansible_port=2223 ansible_user={host.hostName} ansible_ssh_private_key_file={key_path}"
                )
            else:
                inventory_lines.append(
                    f"{host.IPAddress} ansible_user={host.hostName} ansible_ssh_private_key_file={key_path}"
                )
        
        inventory_path = os.path.join(runner_dir, "inventory")
        with open(inventory_path, "w") as f:
            f.write("\n".join(inventory_lines).strip() + '\n')
        
        result = ansible_runner.run(
            private_data_dir=runner_dir,
            playbook=playbook_dst,
            inventory=inventory_path,
            verbosity=4
        )
        # await asyncio.sleep(2)
        return {
            "tes": 1
            # "status": result.status,
            # "rc": result.rc,
            # "stdout": result.stdout.read() if result.stdout else "No output"
        }
    finally:
        # return 1
        if result.rc == 0:
            for key_path in temp_keys:
                if os.path.exists(key_path):
                    os.remove(key_path)
            if os.path.exists(runner_dir):
                shutil.rmtree(runner_dir)
        else:
            print("⚠️ Skipping cleanup for debugging, playbook failed.")

        # for key_path in temp_keys:
        #     if os.path.exists(key_path):
        #         os.remove(key_path)
        # if os.path.exists(runner_dir):
        #     shutil.rmtree(runner_dir)
            
"""
    temp_key_files = []
    try:
        inventory_lines = ["[target]"]

        for item in payload.hosts:
            key_file = NamedTemporaryFile(delete=False, mode='w', prefix='ssh_', suffix='.pem')
            key_file.write(item.ssh_key)
            key_file.close()
            os.chmod(key_file.name, 0o600)
            temp_key_files.append(key_file.name)

            if item.username == "ansible-debian":
                inventory_lines.append(
                    f"{item.host} ansible_port=2222 ansible_user={item.username} ansible_ssh_private_key_file={key_file.name}"
                )
            elif item.username == "ansible-ubuntu":
                inventory_lines.append(
                    f"{item.host} ansible_port=2223 ansible_user={item.username} ansible_ssh_private_key_file={key_file.name}"
                )
            else:
                inventory_lines.append(
                    f"{item.host} ansible_user={item.username} ansible_ssh_private_key_file={key_file.name}"
                )
            
        with NamedTemporaryFile(delete=False, mode='w', prefix='inv_', suffix='.ini') as inv_file:
            inv_file.write("\n".join(inventory_lines))
            invenotry_path = inv_file.name

        result = ansible_runner.run(
            private_data_dir='.',
            inventory=invenotry_path,
            playbook='install_nginx.yml',
            verbosity=1
        )

        return {
            "status": result.status,
            "rc": result.rc,
            "stdout": result.stdout.read() if result.stdout else "No output"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        for key_path in temp_key_files:
            if os.path.exists(key_path):
                os.remove(key_path)
        
        if 'inventory_path' in locals() and os.path.exists(invenotry_path):
            os.remove(invenotry_path)
"""
import asyncio
import shutil
from tempfile import NamedTemporaryFile, mkdtemp
import ansible_runner
from fastapi import APIRouter
from dotenv import load_dotenv
from models.target import TargetList, Target
from utils.model_util import grouping_os
from utils.ansible_runner_util import execute_auto_harden_on_single_target, execute_selected_playbook_on_single_target
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

    tasks = [execute_selected_playbook_on_single_target(playbooks, target) for target in targets.target_list]
    results = await asyncio.gather(*tasks)

    return {"task_results": results}

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

    return {"task_results": results}
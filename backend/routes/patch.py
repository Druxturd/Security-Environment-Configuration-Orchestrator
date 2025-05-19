import asyncio
import os

from dotenv import load_dotenv
from fastapi import APIRouter
from models.patch_model import PatchModel
from utils.ansible_runner_util import execute_selected_patch_on_single_target

router = APIRouter()

load_dotenv()
FILE_DIR = os.getenv("PATCH_FILE_DIR")
BASE_PATCH_URL = "/patch"


@router.get(BASE_PATCH_URL)
def all_patch_files():
    try:
        files = os.listdir(FILE_DIR)
        return {"patch_list": files}
    except FileNotFoundError:
        return {"error": "File not found"}


@router.post(f"{BASE_PATCH_URL}/execute")
async def execute_port_patch_on_target_list(data: PatchModel):
    tasks = []

    for target in data.targets.target_list:
        tasks.append(
            execute_selected_patch_on_single_target(
                data.playbook, data.extra_vars, target
            )
        )

    results = await asyncio.gather(*tasks)

    return {"task_results": results}

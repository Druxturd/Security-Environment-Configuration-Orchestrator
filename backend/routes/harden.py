import asyncio
import os

from dotenv import load_dotenv
from fastapi import APIRouter
from models.harden_model import AutoHardenModel, SelectedHardenModel
from utils.ansible_runner_util import (
    execute_auto_harden_on_single_target,
    execute_selected_control_on_single_target,
)
from utils.model_util import grouping_os

router = APIRouter()

load_dotenv()
FILE_DIR = os.getenv("HARDEN_FILE_DIR")
BASE_HARDEN_URL = "/harden"


@router.get(BASE_HARDEN_URL)
def list_harden_files():
    try:
        files = os.listdir(FILE_DIR)
        return {"harden_list": files}
    except FileNotFoundError:
        return {"error": "File not found"}


@router.post(f"{BASE_HARDEN_URL}/execute")
async def execute_selected_control_on_target_list(data: SelectedHardenModel):
    grouped_OS = grouping_os(data.targets)

    async def execute_selected_control_on_supported_version(
        os_version_name: str, controls: list[dict]
    ):
        tasks = [
            execute_selected_control_on_single_target(
                os_version_name,
                target,
                controls,
            )
            for target in grouped_OS[os_version_name]
        ]

        return await asyncio.gather(*tasks)

    all_tasks = []
    for os_version in ["debian_11", "debian_12", "ubuntu_22", "ubuntu_24"]:
        if not grouped_OS.get(os_version):
            continue
        controls = []
        for control in data.controls:
            selected_control = control.model_dump()["os_version_name"][os_version]
            if selected_control:
                controls.append(control.model_dump())
        all_tasks.append(
            execute_selected_control_on_supported_version(os_version, controls)
        )

    all_results = await asyncio.gather(*all_tasks)

    return {"selected_harden_results": all_results}


@router.post(f"{BASE_HARDEN_URL}/auto-execute")
async def execute_auto_harden_on_target_list(data: AutoHardenModel):
    grouped_OS = grouping_os(data.targets)

    async def execute_auto_harden_on_supported_version(os_version_name: str):
        tasks = [
            execute_auto_harden_on_single_target(os_version_name, target)
            for target in grouped_OS[os_version_name]
        ]

        return await asyncio.gather(*tasks)
        # for target in grouped_OS[os_version_name]:
        #     tasks.append(execute_auto_harden_on_single_target(os_version_name, target))

        # all_results.append(await asyncio.gather(*tasks))

    # if len(grouped_OS["debian_11"]) != 0:
    #     await execute_auto_harden_on_supported_version("debian_11")

    # if len(grouped_OS["debian_12"]) != 0:
    #     await execute_auto_harden_on_supported_version("debian_12")

    # if len(grouped_OS["ubuntu_22"]) != 0:
    #     await execute_auto_harden_on_supported_version("ubuntu_22")

    # if len(grouped_OS["ubuntu_24"]) != 0:
    #     await execute_auto_harden_on_supported_version("ubuntu_24")

    all_tasks = []
    for os_version in ["debian_11", "debian_12", "ubuntu_22", "ubuntu_24"]:
        if not grouped_OS.get(os_version):
            continue
        all_tasks.append(execute_auto_harden_on_supported_version(os_version))

    all_results = await asyncio.gather(*all_tasks)

    return {"auto_harden_results": all_results}

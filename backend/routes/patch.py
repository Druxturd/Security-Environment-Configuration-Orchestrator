from fastapi import APIRouter
from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()
FILE_DIR = os.getenv("PATCH_FILE_DIR")
ALL_DIR = f"{FILE_DIR}/{os.getenv("ALL_PATCH_DIR")}"
SPECIFIC_DIR = f"{FILE_DIR}/{os.getenv("SPECIFIC_PATCH_DIR")}"
BASE_PATCH_URL = "/patch"

@router.get(f"{BASE_PATCH_URL}/all-host")
def all_host_patch_files():
    try:
        files = os.listdir(ALL_DIR)
        return {"patch_list": files}
    except FileNotFoundError:
        return {"error": "File not found"}

@router.get(f"{BASE_PATCH_URL}/specific-host")
def specific_host_patch_files():
    try:
        files = os.listdir(SPECIFIC_DIR)
        return {"patch_list": files}
    except FileNotFoundError:
        return {"error": "File not found"}
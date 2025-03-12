from fastapi import APIRouter
from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()
FILE_DIR = os.getenv("PATCH_FILE_DIR")

@router.get("/patch")
def list_patch_files():
    try:
        files = os.listdir(FILE_DIR)
        return {"patch_list": files}
    except FileNotFoundError:
        return {"error": "File not found"}
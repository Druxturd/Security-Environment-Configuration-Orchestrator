from fastapi import APIRouter
from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()
FILE_DIR = os.getenv("HARDEN_FILE_DIR")

@router.get("/harden")
def list_harden_files():
    try:
        files = os.listdir(FILE_DIR)
        return {"harden_list": files}
    except FileNotFoundError:
        return {"error": "File not found"}
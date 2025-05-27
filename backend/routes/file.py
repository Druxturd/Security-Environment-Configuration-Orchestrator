import os
import sys

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/download-template")
def download_template():
    if getattr(sys, "frozen", False):
        BASE_DIR = os.path.join(sys._MEIPASS, "backend")  # type: ignore
    else:
        BASE_DIR = os.path.dirname(__file__)

    template_path = os.path.join(BASE_DIR, "files", "template.xlsx")
    return FileResponse(
        path=template_path,
        filename="template.xlsx",
    )

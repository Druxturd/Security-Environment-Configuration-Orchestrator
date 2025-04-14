from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/download-template")
def download_template():
    return FileResponse(
        "files/template.csv",
        filename="template.csv",
        media_type="text/csv"
    )
from fastapi import APIRouter, UploadFile, File
from app.services.file_service import save_uploaded_file

router = APIRouter()


@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    saved_file = await save_uploaded_file(file)

    return {
        "message": "File uploaded successfully.",
        "file": saved_file
    }
import os
import uuid
from pathlib import Path
from fastapi import UploadFile, HTTPException

from app.config import UPLOAD_DIR, ALLOWED_EXTENSIONS, MAX_FILE_SIZE_MB


def ensure_upload_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)


def validate_file_extension(filename: str):
    file_extension = Path(filename).suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type {file_extension} is not supported."
        )

    return file_extension


async def save_uploaded_file(file: UploadFile):
    ensure_upload_dir()

    file_extension = validate_file_extension(file.filename)

    file_bytes = await file.read()
    file_size_mb = len(file_bytes) / (1024 * 1024)

    if file_size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max allowed size is {MAX_FILE_SIZE_MB} MB."
        )

    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    return {
        "original_filename": file.filename,
        "saved_filename": unique_filename,
        "file_path": file_path,
        "file_size_mb": round(file_size_mb, 2)
    }
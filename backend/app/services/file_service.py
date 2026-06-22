import os
import uuid
from pathlib import Path

from fastapi import UploadFile, HTTPException

from app.config import UPLOAD_DIR, ALLOWED_EXTENSIONS, MAX_FILE_SIZE_MB


def ensure_upload_dir():
    os.makedirs(UPLOAD_DIR, exist_ok=True)


def validate_file_extension(filename: str):
    if not filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing."
        )

    file_extension = Path(filename).suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type '{file_extension}' is not supported."
        )

    return file_extension


async def save_uploaded_file(file: UploadFile):
    ensure_upload_dir()

    file_extension = validate_file_extension(file.filename)

    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    file_size = 0
    max_file_size_bytes = MAX_FILE_SIZE_MB * 1024 * 1024

    try:
        with open(file_path, "wb") as buffer:
            while True:
                chunk = await file.read(1024 * 1024)

                if not chunk:
                    break

                file_size += len(chunk)

                if file_size > max_file_size_bytes:
                    buffer.close()

                    if os.path.exists(file_path):
                        os.remove(file_path)

                    raise HTTPException(
                        status_code=400,
                        detail=f"File too large. Max allowed size is {MAX_FILE_SIZE_MB} MB."
                    )

                buffer.write(chunk)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save uploaded file: {str(e)}"
        )

    file_size_mb = file_size / (1024 * 1024)

    return {
        "original_filename": file.filename,
        "saved_filename": unique_filename,
        "file_path": file_path,
        "file_size_mb": round(file_size_mb, 2)
    }
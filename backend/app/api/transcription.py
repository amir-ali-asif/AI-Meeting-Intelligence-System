from fastapi import APIRouter, UploadFile, File, Form

from app.services.file_service import save_uploaded_file
from app.services.transcription_service import transcribe_audio_file

router = APIRouter()


@router.post("/transcribe-audio")
async def transcribe_audio(
    file: UploadFile = File(...),
    language: str | None = Form(default=None)
):
    """
    Uploads an audio file, saves it locally, sends it to Groq Whisper,
    and returns the transcript.
    """

    saved_file = await save_uploaded_file(file)

    transcription_result = transcribe_audio_file(
        file_path=saved_file["file_path"],
        language=language
    )

    return {
        "message": "Transcription completed successfully.",
        "file": saved_file,
        "transcription": transcription_result
    }
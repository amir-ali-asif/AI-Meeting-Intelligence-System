from fastapi import HTTPException
from groq import Groq

from app.config import GROQ_API_KEY, GROQ_TRANSCRIPTION_MODEL


def get_groq_client():
    if not GROQ_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is missing. Please add it to backend/.env"
        )

    return Groq(api_key=GROQ_API_KEY)


def extract_transcription_text(transcription_response):
    """
    Groq usually returns an object with a .text attribute.
    This helper keeps the code safe if the response format changes slightly.
    """

    if hasattr(transcription_response, "text"):
        return transcription_response.text

    if isinstance(transcription_response, dict):
        return transcription_response.get("text", "")

    return str(transcription_response)


def transcribe_audio_file(file_path: str, language: str | None = None):
    """
    Sends an audio file to Groq Whisper API and returns transcription text.
    """

    client = get_groq_client()

    try:
        with open(file_path, "rb") as audio_file:
            transcription_params = {
                "file": audio_file,
                "model": GROQ_TRANSCRIPTION_MODEL,
                "response_format": "json",
                "temperature": 0.0,
                "prompt": (
                    "This is a meeting conversation. "
                    "The audio may contain English, Urdu, or mixed Urdu-English. "
                    "Keep names, companies, project names, and technical terms accurate."
                )
            }

            if language:
                transcription_params["language"] = language

            transcription = client.audio.transcriptions.create(
                **transcription_params
            )

        transcript_text = extract_transcription_text(transcription)

        if not transcript_text.strip():
            raise HTTPException(
                status_code=422,
                detail="Transcription completed but no speech text was detected."
            )

        return {
            "text": transcript_text.strip(),
            "model": GROQ_TRANSCRIPTION_MODEL
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Transcription failed: {str(e)}"
        )
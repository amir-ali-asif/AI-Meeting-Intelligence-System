import os
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "25"))

ALLOWED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".mp4",
    ".ogg",
    ".webm"
}
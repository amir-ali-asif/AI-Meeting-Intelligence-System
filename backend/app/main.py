from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.transcription import router as transcription_router

app = FastAPI(
    title="AI Meeting Intelligence API",
    description="Backend API for uploading and processing meeting audio.",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router, prefix="/api")
app.include_router(transcription_router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "AI Meeting Intelligence API is running.",
        "version": "2.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
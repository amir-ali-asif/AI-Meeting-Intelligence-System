# AI Meeting Intelligence System

An AI-powered meeting intelligence platform that converts meeting audio into accurate transcripts and will later generate summaries, key points, action items, speaker insights, and meeting reports using Generative AI.

This project is being developed as a solo portfolio-grade AI project with future startup potential.

---

## Project Vision

Meetings are an important part of modern organizations, but many important decisions, tasks, deadlines, and follow-ups are often lost after the meeting ends.

The goal of this project is to build an AI-powered meeting assistant that can:

* Transcribe meeting audio.
* Generate meeting summaries.
* Extract key discussion points.
* Detect action items.
* Identify decisions.
* Support Urdu and English meeting analysis.
* Allow users to ask questions from meeting transcripts.
* Generate professional meeting reports.

---

## Current Development Status

## Week 1 Completed

In Week 1, the foundation of the project was created.

### Week 1 Features

* GitHub repository initialized.
* FastAPI backend created.
* React + Vite frontend created.
* Audio upload API implemented.
* File validation added.
* Uploaded audio files saved locally.
* Frontend connected with backend.
* Basic upload UI created.

---

## Week 2 Completed

In Week 2, cloud-based transcription was added.

### Week 2 Features

* Integrated Groq API for cloud transcription.
* Added Whisper large-v3 model for transcription.
* Created transcription service in the backend.
* Created `/api/transcribe-audio` endpoint.
* User can upload raw audio from the frontend.
* Backend sends raw audio directly to Groq Whisper large-v3.
* Transcript is returned from the API.
* Transcript is displayed on the frontend.
* Loading state added while transcription is processing.
* Copy transcript feature added.

---

## Important Note

Audio preprocessing has **not** been added yet.

Current Week 2 flow:

```text
Raw Audio File
      ↓
FastAPI Backend
      ↓
Groq Whisper large-v3 API
      ↓
Transcript
      ↓
Frontend Display
```

Planned Week 3 improvement:

```text
Raw Audio File
      ↓
FFmpeg Audio Preprocessing
      ↓
Clean Audio
      ↓
Groq Whisper large-v3 API
      ↓
Improved Transcript
      ↓
LLM Summary + Key Points + Action Items
```

---

## Week 2 Workflow

```text
User Uploads Audio File
            ↓
React Frontend
            ↓
FastAPI Backend
            ↓
File Validation
            ↓
Audio File Saved Locally
            ↓
Raw Audio Sent to Groq Whisper large-v3
            ↓
Transcript Returned
            ↓
Transcript Displayed on Frontend
```

---

## Tech Stack

### Frontend

* React
* Vite
* JavaScript
* CSS

### Backend

* FastAPI
* Python
* Uvicorn
* Groq Python SDK

### AI / Cloud API

* Groq Whisper large-v3 for speech-to-text transcription

### Planned AI Stack

* FFmpeg audio preprocessing
* Gemini / Groq LLM API
* LangGraph
* ChromaDB / Qdrant
* RAG-based meeting Q&A
* PostgreSQL / Supabase

---

## Project Structure

```text
ai-meeting-intelligence/
│
├── backend/
│   ├── .env
│   ├── .env.example
│   ├── requirements.txt
│   ├── uploads/
│   │
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   ├── upload.py
│       │   └── transcription.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   ├── file_service.py
│       │   └── transcription_service.py
│       │
│       └── utils/
│           └── __init__.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── App.css
│   │
│   ├── public/
│   └── package.json
│
├── README.md
├── .gitignore
└── docs/
```

---

## Installation Requirements

Before running this project, make sure the following are installed:

* Python 3.11+
* Node.js LTS
* Git
* VS Code

---

## Backend Setup

Navigate to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Run the backend server:

```bash
uvicorn app.main:app --reload
```

Backend will run on:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to the frontend folder:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Run the frontend development server:

```bash
npm run dev
```

Frontend will run on:

```text
http://localhost:5173
```

---

## Environment Variables

Create a `.env` file inside the `backend` folder.

File path:

```text
backend/.env
```

Example:

```env
UPLOAD_DIR=uploads
MAX_FILE_SIZE_MB=25

GROQ_API_KEY=your_real_groq_api_key_here
GROQ_TRANSCRIPTION_MODEL=whisper-large-v3
```

---

## Environment Example File

The `.env.example` file should contain placeholder values only.

File path:

```text
backend/.env.example
```

Example:

```env
UPLOAD_DIR=uploads
MAX_FILE_SIZE_MB=25

GROQ_API_KEY=your_groq_api_key_here
GROQ_TRANSCRIPTION_MODEL=whisper-large-v3
```

---

## Security Note

Never push real API keys to GitHub.

The real API key should only be stored in:

```text
backend/.env
```

The `.env` file must be ignored by Git.

Your `.gitignore` should include:

```gitignore
.env
backend/.env

uploads/
backend/uploads/

venv/
backend/venv/

__pycache__/
node_modules/
frontend/node_modules/
```

---

## API Endpoints

## Health Check

```http
GET /
```

Example response:

```json
{
  "message": "AI Meeting Intelligence API is running.",
  "version": "2.0.0"
}
```

---

## Upload Audio

```http
POST /api/upload-audio
```

This endpoint uploads and saves an audio file locally.

Supported formats:

* MP3
* WAV
* M4A
* MP4
* OGG
* WEBM
* MPEG
* MPGA
* FLAC

Example response:

```json
{
  "message": "File uploaded successfully.",
  "file": {
    "original_filename": "meeting.mp3",
    "saved_filename": "generated-file-id.mp3",
    "file_path": "uploads/generated-file-id.mp3",
    "file_size_mb": 2.4
  }
}
```

---

## Transcribe Audio

```http
POST /api/transcribe-audio
```

This endpoint uploads an audio file, saves it locally, sends the raw audio to Groq Whisper large-v3, and returns the transcript.

Request fields:

| Field    | Type   | Required | Description                                 |
| -------- | ------ | -------- | ------------------------------------------- |
| file     | File   | Yes      | Audio or video file                         |
| language | String | No       | Optional language code such as `en` or `ur` |

Example response:

```json
{
  "message": "Transcription completed successfully.",
  "file": {
    "original_filename": "meeting.mp3",
    "saved_filename": "generated-file-id.mp3",
    "file_path": "uploads/generated-file-id.mp3",
    "file_size_mb": 2.4
  },
  "transcription": {
    "text": "This is the transcript generated from the meeting audio.",
    "model": "whisper-large-v3"
  }
}
```

---

## Current Application Flow

```text
1. User opens the React frontend.
2. User selects an audio file.
3. User optionally selects language.
4. User clicks Transcribe Audio.
5. Frontend sends the file to FastAPI.
6. FastAPI validates the file.
7. FastAPI saves the file locally.
8. FastAPI sends the raw audio file to Groq Whisper large-v3.
9. Groq returns the transcript.
10. FastAPI sends the transcript back to frontend.
11. Frontend displays the transcript.
12. User can copy the transcript.
```

---

## Week 1 Achievements

* [x] Initialized Git repository
* [x] Created GitHub repository
* [x] Created FastAPI backend
* [x] Created React frontend
* [x] Created audio upload API
* [x] Added file validation
* [x] Saved uploaded files locally
* [x] Connected frontend with backend
* [x] Created basic dashboard UI

---

## Week 2 Achievements

* [x] Installed Groq Python SDK
* [x] Added Groq API key environment variable
* [x] Added Groq Whisper large-v3 model configuration
* [x] Created cloud transcription service
* [x] Created `/api/transcribe-audio` endpoint
* [x] Sent raw audio file to Groq Whisper API
* [x] Received transcript from Groq
* [x] Displayed transcript on frontend
* [x] Added loading state during transcription
* [x] Added optional language selection
* [x] Added copy transcript button
* [x] Updated project documentation

---

## Current Limitations

* Audio preprocessing is not added yet.
* Speaker diarization is not added yet.
* Summary generation is not added yet.
* Key points extraction is not added yet.
* Action item detection is not added yet.
* Meeting history/database is not added yet.
* PDF export is not added yet.
* RAG-based meeting Q&A is not added yet.

---

## Upcoming Roadmap

## Week 3

Planned improvements:

* Add FFmpeg audio preprocessing.
* Convert raw audio into cleaner audio before transcription.
* Improve transcription quality.
* Add LLM integration.
* Generate short meeting summary.
* Generate detailed meeting summary.
* Extract key points.
* Extract action items.
* Detect important decisions.

---

## Week 4

Planned improvements:

* Add database integration.
* Store uploaded meetings.
* Store transcripts.
* Store summaries.
* Store action items.
* Create meeting history dashboard.

---

## Week 5

Planned improvements:

* Add speaker diarization.
* Generate speaker-wise transcript.
* Detect speaker-wise tasks.
* Improve meeting intelligence output.

---

## Week 6

Planned improvements:

* Add vector database.
* Create transcript embeddings.
* Build RAG-based meeting Q&A.
* Allow user to ask questions from meeting transcript.

---

## Week 7

Planned improvements:

* Add Urdu output.
* Add PDF report generation.
* Add export/download feature.
* Polish frontend UI.

---

## Week 8

Planned improvements:

* Dockerize project.
* Prepare deployment.
* Record demo video.
* Improve README.
* Add screenshots.
* Add project to portfolio and CV.

---

## Long-Term Vision

The long-term goal is to transform this project into a complete AI Meeting Assistant SaaS platform for:

* Software houses
* Startups
* Agencies
* Real estate companies
* Educational institutions
* Healthcare organizations
* Government departments

---

## Portfolio Value

This project demonstrates practical skills in:

* Full-stack development
* FastAPI backend development
* React frontend development
* Cloud AI API integration
* Speech-to-text AI
* Generative AI workflow design
* SaaS-style product architecture
* API-based AI product development

---

## Future Startup Potential

This project can later be converted into a SaaS product for teams and organizations that need automatic meeting documentation.

Possible future features:

* Team workspaces
* Real-time meeting transcription
* Speaker identification
* Calendar integration
* Email summary sending
* WhatsApp report sharing
* Organization-level meeting analytics
* Subscription-based pricing

---

## Author

Developed by Amir Ali.
---

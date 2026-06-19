# AI Meeting Intelligence System

An AI-powered meeting intelligence platform designed to transcribe meetings, generate summaries, extract key points, identify action items, and provide intelligent insights from meeting conversations.

This project is being developed as a portfolio-grade AI SaaS application with future startup potential.

---

## 🚀 Project Vision

Modern organizations conduct numerous meetings every day. Important decisions, action items, and follow-ups are often lost or forgotten.

The goal of this project is to build an AI-powered platform capable of:

* Transcribing meetings automatically.
* Generating concise summaries.
* Extracting key discussion points.
* Identifying action items.
* Assigning tasks to speakers.
* Supporting meeting Q&A through RAG.
* Providing Urdu and English outputs.

---

## 📌 Current Development Status

### ✅ Week 1 Completed

#### Features Implemented

* Project repository initialized.
* FastAPI backend setup.
* React frontend setup.
* Audio file upload functionality.
* File validation.
* Audio file storage.
* Frontend and backend integration.
* Basic UI dashboard.

---

## 🏗️ Week 1 Workflow

```text
User Uploads Audio File
            ↓
React Frontend
            ↓
FastAPI Backend API
            ↓
File Validation
            ↓
Audio File Saved Locally
            ↓
Success Response Returned
```

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* JavaScript
* CSS

### Backend

* FastAPI
* Python
* Uvicorn

### Future AI Stack

* Groq Whisper API
* Gemini API
* LangGraph
* Qdrant / ChromaDB
* PostgreSQL / Supabase
* RAG Architecture

---

## 📂 Project Structure

```text
ai-meeting-intelligence/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── README.md
├── .gitignore
└── docs/
```

---

## ⚙️ Installation

### Prerequisites

Make sure the following software is installed:

* Python 3.11+
* Node.js LTS
* Git
* VS Code (Recommended)

---

## 🔧 Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend server:

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🎨 Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start frontend server:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## 📡 API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "AI Meeting Intelligence API is running."
}
```

---

### Upload Audio

```http
POST /api/upload-audio
```

Supported Formats:

* MP3
* WAV
* M4A
* MP4
* OGG
* WEBM

Example Response:

```json
{
  "message": "File uploaded successfully.",
  "file": {
    "original_filename": "meeting.mp3",
    "saved_filename": "abc123.mp3",
    "file_path": "uploads/abc123.mp3",
    "file_size_mb": 2.5
  }
}
```

---

## 🔐 Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
UPLOAD_DIR=uploads
MAX_FILE_SIZE_MB=25

GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## ✅ Week 1 Achievements

* [x] Initialize Git repository
* [x] Create GitHub repository
* [x] Setup FastAPI backend
* [x] Setup React frontend
* [x] Create audio upload API
* [x] Validate uploaded files
* [x] Save uploaded files locally
* [x] Connect frontend with backend
* [x] Push code to GitHub

---

## 🗺️ Project Roadmap

### Week 2

* Integrate cloud-based transcription
* Connect Groq Whisper API
* Display transcription results

### Week 3

* Integrate Gemini/Groq LLM
* Generate meeting summaries
* Extract key points
* Detect action items

### Week 4

* Integrate PostgreSQL/Supabase
* Store meeting history
* Create meeting dashboard

### Week 5

* Speaker diarization
* Speaker-wise transcript generation

### Week 6

* Implement RAG
* Build Meeting Q&A system

### Week 7

* Urdu translation
* PDF report generation
* Export reports

### Week 8

* Dockerization
* Deployment
* Production optimization

---

## 🌟 Long-Term Vision

Transform this project into a complete AI Meeting Assistant SaaS platform for:

* Software Houses
* Startups
* Real Estate Companies
* Educational Institutions
* Healthcare Organizations
* Government Departments

---

## 👨‍💻 Author

**Amir Ali**

---

import { useState } from "react";
import "./App.css";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [language, setLanguage] = useState("");
  const [transcriptionResult, setTranscriptionResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setTranscriptionResult(null);
  };

  const handleTranscribe = async () => {
    if (!selectedFile) {
      alert("Please select an audio file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    if (language.trim()) {
      formData.append("language", language.trim());
    }

    try {
      setLoading(true);
      setTranscriptionResult(null);

      const response = await fetch("http://127.0.0.1:8000/api/transcribe-audio", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Transcription failed.");
      }

      setTranscriptionResult(data);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  const copyTranscript = async () => {
    if (!transcriptionResult?.transcription?.text) {
      return;
    }

    await navigator.clipboard.writeText(transcriptionResult.transcription.text);
    alert("Transcript copied to clipboard.");
  };

  return (
    <div className="page">
      <div className="card">
        <div className="badge">Week 2</div>

        <h1>AI Meeting Intelligence</h1>

        <p className="subtitle">
          Upload your meeting audio and generate a cloud-based transcript using
          Groq Whisper API.
        </p>

        <div className="upload-box">
          <label className="label">Select Audio / Video File</label>

          <input
            type="file"
            accept=".mp3,.wav,.m4a,.mp4,.ogg,.webm,.mpeg,.mpga,.flac"
            onChange={handleFileChange}
          />

          <label className="label">Language Code Optional</label>

          <select
            value={language}
            onChange={(event) => setLanguage(event.target.value)}
          >
            <option value="">Auto Detect Recommended</option>
            <option value="en">English</option>
            <option value="ur">Urdu</option>
            <option value="hi">Hindi</option>
          </select>

          <button onClick={handleTranscribe} disabled={loading}>
            {loading ? "Transcribing..." : "Transcribe Audio"}
          </button>
        </div>

        {selectedFile && (
          <div className="info">
            <strong>Selected File:</strong> {selectedFile.name}
          </div>
        )}

        {loading && (
          <div className="processing">
            <h3>Processing...</h3>
            <p>
              Your audio is being uploaded and transcribed in the cloud. Please
              wait until the transcript appears.
            </p>
          </div>
        )}

        {transcriptionResult && (
          <div className="result">
            <h2>Transcription Result</h2>

            <div className="meta">
              <p>
                <strong>Original File:</strong>{" "}
                {transcriptionResult.file.original_filename}
              </p>

              <p>
                <strong>Saved File:</strong>{" "}
                {transcriptionResult.file.saved_filename}
              </p>

              <p>
                <strong>File Size:</strong>{" "}
                {transcriptionResult.file.file_size_mb} MB
              </p>

              <p>
                <strong>Model:</strong>{" "}
                {transcriptionResult.transcription.model}
              </p>
            </div>

            <textarea
              value={transcriptionResult.transcription.text}
              readOnly
            />

            <button className="secondary-btn" onClick={copyTranscript}>
              Copy Transcript
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
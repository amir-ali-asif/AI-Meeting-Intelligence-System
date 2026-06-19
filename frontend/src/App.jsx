import { useState } from "react";
import "./App.css";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadResult, setUploadResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setUploadResult(null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select an audio file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:8000/api/upload-audio", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Upload failed.");
      }

      setUploadResult(data);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <div className="card">
        <h1>AI Meeting Intelligence</h1>
        <p>
          Upload your meeting audio. In the next phase, this system will
          transcribe, summarize, and extract action items.
        </p>

        <div className="upload-box">
          <input
            type="file"
            accept=".mp3,.wav,.m4a,.mp4,.ogg,.webm"
            onChange={handleFileChange}
          />

          <button onClick={handleUpload} disabled={loading}>
            {loading ? "Uploading..." : "Upload Audio"}
          </button>
        </div>

        {selectedFile && (
          <div className="info">
            <strong>Selected File:</strong> {selectedFile.name}
          </div>
        )}

        {uploadResult && (
          <div className="success">
            <h3>Upload Successful</h3>
            <p>{uploadResult.message}</p>
            <p>
              <strong>Saved As:</strong>{" "}
              {uploadResult.file.saved_filename}
            </p>
            <p>
              <strong>Size:</strong>{" "}
              {uploadResult.file.file_size_mb} MB
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
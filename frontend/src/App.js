import React, { useState } from "react";
import "./styles.css";

const App = () => {
  const [file, setFile] = useState(null);
  const [downloadUrl, setDownloadUrl] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && !selectedFile.name.endsWith('.csv')) {
      setError("Please upload a CSV file");
      setFile(null);
    } else {
      setError("");
      setFile(selectedFile);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please upload a CSV file");
      return;
    }

    setIsLoading(true);
    setError("");
    
    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch("/api/process", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        setDownloadUrl(url);
      } else {
        const errorData = await response.json();
        setError(errorData.error || "Error processing file");
      }
    } catch (err) {
      setError("Network error occurred. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>TickerTok</h1>
      <p className="subtitle">Rewinding stock prices, one tick at a time.</p>

      <div className="upload-section">
        <input
          type="file"
          accept=".csv"
          onChange={handleFileChange}
          className="file-input"
        />
        <button
          onClick={handleUpload}
          disabled={!file || isLoading}
          className="button"
        >
          {isLoading ? (
            <>
              Processing
              <span className="loading"></span>
            </>
          ) : (
            "Upload & Process"
          )}
        </button>

        {error && <p className="error">{error}</p>}

        {downloadUrl && (
          <div>
            <a
              href={downloadUrl}
              download="processed_prices.csv"
              className="download-link"
            >
              Download Processed CSV
            </a>
          </div>
        )}
      </div>

      <footer>
        vibecoded by wanazhar • powered by gpt4-o • 2025
      </footer>
    </div>
  );
};

export default App;
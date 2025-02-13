import React, { useState } from "react"; import "./styles.css";

const App = () => {
  const [file, setFile] = useState(null);
  const [downloadUrl, setDownloadUrl] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please upload a CSV file.");

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
      alert("Error processing file.");
    }
  };

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold text-center">TickerTok</h1>
      <p className="text-center">Rewinding stock prices, one tick at a time.</p>

      <div className="flex flex-col items-center mt-6">
        <input type="file" accept=".csv" onChange={handleFileChange} />
        <button
          onClick={handleUpload}
          className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
        >
          Upload & Process
        </button>

        {downloadUrl && (
          <a
            href={downloadUrl}
            download="processed_prices.csv"
            className="mt-4 text-blue-700 underline"
          >
            Download Processed CSV
          </a>
        )}
      </div>

      <footer className="text-center mt-10">
        vibecoded by wanazhar. powered by gpt4-o. 2025.
      </footer>
    </div>
  );
};

export default App;
import React, { useState } from "react";
import "./styles.css";
import { TradingViewWidget } from './components/TradingView'
import PortfolioAllocationPie from './components/PortfolioPie'
import RiskHeatmap from './components/RiskHeatmap'
import TechnicalIndicatorCard from './components/TechnicalIndicatorCard'
import MarketSentimentGauge from './components/MarketSentimentGauge'
import EarningsCalendar from './components/EarningsCalendar'
import NewsFeedWidget from './components/NewsFeedWidget'

const API_BASE_URL = '';

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

      console.log('Sending request to:', '/api/process');

      const response = await fetch('/api/process', {
        method: "POST",
        body: formData,
      });

      console.log('Response status:', response.status);

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
      }

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      setDownloadUrl(url);
    } catch (err) {
      console.error("Upload error:", err);
      setError("Failed to process file. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="dark:bg-gray-900 min-h-screen">
      <header className="bg-gradient-to-r from-blue-600 to-purple-600 p-6">
        <h1 className="text-3xl font-bold text-white">📈 TickerTok Analytics</h1>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6">
        <div className="lg:col-span-2 bg-white dark:bg-gray-800 rounded-xl p-6 shadow-xl">
          <TradingViewWidget />
        </div>
        
        <div className="space-y-6">
          <PortfolioAllocationPie />
          <RiskHeatmap />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-6">
        <TechnicalIndicatorCard />
        <MarketSentimentGauge />
        <EarningsCalendar />
        <NewsFeedWidget />
      </div>

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
    </div>
  );
};

export default App;
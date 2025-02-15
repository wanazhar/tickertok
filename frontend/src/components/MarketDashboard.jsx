// frontend/src/components/MarketDashboard.jsx
import React, { useEffect, useState } from 'react';
import { TradingViewWidget } from 'react-tradingview-widget';
import OrderBook from './OrderBook';
import NewsFeed from './NewsFeed';

export default function MarketDashboard() {
  const [selectedSymbol, setSelectedSymbol] = useState('AAPL');
  const [priceData, setPriceData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`/api/market/${selectedSymbol}`);
      const data = await response.json();
      setPriceData(data);
    };
    fetchData();
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, [selectedSymbol]);

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 p-6">
      <div className="col-span-2 bg-white rounded-lg shadow-lg p-4">
        <TradingViewWidget
          symbol={`NASDAQ:${selectedSymbol}`}
          theme="Light"
          locale="en"
          autosize
          toolbar_bg="#f4f6f8"
          details
          hotlist
        />
        {priceData && (
          <div className="mt-4 p-4 bg-gray-50 rounded">
            <h2 className="text-2xl font-bold">
              {selectedSymbol}: ${priceData.price?.toFixed(2)}
            </h2>
          </div>
        )}
      </div>
      
      <div className="space-y-6">
        <OrderBook symbol={selectedSymbol} />
        <NewsFeed />
      </div>
    </div>
  );
}
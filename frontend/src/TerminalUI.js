// frontend/src/TerminalUI.js
import { BloombergKeyboard } from 'react-bloomberg-keyboard';
import { NewsMosaic } from 'financial-news-widget';
import { AdvancedCharting } from '@tradingview/charts';

export default function TerminalInterface() {
  return (
    <div className="terminal-grid bg-gray-900 text-green-400">
      <BloombergKeyboard />
      <AdvancedCharting 
        theme="dark" 
        studies={["MACD", "RSI", "Volume"]}
      />
      <OrderBookL3 depth={50} />
      <NewsMosaic sources={['Bloomberg', 'Reuters', 'WSJ']} />
      <TradingBlotter />
      <RiskDashboard />
      <ChatInterface contacts={['Sales', 'Trading', 'Research']} />
    </div>
  )
}
# 📈 TickerTok

> Rewinding stock prices, one tick at a time.

TickerTok is a sleek web application that processes CSV files containing stock tickers and returns their latest prices using Yahoo Finance data.

## ✨ Features

- 📤 Simple CSV file upload
- 📊 Real-time stock price fetching
- 📥 Instant CSV download with results
- 🎯 Error handling and validation
- 💫 Modern, responsive UI

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/wanazhar/tickertok.git
   cd tickertok
   ```

2. Install dependencies:
   ```bash
   # Frontend
   cd frontend
   npm install

   # Backend
   cd ../
   pip install -r requirements.txt
   ```

3. Start the development servers:
   ```bash
   # Frontend (in frontend directory)
   npm start

   # Backend (in root directory)
   uvicorn api.process:app --reload
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

## 📋 CSV Format

Your input CSV file should have a column named "Ticker". Example:
| Ticker |
|--------|
| AAPL   |
| GOOGL  |
| MSFT   |

## 🛠️ Tech Stack

- **Frontend**: React.js, Material-UI
- **Backend**: FastAPI (Python)
- **Data Source**: Yahoo Finance API

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🌐 API Endpoints

- `POST /api/process`
  - Accepts: CSV file upload
  - Returns: Processed CSV with latest stock prices

## 🚀 Deployment

This project is configured for easy deployment on Vercel:

1. Fork this repository
2. Create a new project on [Vercel](https://vercel.com)
3. Connect your forked repository
4. Deploy!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Yahoo Finance API](https://finance.yahoo.com/) for providing stock data
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing backend framework
- [Material-UI](https://material-ui.com/) for the beautiful UI components

## 📞 Support

If you have any questions or need help, please open an issue in the repository.

---

<p align="center">Made with ❤️ by <a href="https://github.com/yourusername">wanazhar</a></p>

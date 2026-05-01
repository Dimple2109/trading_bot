# 📈 Binance Futures Trading Bot (Testnet)

A modular Python-based command-line trading system that executes Market and Limit orders on Binance Futures Testnet (USDT-M).  
The project focuses on API integration, clean architecture, validation, logging, and real-world trading simulation.

---

## 🎯 Overview

This bot allows users to interact with Binance Futures Testnet through a simple CLI interface.  
It supports order placement, input validation, and structured logging for debugging and tracking trades.

---

## ⚡ Key Capabilities

✔ Market order execution (BUY / SELL)  
✔ Limit order execution (BUY / SELL)  
✔ Binance Futures Testnet integration  
✔ CLI-based interaction using argparse  
✔ Strong input validation system  
✔ Modular and maintainable codebase  
✔ Logging of API calls and responses  
✔ Error handling for API and runtime issues  

---

## 🧩 System Architecture

The project follows a layered structure:

CLI Layer → Validation Layer → Order Processing → API Layer → Binance Testnet

---

## 📁 Project Layout

```

trading_bot/
│
├── bot/
│   ├── client.py          → Binance API handler
│   ├── orders.py          → Order execution logic
│   ├── validators.py      → Input validation rules
│   ├── logging_config.py  → Logging configuration
│
├── logs/
│   └── app.log            → Runtime logs
│
├── cli.py                 → Application entry point
├── requirements.txt       → Dependencies
└── README.md              → Documentation

````id="structure2"

---

## ⚙️ Installation Guide

### Step 1: Clone the repository
```bash
git clone <repo-url>
cd trading_bot
````

---

### Step 2: Install dependencies

```bash id="install2"
pip install -r requirements.txt
```

---

### Step 3: Configure API credentials

Create a `.env` file in the root directory:

```env id="env1"
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

### Step 4: Setup Binance Testnet

* Visit: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
* Login and generate API keys
* Ensure testnet wallet has sufficient balance

---

## ▶️ Execution Guide

### 🟢 Place Market Order

```bash id="run3"
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

---

### 🔴 Place Limit Order

```bash id="run4"
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000
```

---

## 📊 Example Output

```
📊 Order Summary
symbol: BTCUSDT
side: BUY
type: MARKET
quantity: 0.01

🔄 Sending request to Binance Testnet...

✅ ORDER EXECUTED
Order ID      : 123456789
Status        : NEW
Executed Qty  : 0.0000
Average Price : 0.00
```

---

## 🧾 Logging System

All runtime activity is stored in:

```
logs/app.log
```

### Logged Information:

* API request payloads
* API responses
* Errors and exceptions
* Execution flow details

---

## ⚠️ Important Notes

* Limit orders remain in **NEW** state until market conditions are met
* Market orders execute instantly based on available liquidity
* Execution quantity may appear as `0.0000` in testnet (expected behavior)
* Binance Futures Testnet does not simulate real profit/loss accurately

---

## 🧠 System Assumptions

* Valid Binance Testnet API credentials are provided
* User has sufficient testnet balance
* Network connectivity is stable (VPN may be required in some regions)

---

## 🚀 Possible Enhancements

* Stop-Limit / OCO order support
* Real-time price feed integration
* Interactive menu-based CLI
* Dashboard UI (Streamlit / React)
* Trade history tracking system

---

## 👨‍💻 Developer

Dimple Vasita

Artificial Intelligence & Data Science Student | Python Developer

---

## 🏁 Project Summary

This project demonstrates practical knowledge of:

* REST API integration
* Financial system simulation
* CLI application development
* Modular software design
* Error handling and logging
* Real-world trading workflow

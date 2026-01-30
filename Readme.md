# Live Stock Market Dashboard - Apple Inc. (AAPL)

A Python-powered real-time analytics pipeline integrated with Microsoft Excel to deliver professional-grade trading insights.

## Project Overview
This project features a live-updating stock market analytics dashboard that tracks *Apple Inc. (AAPL)*. It utilizes a robust Python-driven data pipeline to handle real-time ingestion and processing, while Microsoft Excel serves as the visual analytics layer. The result is a trading-terminal-style interface with live KPIs, intraday trends, volume analysis, and candlestick patterns.

### Key Highlights
* [cite_start]*Market-Aware Automation:* The system automatically triggers data collection at market open (09:30 AM ET) and stops at market close (04:00 PM ET)[cite: 6, 49].
* [cite_start]*Production-Grade Logic:* Prevents API wastage and after-hours data contamination by adhering to official NYSE/NASDAQ hours[cite: 54, 55].
* [cite_start]*Hybrid Architecture:* Combines Python’s computational power with Excel’s flexible visualization capabilities[cite: 88].

---

## Dashboard Preview
![AAPL Stock Dashboard](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/image_224dd9.jpg)
Figure 1: Real-time visual interface featuring KPI panels, intraday price action, and technical charts.

---

## Tech Stack & Resources

### Backend (Data Pipeline)
* [cite_start]**[Python](https://www.python.org/):** The core programming language used for automation and logic[cite: 18].
* [cite_start]**[pandas](https://pandas.pydata.org/):** Used for cleaning, structuring, and calculating rolling extrema[cite: 19, 38].
* [cite_start]**[yfinance](https://pypi.org/project/yfinance/):** The primary API wrapper to fetch live intraday and daily market data[cite: 20, 37].
* [cite_start]**[pytz](https://pythonhosted.org/pytz/):** Handles time-zone conversions to ensure synchronization with Eastern Time (ET)[cite: 21, 51].

### Frontend (Visualization)
* [cite_start]**[Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel):** Serves as the dashboard UI using dynamic formulas and advanced charting[cite: 24, 26].

---

## Dataset Explanation
The system captures and processes a multi-dimensional dataset for AAPL, including:
* [cite_start]*Core Market Data:* Timestamp, Open, High, Low, Close (OHLC), and Volume[cite: 29, 31, 35].
* [cite_start]*Calculated Metrics:* * *Previous Close:* The final price from the prior trading session, used as a performance benchmark[cite: 81].
    * [cite_start]*Percentage Change:* Calculated as $((Current Price - Previous Close) / Previous Close)$[cite: 83].
    * [cite_start]*Intraday Extrema:* Rolling daily High and Low values[cite: 84].

---

## System Architecture
1.  [cite_start]*Ingestion:* Python script fetches raw data via the yfinance API[cite: 8, 10].
2.  [cite_start]*Processing:* Data is cleaned and technical KPIs are calculated in real-time[cite: 38, 39].
3.  [cite_start]*Storage:* Processed data is exported to Excel-readable formats (CSV/XLSX)[cite: 43].
4.  [cite_start]*Visualization:* Excel dynamically pulls these files to refresh charts and KPI panels every fixed interval[cite: 44, 68].

---

## Feature Deep Dive
* [cite_start]*KPI Summary Panel:* Displays Current Price, % Change, Day High/Low, and the "Last Refreshed" timestamp[cite: 59, 67].
* [cite_start]*Live Intraday Chart:* A real-time line chart featuring a dashed reference line for the Previous Close to assess daily performance[cite: 69, 71].
* [cite_start]*Volume Analysis:* An overlay of price lines and volume bars to identify high-activity volatility zones[cite: 73, 75].
* [cite_start]*Daily Candlestick Chart:* Supports technical analysis by visualizing bullish and bearish session indicators[cite: 76, 78].

---

## Future Enhancements
* [cite_start]Implementation of Moving Averages ($20, 50, 200$ days)[cite: 90].
* [cite_start]Multi-ticker support and database integration (SQLite/PostgreSQL)[cite: 91].
* [cite_start]WebSocket-based live streaming for sub-second updates[cite: 91].

---

*Author:* [DivanshieSumitSetia]  
*License:* MIT
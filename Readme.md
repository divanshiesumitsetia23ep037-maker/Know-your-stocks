# Live Stock Market Dashboard - Apple Inc. (AAPL)

This project is an advanced Python-driven data pipeline integrated with Microsoft Excel to deliver a professional, trading-terminal-style dashboard for Apple Inc. (AAPL). It effectively bridges the gap between powerful data processing capabilities and intuitive, accessible visual analytics.

## Project Overview
This project features a live-updating stock market analytics dashboard that tracks *Apple Inc. (AAPL)*. It utilizes a robust Python-driven data pipeline to handle real-time ingestion and processing, while Microsoft Excel serves as the visual analytics layer. The result is a trading-terminal-style interface with live KPIs, intraday trends, volume analysis, and candlestick patterns. The system architecture is designed for scalability and reliability.

### Key Highlights
* *Market-Aware Automation:* The script is “market-aware,” continuously tracking the current Eastern Time (ET). It automatically begins data collection at the market open (09:30 AM ET) and shuts down at the closing bell (04:00 PM ET).[cite: 6, 49].
* *Production-Grade Logic:* By limiting execution strictly to official market hours, the pipeline avoids after-hours data contamination and eliminates unnecessary API calls.[cite: 54, 55].
* *Hybrid Architecture:* Python performs the heavy lifting—retrieving raw data via APIs, cleaning and structuring it, and computing key performance indicators (KPIs) such as percentage change and rolling intraday highs and lows.[cite: 88].

---

## Dashboard Preview
![AAPL Stock Dashboard]("C:\Users\Divanshie\Downloads\github readmes\dashboard.jpg")
Figure 1: Real-time visual interface featuring KPI panels, intraday price action, and technical charts.

---

## Tech Stack & Resources

### Backend (Data Pipeline)
* **[Python](https://www.python.org/):** The core programming language used for automation and logic.
* **[pandas](https://pandas.pydata.org/):** Used for cleaning, structuring, and calculating rolling extrema.
* **[yfinance](https://pypi.org/project/yfinance/):** The primary API wrapper to fetch live intraday and daily market data.
* **[pytz](https://pythonhosted.org/pytz/):** Handles time-zone conversions to ensure synchronization with Eastern Time (ET).

### Frontend (Visualization)
* **[Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel):** Serves as the dashboard UI using dynamic formulas and advanced charting.

---

## Dataset Explanation
The system captures and processes a multi-dimensional dataset for AAPL, including:
* *Core Market Data:* Timestamp, Open, High, Low, Close (OHLC), and Volume.
* *Calculated Metrics:* * *Previous Close:* The final price from the prior trading session, used as a performance benchmark.
    * *Percentage Change:* Calculated as $((Current Price - Previous Close) / Previous Close)$.
    * *Intraday Extrema:* Rolling daily High and Low values.
* *Historical Breadth:* The pipeline fetches the last 1 month of daily data to populate the candlestick series.

---

## System Architecture
1.  *Ingestion:* Python script fetches raw data via the yfinance API.
2.  *Processing:* Data is cleaned, and technical KPIs are calculated in real-time.
3.  *Storage:* Processed data is exported to Excel-readable formats (CSV/XLSX).
4.  *Visualization:* Excel dynamically pulls these files to refresh charts and KPI panels every fixed interval.

---

## Feature Deep Dive
* *KPI Summary Panel:* Displays Current Price, % Change, Day High/Low, and the "Last Refreshed" timestamp. All KPIs are dynamically linked to Python-generated datasets.
* *Live Intraday Chart:* A real-time line chart featuring a dashed reference line for the Previous Close to quickly assess daily performance.
* *Volume Analysis:* An overlay of price lines and volume bars to identify high-activity volatility zones.
* *Monthly Candlestick Chart:* Provides a high-level technical visualization of AAPL’s performance over the last 30 days. It uses bullish and bearish color-coding to highlight price direction and session strength.
* *Technical Context:* Helps traders compare the current live price action against the broader trend of the previous month.

---

## Insights & Observations
* *Previous Close Benchmark:* The previous close acts as a critical intraday benchmark and the "psychological equator" for the trading day. Plotting a dashed reference line allows for an instant assessment of AAPL's performance relative to the prior session.
* *Volume-Price Correlation:* Significant volume spikes often coincide with rapid price movements and high-activity zones. Overlaying price lines with volume bars highlights the intensity of market conviction during volatility.
* *Multi-Timeframe Clarity:* Combining real-time intraday data with daily charts significantly improves overall signal clarity. The 1-month daily candlestick chart provides the necessary technical context to identify bullish or bearish session indicators.
* *Technical Synergy:* The integration of Python and Excel enables professional real-time analytics without the need for expensive BI tools. Separating data ingestion (Python) from visualization (Excel) improves system scalability and mimics real-world trading infrastructure.

---

## Primary Use Cases
This dashboard is designed for a variety of professional and educational scenarios:
* *Financial Market Monitoring:* Keeping a real-time eye on specific ticker movements without needing expensive, specialized trading software.
* *Trading Analytics:* Evaluating intraday volatility and volume spikes to identify potential entry or exit points.
* *Data Engineering Portfolios:* Serving as a "production-grade" demonstration of automation, API integration, and ETL (Extract, Transform, Load) processes.
* *Interview Demonstrations:* Showcasing the ability to integrate disparate tools (Python and Excel) to solve real-world financial data challenges.
* *Corporate Automation:* Providing a template for how Python can enhance legacy Excel reporting with real-time capabilities.

---

*Author:* [DivanshieSumitSetia]  

*License:* MIT

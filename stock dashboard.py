import yfinance as yf
import pandas as pd
import time
from datetime import datetime, time as dtime
from zoneinfo import ZoneInfo
import os

TICKER = "AAPL"

# CSV files
INTRADAY_CSV = r"C:\Users\Divanshie\Stock Data\realtime_stock_data.csv"
MONTHLY_CSV = r"C:\Users\Divanshie\Stock Data\AAPL_1month_data.csv"

# Fetch interval for intraday data (seconds)
FETCH_INTERVAL = 60  

# Market times in NY timezone
MARKET_TZ = ZoneInfo("America/New_York")
MARKET_OPEN = dtime(9, 30)
MARKET_CLOSE = dtime(16, 0)

def is_market_open():
    now = datetime.now(MARKET_TZ).time()
    return MARKET_OPEN <= now <= MARKET_CLOSE


def wait_for_market_open():
    print("Waiting for market to open...")
    while not is_market_open():
        time.sleep(30)
    print("Market opened!")


def append_to_csv(df, filename):
    """Append a DataFrame to CSV, creating file if it doesn't exist."""
    df = df.reset_index(drop=True)
    df["FETCHED_AT"] = datetime.now(MARKET_TZ).strftime('%Y-%m-%d %H:%M:%S')

    file_exists = os.path.isfile(filename)
    df.to_csv(
        filename,
        mode="a",
        header=not file_exists,
        index=False
    )


def fetch_today_ohlc(ticker):
    """Fetch aggregated OHLC for today (1-min interval)."""
    data = yf.download(
        tickers=ticker,
        period="1d",
        interval="1m",
        progress=False
    )

    if data.empty:
        return None

    return pd.DataFrame([{
        "OPEN": float(data["Open"].iloc[0]),
        "HIGH": float(data["High"].max()),
        "LOW": float(data["Low"].min()),
        "CLOSE": float(data["Close"].iloc[-1]),
        "VOLUME": int(data["Volume"].sum())
    }])


def fetch_one_month_history(ticker, csv_file=MONTHLY_CSV):
    """Fetch 1 month historical data and save to CSV."""
    print("Fetching 1-month historical data...")
    ticker_obj = yf.Ticker(ticker)
    monthly_data = ticker_obj.history(period="1mo")

    if monthly_data.empty:
        print("No historical data fetched.")
        return

    # Add timestamp for reference
    monthly_data["FETCHED_AT"] = datetime.now(MARKET_TZ).strftime('%Y-%m-%d %H:%M:%S')

    # Save to CSV
    monthly_data.to_csv(csv_file, index=True)
    print(f"1-month historical data saved to {csv_file}")


if __name__ == "__main__":
    # 1️⃣ Fetch 1-month historical data once at start
    fetch_one_month_history(TICKER)

    # 2️⃣ Wait for market open
    wait_for_market_open()

    # 3️⃣ Start intraday collection loop
    while True:
        if not is_market_open():
            print("Market closed. Stopping script.")
            break

        try:
            latest = fetch_today_ohlc(TICKER)

            if latest is not None:
                # Append to intraday CSV
                append_to_csv(latest, INTRADAY_CSV)
                print(f"Added OHLC at {datetime.now(MARKET_TZ)}")

        except Exception as e:
            print("Error:", e)

        time.sleep(FETCH_INTERVAL)

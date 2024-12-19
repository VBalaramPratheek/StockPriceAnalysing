import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch stock data from Yahoo Finance
def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock price data for a given ticker.
    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL' for Apple).
        start_date (str): Start date in the format 'YYYY-MM-DD'.
        end_date (str): End date in the format 'YYYY-MM-DD'.
    Returns:
        pd.DataFrame: Historical stock data.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Example usage
ticker_symbol = 'AAPL'  # Replace with any stock ticker
start_date = '2023-01-01'
end_date = '2024-01-01'

# Fetch data
stock_prices = fetch_stock_data(ticker_symbol, start_date, end_date)

# Display the first few rows of the stock prices
print("Stock Price Data:")
print(stock_prices.head())

# Plot the stock closing prices
plt.figure(figsize=(10, 6))
plt.plot(stock_prices['Close'], label=f'{ticker_symbol} Closing Prices')
plt.title(f'{ticker_symbol} Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

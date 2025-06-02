# import yfinance as yf
# import time

# def fetch_real_time_stock(symbol):
#     try:
#         stock = yf.Ticker(symbol)
#         stock_info = stock.history(period='1d', interval='1m')

#         if stock_info.empty:
#             print(f"No data found for {symbol}. The stock may be delisted or invalid.")
#             return None

#         current_price = stock_info['Close'].iloc[-1]
#         return round(current_price, 2)

#     except Exception as e:
#         print(f"Error fetching data for {symbol}: {e}")
#         return None

# def generate_stock_data():
#     symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NFLX",
#     "TCS.NS", "INFY.NS", "WIPRO.NS", "HCLTECH.NS", "TECHM.NS",
#     "HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "KOTAKBANK.NS", "AXISBANK.NS",
#     "RELIANCE.NS", "IOC.NS", "ONGC.NS", "NTPC.NS", "POWERGRID.NS",
#     "HINDUNILVR.NS", "ITC.NS", "NESTLEIND.NS", "BRITANNIA.NS", "DABUR.NS",
#     "TATAMOTORS.NS", "MARUTI.NS", "M&M.NS", "HEROMOTOCO.NS", "BAJAJ-AUTO.NS",
#     "SUNPHARMA.NS", "CIPLA.NS", "DRREDDY.NS", "AUROPHARMA.NS", "LUPIN.NS"
# ]
#     while True:
#         for symbol in symbols:
#             performance = fetch_real_time_stock(symbol)
#             if performance is not None:
#                 yield (symbol, performance)
#         time.sleep(0.1)  # Fetch data every minute


# # Search for stock using company


# # import yfinance as yf
# # import time

# # def fetch_real_time_stock(symbol):
# #     """
# #     Fetch the latest stock price from Yahoo Finance using the yfinance library.
# #     Returns the current stock price or None if the stock data is unavailable.
# #     """
# #     try:
# #         stock = yf.Ticker(symbol)
# #         stock_info = stock.history(period='1d', interval='1m')

# #         # Check if stock_info is empty (no data found)
# #         if stock_info.empty:
# #             print(f"No data found for {symbol}. The stock may be delisted or invalid.")
# #             return None

# #         # Get the latest closing price using iloc for positional access
# #         current_price = stock_info['Close'].iloc[-1]
# #         return round(current_price, 2)

# #     except Exception as e:
# #         print(f"Error fetching data for {symbol}: {e}")
# #         return None

# # def generate_stock_data():
# #     """
# #     Generate real-time stock data by fetching the stock prices of multiple symbols.
# #     The function yields stock symbols and their respective performances.
# #     """
# #     symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "NVIDIA Corp", "META", "NFLX"]
# #     while True:
# #         for symbol in symbols:
# #             performance = fetch_real_time_stock(symbol)
# #             if performance is not None:
# #                 yield (symbol, performance)
# #         time.sleep(10)  # Fetch data every minute

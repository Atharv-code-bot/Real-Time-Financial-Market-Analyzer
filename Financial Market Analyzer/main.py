import time
import threading
import yfinance as yf
from flask import Flask, jsonify, render_template
from analyzer import RealTimeFinancialMarketAnalyzer, Stock

app = Flask(__name__)


analyzer = RealTimeFinancialMarketAnalyzer(top_n=50)

def fetch_real_time_stock(symbol, retries=3):
    for _ in range(retries):
        try:
            stock = yf.Ticker(symbol)
            stock_info = stock.history(period='1d', interval='1m')

            if stock_info.empty:
                print(f"No data found for {symbol}. The stock may be delisted or invalid.")
                return None

            current_price = stock_info['Close'].iloc[-1]
            return round(current_price, 2)

        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            time.sleep(2) 
    return None

def generate_stock_data():
    symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NFLX","IRFC.NS","BHEL.NS",
    "TCS.NS", "INFY.NS", "WIPRO.NS", "HCLTECH.NS", "TECHM.NS",
    "HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "KOTAKBANK.NS", "AXISBANK.NS",
    "RELIANCE.NS", "IOC.NS", "ONGC.NS", "NTPC.NS", "POWERGRID.NS",
    "HINDUNILVR.NS", "ITC.NS", "NESTLEIND.NS", "BRITANNIA.NS", "DABUR.NS",
    "TATAMOTORS.NS", "MARUTI.NS", "M&M.NS", "HEROMOTOCO.NS", "BAJAJ-AUTO.NS",
    "SUNPHARMA.NS", "CIPLA.NS", "DRREDDY.NS", "AUROPHARMA.NS", "LUPIN.NS",
    "ADANIGREEN.NS", "ADANIPORTS.NS", "ADANIPOWER.NS", "GRASIM.NS", "ULTRACEMCO.NS",
    "BHEL.NS", "TATASTEEL.NS", "JSWSTEEL.NS", "SAIL.NS", "JINDALSTEL.NS",
    "HINDALCO.NS", "ASHOKLEY.NS", "BOSCHLTD.NS", "MOTHERSUMI.NS", "EICHERMOT.NS",
    "BHARTIARTL.NS", "RELIANCE.NS", "VODAFONEIDEA.NS", "ITC.NS", "PIDILITE.NS",
    "ZEEENT.NS", "SUNTV.NS", "NETWORK18.NS", "BALRAMCHIN.NS", "INDIGO.NS",
    "INFRATEL.NS", "CONCOR.NS", "DELHIVERY.NS", "GAIL.NS", "INDIANBUNK.NS"]

    while True:
        for symbol in symbols:
            performance = fetch_real_time_stock(symbol)
            if performance is not None:
                yield (symbol, performance)
        time.sleep(10)

def update_stock_data():
    while True:
        try:
            for symbol, performance in generate_stock_data():
                stock = Stock(symbol, performance)
                analyzer.add_or_update_stock(stock)
        except Exception as e:
            print(f"Error in background thread: {e}")
            time.sleep(5)


threading.Thread(target=update_stock_data, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/top-stocks/<int:limit>')
def top_stocks(limit):
    top_stocks = analyzer.get_top_stocks()[:limit]
    return jsonify([{'symbol': stock.symbol, 'performance': stock.performance} for stock in top_stocks])

@app.route('/smallest-stocks/<int:limit>')
def smallest_stocks(limit):
    smallest_stocks = analyzer.get_smallest_stocks()[:limit]
    return jsonify([{'symbol': stock.symbol, 'performance': stock.performance} for stock in smallest_stocks])


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server encountered an error'}), 500

if __name__ == '__main__':
    app.run(debug=True)

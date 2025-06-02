import heapq

class Stock:
    def __init__(self, symbol, performance):
        self.symbol = symbol
        self.performance = performance

    def __lt__(self, other):
        return self.performance < other.performance

import heapq

class RealTimeFinancialMarketAnalyzer:
    def __init__(self, top_n):
        self.top_n = top_n
        self.stock_dict = {} 
    def add_or_update_stock(self, stock):
        self.stock_dict[stock.symbol] = stock.performance

    def get_top_stocks(self):
        n = min(len(self.stock_dict), self.top_n)
        print(f"Fetching top {n} stocks out of {len(self.stock_dict)} available stocks.")

    
        top_stocks = heapq.nlargest(n, self.stock_dict.items(), key=lambda x: x[1])
    
        return [Stock(symbol, performance) for symbol, performance in top_stocks]


    def get_smallest_stocks(self):

        smallest_stocks = heapq.nsmallest(self.top_n, self.stock_dict.items(), key=lambda x: x[1])
        return [Stock(symbol, performance) for symbol, performance in smallest_stocks]
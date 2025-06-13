
import requests
import json
import time
from datetime import datetime, timedelta

class AlpacaTrader:
    def __init__(self, api_key, secret_key, is_paper=True):
        self.api_key = api_key
        self.secret_key = secret_key
        self.is_paper = is_paper
        
        # Paper vs Live endpoints
        if is_paper:
            self.base_url = "https://paper-api.alpaca.markets"
            self.data_url = "https://data.alpaca.markets"
        else:
            self.base_url = "https://api.alpaca.markets"
            self.data_url = "https://data.alpaca.markets"
            
        self.headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key,
            "Content-Type": "application/json"
        }
    
    def get_account_info(self):
        """Get account information"""
        url = f"{self.base_url}/v2/account"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_current_price(self, symbol):
        """Get current price for a symbol"""
        url = f"{self.data_url}/v2/stocks/{symbol}/trades/latest"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_bars(self, symbol, timeframe="1Day", limit=100):
        """Get historical bar data"""
        end_time = datetime.now()
        start_time = end_time - timedelta(days=limit)
        
        url = f"{self.data_url}/v2/stocks/{symbol}/bars"
        params = {
            "start": start_time.isoformat(),
            "end": end_time.isoformat(),
            "timeframe": timeframe,
            "limit": limit
        }
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def place_market_order(self, symbol, qty, side, stop_loss=None, take_profit=None):
        """Place a market order"""
        url = f"{self.base_url}/v2/orders"
        
        order_data = {
            "symbol": symbol,
            "qty": str(qty),
            "side": side,  # "buy" or "sell"
            "type": "market",
            "time_in_force": "day"
        }
        
        # Add stop loss and take profit as bracket order
        if stop_loss or take_profit:
            order_data["order_class"] = "bracket"
            if stop_loss:
                order_data["stop_loss"] = {"stop_price": str(stop_loss)}
            if take_profit:
                order_data["take_profit"] = {"limit_price": str(take_profit)}
        
        response = requests.post(url, headers=self.headers, json=order_data)
        return response.json()
    
    def get_positions(self):
        """Get all open positions"""
        url = f"{self.base_url}/v2/positions"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def close_position(self, symbol, qty=None):
        """Close a position"""
        url = f"{self.base_url}/v2/positions/{symbol}"
        data = {}
        if qty:
            data["qty"] = str(qty)
        response = requests.delete(url, headers=self.headers, json=data)
        return response.json()
    
    def get_orders(self, status="open"):
        """Get orders"""
        url = f"{self.base_url}/v2/orders"
        params = {"status": status}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

def simple_moving_average(prices, period):
    """Calculate simple moving average"""
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period

def rsi(prices, period=14):
    """Calculate RSI"""
    if len(prices) < period + 1:
        return None
    
    gains = []
    losses = []
    
    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(-change)
    
    if len(gains) < period:
        return None
        
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    
    if avg_loss == 0:
        return 100
    
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
    print(f"RSI: {rsi}, SMA 20: {sma_20}, SMA 50: {sma_50}")
print("Buy conditions met")  # Right before placing buy
print("Sell conditions met")  # Right before placing sell


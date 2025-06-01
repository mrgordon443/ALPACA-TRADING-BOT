import requests
import json
import os

# Load Alpaca keys (for Replit, you can set these as Environment Variables)
API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY
}

def get_account():
    url = f"{BASE_URL}/v2/account"
    r = requests.get(url, headers=HEADERS)
    return r.json()

def place_order(symbol, qty, side, type="market", time_in_force="gtc"):
    url = f"{BASE_URL}/v2/orders"
    order_data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(url, headers=HEADERS, json=order_data)
    return r.json()

# Test the functions
account = get_account()
print("Account:", account)

order = place_order("AAPL", 1, "buy")
print("Order Response:", order)

import os
import alpaca_trade_api as tradeapi

# Load API keys from environment
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

# Initialize API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Check account
account = api.get_account()
print("Account status:", account.status)

# Example: Get last price of AAPL
barset = api.get_barset('AAPL', 'minute', limit=1)
aapl_price = barset['AAPL'][0].c
print(f"AAPL last price: ${aapl_price}")

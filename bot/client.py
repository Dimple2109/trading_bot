from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        # ✅ Proper Testnet mode
        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

    def place_order(self, **params):
        try:
            return self.client.futures_create_order(**params)
        except Exception as e:
            print("API Error:", str(e))
            return None

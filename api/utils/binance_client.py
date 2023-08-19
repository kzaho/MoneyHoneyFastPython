import os
from binance.client import Client


def init_binance_client() -> Client:
    """Initialize and return a Binance client."""
    api_key = os.environ.get("BINANCE_API_KEY")
    api_secret = os.environ.get("BINANCE_API_SECRET")
    client = Client(api_key, api_secret)
    return client

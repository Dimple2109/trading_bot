import argparse
from bot.client import BinanceClient
from bot.orders import create_order
from bot.logging_config import setup_logger

API_KEY = "jp4jH9d3OrGqQnSUo1YqKwWSGkW2cVg1lfGWpAfU1aIGgD88aoFdj6ira87md5ba"
API_SECRET = "Pe4TYKB7GBtTMuWX1AXfXZUJzF605ZiqOUPbBJeXP35PwGGvPoKgKu3RAg9hJdss"

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    client = BinanceClient(API_KEY, API_SECRET)

    create_order(
        client,
        logger,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

if __name__ == "__main__":
    main()
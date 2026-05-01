import argparse
from bot.client import BinanceClient
from bot.orders import create_order
from bot.logging_config import setup_logger

API_KEY = "jp4jH9d3OrGqQnSUo1YqKwWSGkW2cVg1lfGWpAfU1aIGgD88aoFdj6ira87md5ba"
API_SECRET = "Pe4TYKB7GBtTMuWX1AXfXZUJzF605ZiqOUPbBJeXP35PwGGvPoKgKu3RAg9hJdss"

def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    print("\n" + "="*55)
    print("🚀 BINANCE FUTURES TRADING BOT")
    print("="*55)

    print("\n📊 ORDER DETAILS")
    print(f"Symbol     : {args.symbol}")
    print(f"Side       : {args.side}")
    print(f"Type       : {args.type}")
    print(f"Quantity   : {args.quantity}")
    print(f"Price      : {args.price if args.price else 'N/A'}")

    print("\n⏳ Connecting to Binance Testnet...")

    client = BinanceClient(API_KEY, API_SECRET)

    order = create_order(
        client,
        logger,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n" + "-"*55)

    if order:
        print("✅ ORDER EXECUTED SUCCESSFULLY")
        print(f"🆔 Order ID     : {order.get('orderId')}")
        print(f"📌 Status       : {order.get('status')}")
        print(f"📦 Executed Qty : {order.get('executedQty')}")
        print(f"💰 Avg Price    : {order.get('avgPrice')}")
    else:
        print("❌ ORDER FAILED")
        print("Reason: Check logs or API response")

    print("-"*55)
    print("📄 Log File: bot.log")
    print("="*55)

if __name__ == "__main__":
    main()

from bot.validators import validate_input

def create_order(client, logger, symbol, side, order_type, quantity, price=None):
    try:
        validate_input(symbol, side, order_type, quantity, price)

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {params}")

        response = client.place_order(**params)

        logger.info(f"Order response: {response}")

        print("\n✅ ORDER SUCCESS")
        print(response)

        return response

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        print("❌ ORDER FAILED:", str(e))
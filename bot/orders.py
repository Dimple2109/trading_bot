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
            params["price"] = str(price)
            params["timeInForce"] = "GTC"

        logger.info(f"Placing order: {params}")

        response = client.place_order(**params)

        if not response:
            raise Exception("Order failed - empty response")

        logger.info(f"Order response: {response}")

        print("\n✅ ORDER SUCCESS")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))
        print("\nRaw Response:", response)

        return response

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")

        print("\n❌ ORDER FAILED")
        print("Reason:", str(e))

        return None

from email_notification import send_email


def send_notification(product_name, price, availability, target_price):
    if availability == "AVAILABLE" and price <= target_price:
        print("\n🔔 NOTIFICATION")
        print("========================================")
        print(f"Product: {product_name}")
        print(f"Current Price: ₹{price:,.2f}")
        print("🎉 Target price reached!")
        print("The product is available at or below your target price.")
        print("========================================")

        send_email(
            "Amazon Product Checker - Target Price Reached",
            f"""🎉 Target price reached!

Product: {product_name}
Current Price: ₹{price:,.2f}
Availability: {availability}

The product is available at or below your target price.
"""
        )
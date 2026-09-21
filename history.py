import csv
from datetime import datetime


def save_history(product_name, price, availability, url):
    file_exists = False

    try:
        with open("history.csv", "r", encoding="utf-8"):
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open("history.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date & Time",
                "Product",
                "Price",
                "Availability",
                "URL"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            product_name,
            price,
            availability,
            url
        ])
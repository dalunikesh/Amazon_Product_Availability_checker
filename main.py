import time
from amazon_checker import check_product


while True:
    url = input("\nEnter Amazon product URL: ")

    target_price = input("Enter your target price: ₹")

    interval = int(input("Check every how many seconds? "))

    while True:
        check_product(url, target_price)

        choice = input("\nContinue monitoring? (y/n): ")

        if choice.lower() not in ["y", "yes"]:
            print("\nMonitoring stopped.")

            another = input("\nDo you want to check another product? (y/n): ")

            if another.lower() not in ["y", "yes"]:
                print("\nThank you for using Amazon Product Availability Checker!")
                exit()

            break

        print(f"\nWaiting {interval} seconds before checking again...")
        time.sleep(interval)
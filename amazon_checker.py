from selenium import webdriver
from history import save_history
from notifications import send_notification


def check_product(url, target_price):
    driver = None
    target_price = float(target_price)

    try:
        driver = webdriver.Chrome()
        driver.get(url)

        product_name = driver.title.split(" : Amazon.in")[0]

        price = driver.find_element(
            "xpath",
            "//span[@class='a-price']//span[@class='a-offscreen']"
        ).get_attribute("textContent")
        current_price = float(
            price.replace("₹", "").replace(",", "")
        )

        page_text = driver.find_element("tag name", "body").text

        if "In stock" in page_text:
            availability = "AVAILABLE"
        elif "Currently unavailable" in page_text:
            availability = "NOT AVAILABLE"
        else:
            availability = "UNKNOWN"

        print("\n========================================")
        print("   AMAZON PRODUCT AVAILABILITY CHECKER")
        print("========================================")
        print("Product:", product_name)
        print("Price:", price)
        print("Availability:", availability)
        print("URL:", url)
        if current_price <= target_price:
            print("🎉 Target price reached!")
        else:
            print("⏳ Target price not reached.")
        send_notification(
            product_name,
            current_price,
            availability,
            target_price
        )
        save_history(product_name, price, availability, url)

        print("========================================")

    except Exception as error:
        print("\n❌ Unable to check this product.")
        print("Reason:", error)

    finally:
        if driver:
            driver.quit()
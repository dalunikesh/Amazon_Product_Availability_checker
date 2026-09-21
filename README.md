# Amazon Product Availability Checker
## 📌 Project Description

Amazon Product Availability Checker is a Python-based project that checks the availability and price of products on Amazon.

The project can monitor products automatically, maintain price and availability history, and notify the user when the product reaches the target price or becomes available.
## ✨ Features

- 🔍 Check Amazon product price and availability
- 📊 Maintain price and availability history
- 🔄 Automatic product monitoring
- 🔔 Price and stock notifications
- 🎯 Target-price alert
- 📧 Email notification system
- 🛑 Option to stop monitoring
## 🛠️ Technologies Used

- Python
- Selenium
- SMTP
- Python-dotenv
- CSV
- Amazon product pages

## 📂 Project Structure

```text
Amazon_Product_Availability_checker/
│
├── main.py
├── amazon_checker.py
├── history.py
├── notifications.py
├── email_notification.py
├── history.csv
├── requirements.txt
├── .gitignore
├── .env
└── README.md

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>

## 📸 Example Output

```text
========================================
   AMAZON PRODUCT AVAILABILITY CHECKER
========================================
Product: OnePlus Nord 6
Price: ₹46,999.00
Availability: AVAILABLE
URL: Amazon Product URL

🎉 Target price reached!

🔔 NOTIFICATION
========================================
Product: OnePlus Nord 6
Current Price: ₹46,999.00
🎉 Target price reached!
The product is available at or below your target price.
========================================

📧 Email notification sent successfully!

## 🔐 Security

This project uses environment variables to store sensitive information such as email credentials.

The `.env` file is included in `.gitignore` and should **never be uploaded to GitHub**.

Before running the project, create your own `.env` file and add your email configuration:

```text
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com
## 🚀 Future Improvements

- Add a graphical user interface (GUI)
- Support multiple Amazon products at the same time
- Add WhatsApp or Telegram notifications
- Store product data in a database
- Add price-drop charts and analytics
- Improve Amazon page handling and error detection
## 👨‍💻 Author

**Nikesh Dalu**

This project was developed as a Python project to practice web automation, data handling, monitoring, and email notification systems.
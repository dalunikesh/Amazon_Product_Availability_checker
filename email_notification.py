import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv(override=True)


def send_email(subject, body):
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("EMAIL_RECEIVER")

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    message.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()

        server.login(sender_email, sender_password)

        server.send_message(message)

    print("📧 Email notification sent successfully!")
import smtplib, ssl
import os

HOST = "smtp.gmail.com"
PORT = 465

SENDER = "pythonemail194@gmail.com"
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

RECEIVER = "vanjasav194@gmail.com"


class Email:
    def send(self, message):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, RECEIVER, message)

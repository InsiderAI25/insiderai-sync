import os
import smtplib
from email.mime.text import MIMEText

def trigger_monique_alert(message):
    sender = os.getenv("GMAIL_SENDER")
    receiver = os.getenv("GMAIL_RECEIVER")
    password = os.getenv("GMAIL_APP_PASSWORD")

    if not all([sender, receiver, password]):
        print("[Gmail] Missing environment variables.")
        return

    msg = MIMEText(message)
    msg['Subject'] = '🧠 Monique Alert: Daily Sync'
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        print("[Gmail] Email sent successfully.")
    except Exception as e:
        print(f"[Gmail] Failed to send email: {e}")

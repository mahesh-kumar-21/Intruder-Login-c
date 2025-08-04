# send_email.py
import smtplib
import os
from email.message import EmailMessage
import sys

def send_email(image_path, timestamp):
    EMAIL_ADDRESS = "palavalisumathi10@gmail.com"
    EMAIL_PASSWORD = "dtbm ulem idkc fdpf"

    msg = EmailMessage()
    msg['Subject'] = f'🚨 Intruder Detected at {timestamp}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f'An intruder tried to access the system at {timestamp}. See the attached image.')

    with open(image_path, 'rb') as img:
        msg.add_attachment(img.read(), maintype='image', subtype='jpeg', filename=os.path.basename(image_path))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("📧 Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    # Expect image path and timestamp as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python send_email.py <image_path> <timestamp>")
    else:
        send_email(sys.argv[1], sys.argv[2])

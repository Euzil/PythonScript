import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
def send_email():
    sender_email = "your_email@example.com"
    receiver_email = "receiver@example.com"
    password = input("Type your password and press enter: ")
    message = MIMEMultipart("alternative")
    message["Subject"] = "Daily Reminder"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """\
    Hi,
    This is your daily reminder!
    """
    part = MIMEText(text, "plain")
    message.attach(part)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
schedule.every().day.at("10:30").do(send_email)
while True:
    schedule.run_pending()
    time.sleep(1)
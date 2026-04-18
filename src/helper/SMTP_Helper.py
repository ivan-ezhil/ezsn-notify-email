import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

# Load environment variables from the .env file (if present)
load_dotenv()

class smtp_connection():
    def __init__(self,host,port,sender_email,password):
        self.host=host
        self.port=port
        self.sender_email=sender_email
        self.password=password

    def __enter__(self):
        self.server = smtplib.SMTP(self.host, self.port)
        self.server.starttls()
        self.server.login(self.sender_email, self.password)
        return self

    def send_mail(self,receiver_email,subject,body):
        # Create the email
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain", "utf-8"))

        self.server.send_message(message)
        print("Email sent successfully!")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        if self.server:
            self.server.quit()
        if exc_type:
            print(f"Exception: {exc_value}")

# Usage
with smtp_connection(
    host='smtp.gmail.com',
    port=587,
    sender_email = "gayathri.ma43@gmail.com",
    password =os.getenv('PASSWORD')
) as smtp:

    smtp.send_mail(
        receiver_email = "NEC0914014@gmail.com",
        subject='Test Mail',
        body='Hello, this is a test email using Context Manager'
    )

import smtplib
from contextlib import contextmanager
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@contextmanager
def smtp_connection(sender_email, password):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    try:
        server.starttls()
        server.login(sender_email, password)
        yield server  # 👈 give server to 'with' block
    finally:
        server.quit()  # 👈 always runs


def smtp_email(sender_email, password, receiver_email):

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Test Email - Hi Ezhil"

    body = "Hello! This is a test email sent using Python."
    message.attach(MIMEText(body, "plain", "utf-8"))

    try:
        with smtp_connection(sender_email, password) as server:
            # Send email
            server.send_message(message)
            print("Email sent successfully!")

    except Exception as e:
        print("Error:", e)


# Your email credentials
sender_email = "gayathri.ma43@gmail.com"
receiver_email = "NEC0914014@gmail.com"
password = "wpcwqgbauwvadiac"  # Not your real password!

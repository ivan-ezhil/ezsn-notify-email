import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SMTP_Connection():
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

    def send_mail(self,receiver_email,subject,body,file_path,cc,bcc):
        # Create the email
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        filename = os.path.basename(file_path)

        with open(file_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            encoders.encode_base64(part)

            part.add_header("Content-Disposition", f"attachment; filename={filename}")
            # ✅ Add CC (visible)
            if cc:
                message["Cc"] = ", ".join(cc) if isinstance(cc, list) else cc

            message.attach(MIMEText(body, "html"))
            message.attach(part)

             # ✅ Combine all recipients
            recipients = [receiver_email]

            if cc:
                recipients += cc if isinstance(cc, list) else [cc]

            if bcc:
                recipients += bcc if isinstance(bcc, list) else [bcc]

        self.server.send_message(message,to_addrs=recipients)
        print("Email sent successfully!")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        if self.server:
            self.server.quit()
        if exc_type:
            print(f"Exception: {exc_value}")


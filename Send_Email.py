
import os

from dotenv import load_dotenv

from src.helper.SMTP_Helper import SMTP_Connection
from src.helper.TEMPLATE_String import EmailTemplate

# Load environment variables from the .env file (if present)
load_dotenv()

def send_email(email_inputs):
    print(email_inputs)
    print(type(email_inputs))
    et = EmailTemplate(email_inputs.email_details.html_file, email_inputs.template_details)
    et.read_file()
    print(et.template_dynamic_var())
    print(et.find_missing_input() )
    email_body=et.apply()

    with SMTP_Connection(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        sender_email = os.getenv('SENDER_EMAIL'),
        password =os.getenv('PASSWORD')
    ) as smtp:

        smtp.send_mail(
            receiver_email = email_inputs.email_details.receiver_email,
            subject=email_inputs.email_details.subject,
            body=email_body,
            file_path=email_inputs.email_details.file_path,
            cc=email_inputs.email_details.cc,
            bcc=email_inputs.email_details.bcc

        )

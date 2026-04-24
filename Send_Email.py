
import os

from dotenv import load_dotenv

from src.helper.SMTP_Helper import SMTP_Connection
from src.helper.TEMPLATE_String import EmailTemplate

# Load environment variables from the .env file (if present)
load_dotenv()

html_file = "templates/invoice.html"
user_input = {
    "customer_name": "$Nila,/n<b><script>alert('hi')</script>",
    "invoice_reference": "Amazon",
    "service_description":"invoice for products",
    "invoice_number":"98123HJO087",
    "invoice_date":"12/3/2026",
    "due_date":"15/03/2026",
    "amount_due":"15000",
    "payment_method":"Card",
    "sender_name":"Mathi",
    "company_name":"InfoTech",
    "contact_details":"987654321"
}


et = EmailTemplate(html_file, user_input)
et.read_file()
print(et.template_dynamic_var())
print(et.find_missing_input())
email_body=et.apply()


with SMTP_Connection(
    host='smtp.gmail.com',
    port=587,
    sender_email = "gayathri.ma43@gmail.com",
    password =os.getenv('PASSWORD')
) as smtp:

    smtp.send_mail(
        #receiver_email = "NEC0914014@gmail.com",
        receiver_email = "gayathri.ma43@gmail.com",
        subject='Test Mail',
        body=email_body,
        file_path="templates/test.pdf",
        cc=["gayathri.ma43@gmail.com"],
        bcc=["gayathria156@gmail.com"]

    )

#gayathri.ma43@gmail.com"

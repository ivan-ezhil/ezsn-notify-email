
from fastapi import FastAPI

from app.schemas.Emails import EmailInputs
from Send_Email import send_email

app = FastAPI()

@app.post("/send-email")
def send(email_inputs:EmailInputs):
    print(email_inputs)
    if(email_inputs.customer_details.customer_id==1):
        return {"message": "Insuffient balance"}
    result = send_email(email_inputs)
    return {"message": result}

# user_input = {

    #     "email_details":{
    #         "receiver_email" :"gayathri.ma43@gmail.com",
    #         "subject":"Test Mail",
    #         "html_file":"templates/invoice.html",
    #         "file_path":"templates/test.pdf",
    #         "cc":["gayathri.ma43@gmail.com"],
    #         "bcc":["gayathria156@gmail.com"]
    #     },
    #     "email_inputs":{
    #         "customer_name": "$Nila,/n<b><script>alert('hi')</script>",
    #         "invoice_reference": "Amazon",
    #         "service_description":"invoice for products",
    #         "invoice_number":"98123HJO087",
    #         "invoice_date":"12/3/2026",
    #         "due_date":"15/03/2026",  
    #         "amount_due":"15000",
    #         "payment_method":"Card",
    #         "sender_name":"Mathi",
    #         "company_name":"InfoTech",
    #         "contact_details":"987654321",
    #     }
    # }

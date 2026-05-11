from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EmailDetails(BaseModel):
    receiver_email:str
    subject:str
    html_file:str
    file_path:str
    cc:list
    bcc:list

class CustomerDetails(BaseModel):
    customer_id:int

class EmailInputs(BaseModel):
    email_details:EmailDetails
    template_details:dict
    customer_details:CustomerDetails

# class EmailTemplateData(BaseModel):
#     customer_name: str
#     invoice_reference: str
#     service_description:str
#     invoice_number: str
#     invoice_date:date
#     due_date:str
#     amount_due:int
#     payment_method:str
#     sender_name:str
#     company_name:str
#     contact_details:int

from fastapi import FastAPI

from Send_Email import send_email

app = FastAPI()


@app.post("/send-email")
def send(html_file:str,receiver_email:str):
    html_file = "templates/invoice.html"
    receiver_email = "gayathri.ma43@gmail.com"
    result = send_email(html_file,receiver_email)
    return {"message": result}

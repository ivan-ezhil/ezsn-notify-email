from fastapi import FastAPI
from Send_Email import EmailTemplate

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server running"}

@app.post("/send-email")
def send():
    return {"message": "Email sent"}

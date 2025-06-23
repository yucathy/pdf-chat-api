# app/main.py
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from .routes import router

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "PDF Chat API is running inside Docker!"}

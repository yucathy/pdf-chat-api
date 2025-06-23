# app/main.py
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from .routes import router
from .query_log import init_db

init_db()

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "PDF Chat API is running inside Docker!"}

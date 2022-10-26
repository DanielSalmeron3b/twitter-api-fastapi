# FastAPI
from fastapi import FastAPI

app = FastAPI()

from models import User, UserBase, UserLogin
from models import Tweet

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}
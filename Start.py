from fastapi import FastAPI
from datetime import datetime

fast = FastAPI

@fast.get("/")
def index():
    email = "tomiwajegede29@gmail.com"
    current_time  = datetime.now()


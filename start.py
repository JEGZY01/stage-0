from fastapi import FastAPI,status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",status_code=status.HTTP_200_OK)
def home():
    email = "tomiwajegede29@gmail.com"
    current_time  = str(datetime.now().replace(microsecond=0).isoformat())+"Z"
    github_url = "https://github.com/JEGZY01/stage-0"
    return{
        "email": email,
        "current_datetime": current_time,
        "github_url": github_url
    }


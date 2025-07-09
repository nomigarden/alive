from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CHECKIN_FILE = "checking_data.json"

# if not file, initialize it
def init_checkin_file():
    if not os.path.exists(CHECKIN_FILE):
        with open(CHECKIN_FILE, "w") as f:
            json.dump({"last_checking": None}, f)

init_checkin_file()

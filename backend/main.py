from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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

class CheckinRequest(BaseModel):
    timestamp: str
    ip: str | None = None
    location: str | None = None
    
@app.get("/last-checkin")
async def get_last_checkin():
    with open(CHECKIN_FILE, "r") as f:
        data = json.load(f)
    return data

@app.post("/check-in")
async def post_checkin(payload: CheckinRequest, request: Request):
    client_ip = payload.ip or request.client.host
    
    new_data = {
        "last_checkin": payload.timestamp,
        "ip": client_ip,
        "location": payload.location,
    }
    
    with open(CHECKIN_FILE, "w") as f:
        json.dump(new_data, f, indent=2)
        
    return {"message": "Check.in saved", "data": new_data}
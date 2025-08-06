# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import datetime

app = FastAPI()

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy signal data class
class Signal(BaseModel):
    symbol: str
    horizon: str
    signal: str
    timestamp: str

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/signal")
def get_signal():
    return [
        Signal(symbol="BTC", horizon="Short", signal="BUY", timestamp=str(datetime.datetime.now())),
        Signal(symbol="ETH", horizon="Strategic", signal="HOLD", timestamp=str(datetime.datetime.now()))
    ]

# Optional: Add POST or webhook endpoints if needed

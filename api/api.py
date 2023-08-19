import os
from fastapi import FastAPI


BINANCE_API_KEY = os.environ.get("BINANCE_API_KEY")
BINANCE_API_SECRET = os.environ.get("BINANCE_API_SECRET")

app = FastAPI()

# This would likely connect to your trading system in a real-world scenario
algorithm_status = "Stopped"

@app.get("/")
def read_root():
    return {"message": "Trading Algorithm API"}

@app.get("/status")
def read_status():
    global algorithm_status
    return {"status": algorithm_status}

@app.post("/start")
def start_algorithm():
    global algorithm_status
    algorithm_status = "Running"
    return {"status": algorithm_status, "message": "Algorithm started"}

@app.post("/stop")
def stop_algorithm():
    global algorithm_status
    algorithm_status = "Stopped"
    return {"status": algorithm_status, "message": "Algorithm stopped"}

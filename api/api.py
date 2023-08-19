import os
from fastapi import FastAPI
from api.routes.balances import balance_router

app = FastAPI()
app.include_router(balance_router, prefix="/balances", tags=["Balances"])

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

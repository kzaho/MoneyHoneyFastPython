from fastapi import APIRouter, HTTPException
from api.utils.binance_client import init_binance_client

router = APIRouter()

# ... [Rest of the code, like Binance setup]


@router.get("/balance")
def get_balance():
    # ... [Function body to get balance]
    try:
        client = init_binance_client()
        account_info = client.get_account()
        balances = account_info.get("balances")
        return {"balances": balances}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

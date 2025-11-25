from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "UP"}

@app.get("/quote")
def get_quote(
    from_currency: str = Query(..., alias="from"), 
    to_currency: str = Query(..., alias="to")
):
    # Mock data
    return {
        "from": from_currency,
        "to": to_currency,
        "price": 5.42,
        "timestamp": datetime.now().isoformat()
    }
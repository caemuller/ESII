from fastapi import FastAPI, Query
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "UP"}

@app.get("/history")
def get_history(
    from_currency: str = Query(..., alias="from"), 
    to_currency: str = Query(..., alias="to")
):
    now = datetime.now()
    # Mock alues
    return {
        "from": from_currency,
        "to": to_currency,
        "values": [
            {"timestamp": (now - timedelta(days=1)).isoformat(), "price": 5.42},
            {"timestamp": (now - timedelta(days=2)).isoformat(), "price": 5.38},
            {"timestamp": (now - timedelta(days=3)).isoformat(), "price": 5.47}
        ]
    }
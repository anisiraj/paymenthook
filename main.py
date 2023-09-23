from fastapi import FastAPI
from paymenthook.models.definitions import PayOutSegment,TransactionNotification,Report
app = FastAPI()



@app.post("/hooks/trasaction/")
async def process_transactions(body: TransactionNotification):
    return body

@app.post("/hooks/payout/")
async def process_payout_segment(body: PayOutSegment):
    return body

@app.post("/hooks/eodreport")
async def create_item(body: Report):
    return body


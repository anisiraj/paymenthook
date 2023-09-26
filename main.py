from fastapi import FastAPI
from paymenthook.models.definitions import PayOutSegment,TransactionNotification,Report
from paymenthook.data.async_mongo_controller import init_db
from paymenthook.actions.handler_manager import get_dummy_handler_manager
import json

app = FastAPI()
manager=get_dummy_handler_manager()


@app.on_event("startup")
async def start_db():
    await init_db()


@app.post("/hooks/trasaction/")
async def process_transactions(transaction: TransactionNotification):
   
    result= await manager.dispatch("/hooks/trasaction/",transaction)
    return {"msg":f"transaction dispatched {transaction.transaction_id}"}

@app.post("/hooks/payout/")
async def process_payout_segment(segment: PayOutSegment):    
    result= await manager.dispatch("/hooks/payout/",segment)    
    return  {"msg":f"payment segment dispatched to {segment.transaction_id}"}

@app.post("/hooks/eodreport")
async def create_item(report: Report):
    result= await manager.dispatch("/hooks/eodreport",report) 
    return   {"msg":f"report  dispatched for {report.publication_date}"}

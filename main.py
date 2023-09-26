from fastapi import FastAPI
from paymenthook.models.definitions import PayOutSegment,TransactionNotification,Report
from paymenthook.data.async_mongo_controller import init_db
from paymenthook.actions.handler_manager import get_dummy_handler_manager


app = FastAPI()



@app.on_event("startup")
async def start_db():
    await init_db()


@app.post("/hooks/trasaction/")
async def process_transactions(transaction: TransactionNotification):
    manager=get_dummy_handler_manager()
    result= await manager.dispatch("/hooks/trasaction/",transaction)
    return result

@app.post("/hooks/payout/")
async def process_payout_segment(segment: PayOutSegment):
    manager=get_dummy_handler_manager()
    result= await manager.dispatch("/hooks/payout/",segment)
    
    return result

@app.post("/hooks/eodreport")
async def create_item(body: Report):
    return body


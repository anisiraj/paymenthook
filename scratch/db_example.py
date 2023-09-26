
import sys
sys.path.append("../")

from paymenthook.data.async_mongo_controller import init_db,TransactionODM,insert_transaction,update_payment_segment,insert_report
from paymenthook.models.definitions import TransactionNotification,Report,PayOutSegment


data={
    "Psp Reference": "MYRANDOMID",
    "amount": 0,
    "timestamp": "2023-09-24T20:50:52.661Z",
    "Merchant Account": "MYRANDOMACCOUNT",
    "transaction_type": "AUTH",
    "seller_split":None,
    "valpay_split":None,
    "fee_split":None
}
payout_data={
  "Psp Reference": "MYRANDOMID",
  "amount": 0,
  "timestamp": "2023-09-24T21:07:54.725Z",
  "split_id": "SELLER"
}

report_data={
  "rows": [
    {
      "Psp Reference": "string",
      "amount": 0,
      "timestamp": "2023-09-26T09:14:49.870Z",
      "Merchant Account": "string",
      "transaction_type": "AUTH",
      "some_key":"some_vLUE"
    }
  ]
}

async def test():     
    await init_db()  
    
    
    p=PayOutSegment(**payout_data)
    print(p)
    await update_payment_segment(p)
    
async def report_test():     
    await init_db()  
    
    
    p=Report(**report_data)
    print(p)
    await insert_report(p)
    

    
    
   
if __name__=="__main__":
    import asyncio
    asyncio.run(report_test())
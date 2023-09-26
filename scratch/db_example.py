
import sys
sys.path.append("../")

from paymenthook.data.async_mongo_controller import init_db,TransactionODM
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

async def test():     
    await init_db()
   
    
    p=PayOutSegment(**payout_data)
    
    await TransactionODM.find_one(TransactionODM.transaction_id==p.transaction_id).\
        update ({"$set": {TransactionODM.seller_split: p}})
if __name__=="__main__":
    import asyncio
    asyncio.run(test())
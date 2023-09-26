
from config import mongo_uri, transaction_collection_name, report_collection_name, mongo_db_name
from beanie import init_beanie,Document
import motor.motor_asyncio
from paymenthook.models.definitions import TransactionNotification,Report,PayOutSegment,PayoutSplitType


class TransactionODM(TransactionNotification,Document):
   class Settings:
      name=transaction_collection_name
      
class ReportODM(Report,Document):
   class Settings:
      name=report_collection_name    
      
      
      
async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
       mongo_uri
    )
    await init_beanie(database=client[mongo_db_name], document_models=[TransactionODM,ReportODM])
 
    
async def insert_transaction(transaction_notification:TransactionNotification):
   """_summary_

   Args:
       transaction_notification (TransactionNotification): a transaction notification object
   """
   #convert to ODM, we have one to one map given the inheritence model
   notification=TransactionODM(**transaction_notification.model_dump())   
   #todo have an upsert function
   await TransactionODM.insert_one(notification)
   
async def update_payment_segment(payout:PayOutSegment):
   """_summary_

   Args:
       transaction_id (str): _description_
       segment (PayOutSegment): _description_
   """
   #todo : better error handling
   #find the correspoding transaction
   target= await TransactionODM.find_one(
      TransactionODM.transaction_id==payout.transaction_id)   
   
   print(target)
   #update the corresponding split   
   if target is not None:
      print("updating split")
  
         
      if payout.split_id==PayoutSplitType.SELLER:
         await target.update({"$set": {TransactionODM.seller_split: payout}})      
      elif payout.split_id==PayoutSplitType.VALPAY:
         await target.update({"$set": {TransactionODM.valpay_split: payout}})
      elif payout.split_id==PayoutSplitType.FEE:
         await target.update({"$set": {TransactionODM.fee_split: payout}})
   else:
      raise Exception("Transaction not found")
      
async def insert_report(report:Report):
   """_summary_

   Args:
       report (Report): _description_
   """
   #convert to ODM, we have one to one map given the inheritence model
   print("publishing report")
   report=ReportODM(**report.model_dump())   
   #todo have an upsert function based on date
   await ReportODM.insert_one(report)      
  
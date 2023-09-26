from typing import Any
from abc import ABC, abstractmethod
from paymenthook.models.definitions import TransactionNotification,Report,PayOutSegment
from paymenthook.data.async_mongo_controller import (
    insert_transaction,
    update_payment_segment,
    insert_report
    )

class BaseEntityHandler:  
    
    @abstractmethod
    async def run(self,target:Any,**kwargs) :  
        """
        This is the main function that is called by the handler manager
        kwargs: will pass any runtime parameters to the handler
        target: will be the object that is passed to the handler
        
        """  
       
        pass
    
class LogPublisher(BaseEntityHandler):    
    
    """
    Very basic handler compares ta
    
    """
    target_type=Any
    async def run(self,target:Any) :
        print(target)
        
class PropagationPublisher(BaseEntityHandler):
    subscription_urls=[]    
    async def run(self,target:Any) :
        for url in self.__class__.subscription_urls:
            print(f"Propagating to {url}")   
            #todo : make async request to url subscribers    

class S3Publisher(BaseEntityHandler):
    """
    Dumps a json to S3 bucket
    Args:
        BaseEntityHandler (_type_): _description_
        
    """
    default_bucket_name=None
    def   __init__(self,bucket_name:str) :
        self.bucket_name=bucket_name  or self.default_bucket_name
    async def run(self,target:Any) :
        raise NotImplementedError("S3Publisher is not implemented")
    

   
   
class TransactionPublisher(BaseEntityHandler):
    """
     Takens in the transaction data and upserts it into the database
    
    """
    async def run(self,target:TransactionNotification) :
        await insert_transaction(target)
        
class PaymentSegmentPublisher(BaseEntityHandler):
    async def run(self,target:PayOutSegment) :
        await update_payment_segment(target)
   
class ReportPublisher(BaseEntityHandler):
    async def run(self,target:Any) :
        await  insert_report(target)
       
   
class ReportReconciliationHandler(BaseEntityHandler):
    async def run(self,target:Any) :
        print("Reconciling report")
       
       
    
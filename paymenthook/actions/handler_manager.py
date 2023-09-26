from collections import defaultdict
from paymenthook.actions.handlers import (BaseEntityHandler,LogPublisher,
                                          TransactionPublisher,
                                          PaymentSegmentPublisher,
                                          ReportPublisher,)
import asyncio
from typing import Any,List

class HandlerManager:        
    @classmethod
    def from_dict(cls,path_dict:dict[str,List[BaseEntityHandler]]):
        raise NotImplementedError
    @classmethod
    def from_json(cls,filename:str):
        raise NotImplementedError
    
    
        
    def __init__(self, path_dict:dict[str,List[BaseEntityHandler]]=None) -> None:
        "maps paths to handlers"
        self.path_dict=path_dict or defaultdict(list)
        
        
    def register(self,path:str,handler:BaseEntityHandler,dispatch_id=None):        
        self.path_dict[path].append(handler)
        
    async def dispatch(self,path,target:Any)->asyncio.Future[tuple] :      
        return asyncio.gather(*[handler.run(target) for handler in self.path_dict[path]],return_exceptions=True)
    
    
    
def get_dummy_handler_manager()->HandlerManager:
    h=HandlerManager()
    h.register("/hooks/trasaction/",LogPublisher(),dispatch_id="log_transaction")
    h.register("/hooks/trasaction/",TransactionPublisher(),dispatch_id="transaction")
    
    h.register("/hooks/payout/",LogPublisher(),dispatch_id="log_payout")
    h.register("/hooks/payout/",PaymentSegmentPublisher(),dispatch_id="payout")    
    
    h.register("/hooks/eodreport",LogPublisher(),dispatch_id="log")
    h.register("/hooks/eodreport",ReportPublisher(),dispatch_id="eodreport")
    
    return h
    
    
    
    
    
    
    
    
   
        
    
    
    
    
    
    
    

    
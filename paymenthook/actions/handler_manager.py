from collections import defaultdict
from paymenthook.actions.handlers import BaseEntityHandler,LogPublisher,TransactionPublisher,PaymentSegmentPublisher
import asyncio
from typing import Any,List

class HandlerManager:        
    
    
        
    def __init__(self, path_dict:dict[str,List[BaseEntityHandler]]=None) -> None:
        "maps paths to handlers"
        self.path_dict=path_dict or defaultdict(list)
        
        
    def register(self,path:str,handler:BaseEntityHandler,dispatch_id=None):        
        self.path_dict[path].append(handler)
        
    async def dispatch(self,path,target:Any)->asyncio.Future[tuple] :      
        return asyncio.gather(*[handler.run(target) for handler in self.path_dict[path]],return_exceptions=True)
    
    
    
def get_dummy_handler_manager()->HandlerManager:
    h=HandlerManager()
    h.register("/hooks/trasaction/",LogPublisher(),dispatch_id="log")
    h.register("/hooks/trasaction/",TransactionPublisher(),dispatch_id="transaction")
    
    h.register("/hooks/payout/",LogPublisher(),dispatch_id="log")
    h.register("/hooks/payout/",PaymentSegmentPublisher(),dispatch_id="payout")    
    
    return h
    
    
    
    
    
    
    
    
   
        
    
    
    
    
    
    
    

    
from typing import Any
from abc import ABC, abstractmethod


class BaseEntityHandler:  
    
    @abstractmethod
    async def run(self,target:Any) :     
        pass
    
class LogPublisher(BaseEntityHandler):
    
    """
    Very basic handler compares ta
    
    """
    target_type=Any
    async def run(self,target:Any) :
        print(target)
       
    
class MongoDBPublisher(BaseEntityHandler):
    async def run(self,target:Any) :
        print(target)
        
class ReportPublisher(BaseEntityHandler):
    async def run(self,target:Any) :
        print(target)

class SQLPublisher(BaseEntityHandler):
    async def run(self,target:Any) :
       raise NotImplementedError("SQLPublisher is not implemented")
      
    
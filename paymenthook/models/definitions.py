from pydantic  import BaseModel,Field,AliasChoices,ConfigDict,computed_field,Extra
import datetime 
import enum 
from typing import List,Optional

#crrate prefdefined fields for parsing with aliases

prefab_fields = {
    "transaction_id":Field(
        validation_alias=AliasChoices(
            "Psp Reference","transaction_id"
            )
        ),
    "merchant_id":Field(validation_alias=AliasChoices("Merchant Account",   "merchant_id")),  
    "timestamp":Field(default_factory=datetime.datetime.now)  
}

class TrasnactionType(enum.Enum) :
    AUTH="AUTH"
    REFUND="REFUND"
    DISPUTE="DISPUTE"
    
class PayoutSplitType(enum.Enum) :
    SELLER="SELLER"
    VALPAY="VALPAY"
    FEE="FEE"
  
class BaseTransactionInfo(BaseModel,extra=Extra.allow) :
    transaction_id:str=prefab_fields["transaction_id"]   
    amount:float=0.0
    timestamp:datetime.datetime=prefab_fields["timestamp"]
    
  
    
class PayOutSegment(BaseTransactionInfo) :   
    split_id:PayoutSplitType


class TransactionNotification(BaseTransactionInfo):  
    merchant_id:str=prefab_fields["merchant_id"] 
    transaction_type:TrasnactionType
    seller_split:Optional[PayOutSegment]=None
    valpay_split:Optional[PayOutSegment]=None
    fee_split:Optional[PayOutSegment]=None
    
   
  
    
class ReportRow(BaseTransactionInfo) :   
    merchant_id:str=prefab_fields["merchant_id"] 
    transaction_type:TrasnactionType
    
    
class Report(BaseModel):
    
    rows:List[ReportRow]
    #given report is a end-of-day report, we can compute the date at time of publication and will be a unique key
    #in the mongo collection
    @computed_field
    @property
    def publication_date(self) -> int:
        return datetime.datetime.now().date()
    
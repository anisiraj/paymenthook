from pydantic  import BaseModel,Field,AliasChoices
import datetime 
import enum 
from typing import List,Optional

prefab_fields = {
    "transaction_id":Field(
        validation_alias=AliasChoices(
            "Psp Reference","transaction_id"
            )
        ),
    "merchant_id":Field(validation_alias="Merchant Account"),  
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
  
class BaseTransactionInfo(BaseModel) :
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
    split_id:PayoutSplitType
    transaction_type:TrasnactionType
    
class Report(BaseModel):
    rows:List[ReportRow]
    
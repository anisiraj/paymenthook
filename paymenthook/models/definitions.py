from pydantic  import Basemodel,Field
import datetime 
import enum 
from typing import List


prefab_fields = {
    "transaction_id":Field(validation_alias="Psp Reference"),
    "merchant_id":Field(validation_alias="Merchant Account"),    
    
}

class TrasnactionType(enum.Enum) :
    AUTH:"AUTH"
    REFUND:"REFUND"
    DISPUTE:"DISPUTE"
    
class PayoutSplitType(enum.Enum) :
    SELLER:"SELLER"
    VALPAY:"VALPAY"
    FEE:"FEE"
  
class BaseTransactionInfo(Basemodel) :
    transaction_id:str=prefab_fields["transaction_id"]
    merchant_id:str=prefab_fields["merchant_id"]
    amount:float
    date:datetime
   


class TransactionNotification(BaseTransactionInfo):   
    transaction_type:TrasnactionType
  

class PayOutSegment(BaseTransactionInfo) :   
    split_id:PayoutSplitType
    
class ReportRow(BaseTransactionInfo) :  
    split_id:PayoutSplitType
    transaction_type:TrasnactionType
    
    
class Report(Basemodel):
    rows:List[ReportRow]
    
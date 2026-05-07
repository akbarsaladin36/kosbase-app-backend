from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class TransactionResponse(BaseModel):
    user_uuid: str
    owner_uuid: str
    room_code: str
    description: str
    base_price: int
    discount_price: int
    total_price: int
    status_cd: str
    created_at: datetime
    created_by: str
    created_by_username: str

    model_config = {"from_attributes": True}

class TransactionsMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[List[TransactionResponse]] = None

class TransactionMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[TransactionResponse] = None

from pydantic import BaseModel
from typing import Optional

class CreateTransactionInput(BaseModel):
    user_uuid: str
    owner_uuid: str
    room_code: str
    description: str
    base_price: int
    discount_price: int

class UpdateTransactionInput(BaseModel):
    status_cd: str
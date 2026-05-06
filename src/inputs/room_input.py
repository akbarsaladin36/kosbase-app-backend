from pydantic import BaseModel
from typing import Optional

class CreateRoomInput(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    price: str

class UpdateRoomInput(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    price: str
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProfileResponse(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_by_username: Optional[str] = None

    model_config = {"from_attributes": True}

class ProfileMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[ProfileResponse] = None
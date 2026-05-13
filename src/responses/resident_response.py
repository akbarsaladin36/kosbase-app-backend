from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CreateResidentResponse(BaseModel):
    room_code: Optional[str] = None
    owner_uuid: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    created_by_username: Optional[str] = None

    model_config = {"from_attributes": True}

class UpdateResidentResponse(BaseModel):
    full_name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_by_username: Optional[str] = None

    model_config = {"from_attributes": True}

class ResidentsResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[List[CreateResidentResponse]] = None

class ResidentResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[CreateResidentResponse] = None

class UpdateResidentMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[UpdateResidentResponse] = None


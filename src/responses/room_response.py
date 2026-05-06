from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class RoomResponse(BaseModel):
    owner_uuid: Optional[str] = None
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    price: Optional[str] = None
    status_cd: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    created_by_username: Optional[str] = None

    model_config = {"from_attributes": True}

class UpdateRoomResponse(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    price: Optional[str] = None
    status_cd: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_by_username: Optional[str] = None

    model_config = {"from_attributes": True}

class RoomsMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[List[RoomResponse]] = None

class RoomMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[RoomResponse] = None

class CreateRoomMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[RoomResponse] = None

class UpdateRoomMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[UpdateRoomResponse] = None
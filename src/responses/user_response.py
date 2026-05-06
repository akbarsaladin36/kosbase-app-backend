from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserDataResponse(BaseModel):
    id: int
    uuid:                Optional[str]      = None
    username:            Optional[str]      = None
    email:               Optional[str]      = None
    first_name:          Optional[str]      = None 
    last_name:           Optional[str]      = None 
    address:             Optional[str]      = None 
    phone_number:        Optional[str]      = None 
    role:                Optional[str]      = None
    is_active:           Optional[int]      = None
    created_at:          Optional[datetime] = None
    created_by:          Optional[str]      = None
    created_by_username: Optional[str]      = None
    updated_at:          Optional[datetime] = None 
    updated_by:          Optional[str]      = None 
    updated_by_username: Optional[str]      = None

    model_config = {"from_attributes": True}

class UsersResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[List[UserDataResponse]] = None

class UserResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[UserDataResponse] = None

    
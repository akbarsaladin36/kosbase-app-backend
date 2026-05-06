from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class RegisterResponse(BaseModel):
    id: int
    uuid: str
    username: str
    email: str
    created_at: datetime
    created_by: str
    created_by_username: str

    model_config = {"from_attributes": True}

class LoginResponse(BaseModel):
    uuid: str
    username: str
    email: str
    role: str

    model_config = {"from_attributes": True}

class RegisterMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[RegisterResponse] = None

class LoginMessageResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[LoginResponse] = None
    token: str


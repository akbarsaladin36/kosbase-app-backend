from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class CreateUserInput(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    address: str
    phone_number: str
    role: str

class UpdateUserInput(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str
    role: str
    is_active: Optional[int] = 1
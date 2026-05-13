from pydantic import BaseModel

class CreateResidentInput(BaseModel):
    room_code: str
    full_name: str
    email: str
    address: str
    phone_number: str

class UpdateResidentInput(BaseModel):
    full_name: str
    address: str
    phone_number: str
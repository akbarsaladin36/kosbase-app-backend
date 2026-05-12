from pydantic import BaseModel

class UpdateProfileInput(BaseModel):
    first_name: str
    last_name: str
    address: str
    phone_number: str
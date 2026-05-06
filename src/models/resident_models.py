from sqlalchemy import Column, Integer, String, Text, DateTime
from src.config.database import Base

class Resident(Base):

    __tablename__ = "residents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_uuid = Column(String(150), nullable=True)
    room_code = Column(String(150), nullable=True)
    uuid = Column(String(150), nullable=True)
    full_name = Column(String(200), nullable=True)
    address = Column(Text, nullable=True)
    phone_number = Column(String(30), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True)
    created_by = Column(String(150), nullable=True)
    created_by_username = Column(String(150), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    updated_by = Column(String(150), nullable=True)
    updated_by_username = Column(String(150), nullable=True)
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from src.config.database import Base

class Room(Base):

    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    owner_uuid = Column(String(150), nullable=True)
    code = Column(String(150), nullable=True)
    name = Column(String(150), nullable=True)
    description = Column(Text, nullable=True)
    type = Column(String(30), nullable=True)
    price = Column(String(30), nullable=True)
    status_cd = Column(String(30), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True)
    created_by = Column(String(150), nullable=True)
    created_by_username = Column(String(150), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    updated_by = Column(String(150), nullable=True)
    updated_by_username = Column(String(150), nullable=True)
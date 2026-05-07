from sqlalchemy import Column, Integer, String, Text, DateTime
from src.config.database import Base

class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_uuid = Column(String(150), nullable=True)
    owner_uuid = Column(String(150), nullable=True)
    room_code = Column(String(150), nullable=True)
    code = Column(String(150), nullable=True)
    description = Column(Text, nullable=True)
    base_price = Column(String(30), nullable=True)
    discount_price = Column(String(30), nullable=True)
    total_price = Column(String(30), nullable=True)
    status_cd = Column(String(30), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True)
    created_by = Column(String(150), nullable=True)
    created_by_username = Column(String(150), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    updated_by = Column(String(150), nullable=True)
    updated_by_username = Column(String(150), nullable=True)
from src.config.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Payment(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement= True, index=True)
    user_uuid = Column(String(150), nullable=True)
    transaction_code = Column(String(150), nullable=True, index=True)
    code = Column(String(150), nullable=True)
    description = Column(Text, nullable=True)
    total_price = Column(String(30), nullable=True)
    status_cd = Column(String(30), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True)
    created_by = Column(String(150), nullable=True)
    created_by_username = Column(String(150), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    updated_by = Column(String(150), nullable=True)
    updated_by_username = Column(String(150), nullable=True)
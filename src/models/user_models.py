from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from src.config.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    uuid = Column(String(150), nullable=True)
    username = Column(String(150), nullable=True)
    email = Column(String(150), unique=True, nullable=True)
    password = Column(String(150), nullable=True)
    first_name = Column(String(200), nullable=True)
    last_name = Column(String(200), nullable=True)
    address = Column(Text, nullable=True)
    phone_number = Column(String(20), nullable=True)
    role = Column(String(20), nullable=True)
    is_active = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=True)
    created_by = Column(String(150), nullable=True)
    created_by_username = Column(String(150), nullable=True)
    updated_at = Column(DateTime(timezone=True), nullable=True)
    updated_by = Column(String(150), nullable=True)
    updated_by_username = Column(String(150), nullable=True)

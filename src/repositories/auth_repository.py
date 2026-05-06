from src.models.user_models import User 
from sqlalchemy.orm import Session
from typing import Optional

class AuthRepository:

    def __init__(self, db = Session):
        self.db = db
    
    def get_user_repository(self, username: str) -> Optional[User]:
        user = self.db.query(User).filter(User.username == username).first()
        return user
    
    def register_repository(self, auth_register_input: dict) -> User:
        user = User(**auth_register_input)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
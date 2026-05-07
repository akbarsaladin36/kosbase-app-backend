from src.models.user_models import User
from sqlalchemy.orm import Session
from typing import Optional

class UserRepository:
    def __init__(self, db = Session):
        self.db = db

    def get_users_repository(self) -> tuple[list[User]]:
        users = self.db.query(User).all()
        return users
    
    def get_user_repository(self, username: str) -> Optional[User]:
        user = self.db.query(User).filter(User.username == username).first()
        return user
    
    def get_user_by_id_repository(self, user_uuid: str) -> Optional[User]:
        user = self.db.query(User).filter(User.uuid == user_uuid).first()
        return user

    def create_user_repository(self, user_create_input: dict) -> User:
        user = User(**user_create_input)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update_user_repository(self, user: User, user_update_input: dict) -> User:
        for field, value in user_update_input.items():
            setattr(user, field, value)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete_user_repository(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
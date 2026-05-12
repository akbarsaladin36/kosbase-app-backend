from sqlalchemy.orm import Session
from src.models.user_models import User

class ProfileRepository:
    def __init__(self, db = Session):
        self.db = db

    def get_profile_repository(self, username: str) -> User:
        profile = self.db.query(User).filter(User.username == username).first()
        return profile
    
    def update_profile_repository(self, update_profile_input: dict, profile: User) -> User:
        for field, value in update_profile_input.items():
            setattr(profile, field, value)
        self.db.commit()
        self.db.refresh(profile)
        return profile
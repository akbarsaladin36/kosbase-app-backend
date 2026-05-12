from fastapi import Depends, Request
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.repositories.profile_repository import ProfileRepository
from src.services.profile_service import ProfileService
from src.inputs.profile_input import UpdateProfileInput

def get_profile_service(db: Session = Depends(get_db)) -> ProfileService:
    profileRepository = ProfileRepository(db)
    return ProfileService(profileRepository)

class ProfileController:
    @staticmethod
    def get_profile_controller(req: Request, profileService: ProfileService = Depends(get_profile_service)):
        current_user = req.state.current_user
        return profileService.get_profile_service(current_user)
    
    @staticmethod
    def update_profile_controller(req: Request, payload: UpdateProfileInput, profileService: ProfileService = Depends(get_profile_service)):
        current_user = req.state.current_user
        return profileService.update_profile_service(payload, current_user)
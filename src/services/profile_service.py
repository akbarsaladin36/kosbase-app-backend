from fastapi import HTTPException, status
from datetime import datetime
from src.repositories.profile_repository import ProfileRepository
from src.responses.profile_response import ProfileMessageResponse, ProfileResponse
from src.inputs.profile_input import UpdateProfileInput

class ProfileService:
    def __init__(self, profileRepository: ProfileRepository):
        self.profileRepository = profileRepository

    def get_profile_service(self, current_user: dict) -> ProfileMessageResponse:
        profile = self.profileRepository.get_profile_repository(current_user.get("username"))

        if profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A profile data is not found!"
            )
        else:
            return ProfileMessageResponse(
                status_code=status.HTTP_200_OK,
                message="A profile data is succesfully appeared!",
                data=profile
            )
        
    def update_profile_service(self, payload: UpdateProfileInput, current_user: dict) -> ProfileMessageResponse:
        profile = self.profileRepository.get_profile_repository(current_user.get("username"))

        if profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A profile data is not found!"
            )
        else:
            update_profile_setdata = payload.model_dump()
            update_profile_setdata["updated_at"] = datetime.now()
            update_profile_setdata["updated_by"] = current_user.get("uuid")
            update_profile_setdata["updated_by_username"] = current_user.get("username")
            update_profile = self.profileRepository.update_profile_repository(update_profile_setdata, profile)
            validate_update_profile = ProfileResponse.model_validate(update_profile)
            return ProfileMessageResponse(
                status_code=status.HTTP_200_OK,
                message="An existing profile data is succesfully updated!",
                data=validate_update_profile
            )
from src.repositories.user_repository import UserRepository
from fastapi import HTTPException, status
from src.inputs.user_input import CreateUserInput, UpdateUserInput
from src.responses.user_response import UserDataResponse, UsersResponse, UserResponse
from src.helper.index import generate_hash_password, generate_uuid
from datetime import datetime

class UserService:

    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    def get_users_service(self) -> UsersResponse:
        users = self.userRepository.get_users_repository()

        if users is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A users data are empty!"
            )
        else:
            users_data = [UserDataResponse.model_validate(user) for user in users]
            return UsersResponse(
                status_code=status.HTTP_200_OK,
                message="A users data are succesfully appeared",
                data=users_data
            )
        
    def get_user_service(self, username: str) -> UserResponse:
        user = self.userRepository.get_user_repository(username)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A user data is not found!"
            )
        else:
            return UserResponse(
                status_code=status.HTTP_200_OK,
                message="A user data is succesfully appeared!",
                data=user
            )
        
    def create_user_service(self, payload: CreateUserInput, current_user: dict) -> UserResponse:
        user = self.userRepository.get_user_repository(payload.username)

        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user data is previously registered!"
            )
        else:
            user_set_data = payload.model_dump()
            uuid = generate_uuid()
            user_set_data["uuid"] = uuid
            user_set_data["password"] = generate_hash_password(user_set_data["password"])
            user_set_data["role"] = "user"
            user_set_data["is_active"] = 1
            user_set_data["created_at"] = datetime.now()
            user_set_data["created_by"] = current_user.get("uuid")
            user_set_data["created_by_username"] = current_user.get("username")
            create_user = self.userRepository.create_user_repository(user_set_data)
            user_data = UserDataResponse.model_validate(create_user)
            return UserResponse(
                status_code=status.HTTP_200_OK,
                message="A new user data is succesfully created!",
                data=user_data
            )
        
    def update_user_service(self, username: str, payload: UpdateUserInput, current_user: dict) -> UserResponse:
        user = self.userRepository.get_user_repository(username)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A user data is not found!"
            )
        else:
            user_update_set_data = payload.model_dump()
            user_update_set_data["updated_at"] = datetime.now()
            user_update_set_data["updated_by"] = current_user.get("uuid")
            user_update_set_data["updated_by_username"] = current_user.get("username")
            update_user = self.userRepository.update_user_repository(user, user_update_set_data)
            user_data = UserDataResponse.model_validate(update_user)
            return UserResponse(
                status_code=status.HTTP_200_OK,
                message="An existing user data is succesfully updated!",
                data=user_data
            )
        
    def delete_user_service(self, username: str) -> UserResponse:
        user = self.userRepository.get_user_repository(username)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A user data is not found!"
            )
        else:
            self.userRepository.delete_user_repository(user)
            return UserResponse(
                status_code=status.HTTP_200_OK,
                message="A existing user data is succesfully deleted!"
            )
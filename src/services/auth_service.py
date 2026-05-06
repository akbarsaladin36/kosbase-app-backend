from fastapi import HTTPException, status
from datetime import datetime
from src.repositories.auth_repository import AuthRepository
from src.responses.auth_response import RegisterMessageResponse, LoginMessageResponse
from src.inputs.auth_input import RegisterInput, LoginInput
from src.helper.index import generate_hash_password, verify_hash_password, generate_uuid
from src.helper.jwt import create_token

class AuthService:
    def __init__(self, authRepository: AuthRepository):
        self.authRepository = authRepository

    def register_service(self, payload: RegisterInput) -> RegisterMessageResponse:
        user = self.authRepository.get_user_repository(payload.username)
        if user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A username is registered! Please try find a new username again!"
            )
        else:
            uuid = generate_uuid()
            register_data = payload.model_dump()
            register_data["uuid"] = uuid
            register_data["password"] = generate_hash_password(register_data["password"])
            register_data["role"] = "user"
            register_data["is_active"] = 1
            register_data["created_at"] = datetime.now()
            register_data["created_by"] = uuid
            register_data["created_by_username"] = register_data["username"]
            user = self.authRepository.register_repository(register_data)
            return RegisterMessageResponse(
                status_code=status.HTTP_200_OK,
                message="A new user is succesfully created!",
                data=user
            )
    
    def login_service(self, payload: LoginInput) -> LoginMessageResponse:
        user = self.authRepository.get_user_repository(payload.username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A username is not found! Please register now!"
            )
        else:
            # login_input = payload.model_dump()
            if verify_hash_password(payload.password, user.password) is False:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="A password did not match! Please try again!"
                )
            else:
                token = create_token(user.uuid, user.username, user.email, user.role)
                return LoginMessageResponse(
                    status_code=status.HTTP_200_OK,
                    message="A user is succesfully login",
                    data=user,
                    token=token
                )
            
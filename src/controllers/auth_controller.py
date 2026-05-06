from sqlalchemy.orm import Session
from fastapi import Depends
from src.config.database import get_db
from src.repositories.auth_repository import AuthRepository
from src.services.auth_service import AuthService
from src.inputs.auth_input import RegisterInput, LoginInput

def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    authRepository = AuthRepository(db)
    return AuthService(authRepository)

class AuthController:
    @staticmethod
    def register_controller(payload: RegisterInput, authService: AuthService = Depends(get_auth_service)):
        return authService.register_service(payload)
    
    @staticmethod
    def login_controller(payload: LoginInput, authService: AuthService = Depends(get_auth_service)):
        return authService.login_service(payload)
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService
from src.inputs.user_input import CreateUserInput, UpdateUserInput

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    userRepository = UserRepository(db)
    return UserService(userRepository)

class UserController:
    @staticmethod
    def get_users_controller(userService: UserService = Depends(get_user_service)):
        return userService.get_users_service()
    
    @staticmethod
    def get_user_controller(username: str, userService: UserService = Depends(get_user_service)):
        return userService.get_user_service(username)
    
    @staticmethod
    def create_user_controller(payload: CreateUserInput, req: Request, userService: UserService = Depends(get_user_service)):
        current_user = req.state.current_user
        return userService.create_user_service(payload, current_user)
    
    @staticmethod
    def update_user_controller(username: str, payload: UpdateUserInput, req: Request, userService: UserService = Depends(get_user_service)):
        current_user = req.state.current_user
        return userService.update_user_service(username, payload, current_user)
    
    @staticmethod
    def delete_user_controller(username: str, userService: UserService = Depends(get_user_service)):
        return userService.delete_user_service(username)
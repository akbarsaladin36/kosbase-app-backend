from fastapi import Depends, Request
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.repositories.room_repository import RoomRepository
from src.services.room_service import RoomService
from src.inputs.room_input import CreateRoomInput, UpdateRoomInput

def get_room_service(db: Session = Depends(get_db)) -> RoomService:
    roomRepository = RoomRepository(db)
    return RoomService(roomRepository)

class RoomController:
    @staticmethod
    def get_rooms_controller(roomService: RoomService = Depends(get_room_service)):
        return roomService.get_rooms_service()
    
    @staticmethod
    def get_rooms_by_user_controller(req: Request, roomService: RoomService = Depends(get_room_service)):
        current_user = req.state.current_user
        return roomService.get_rooms_by_user_service(current_user)
    
    @staticmethod
    def get_room_controller(room_code: str, roomService: RoomService = Depends(get_room_service)):
        return roomService.get_room_service(room_code)
    
    @staticmethod
    def create_room_controller(payload: CreateRoomInput, req: Request, roomService: RoomService = Depends(get_room_service)):
        current_user = req.state.current_user
        return roomService.create_room_service(payload, current_user)
    
    @staticmethod
    def update_room_controller(room_code: str, payload: UpdateRoomInput, req: Request, roomService: RoomService = Depends(get_room_service)):
        current_user = req.state.current_user
        return roomService.update_room_service(room_code, payload, current_user)
    
    @staticmethod
    def delete_room_controller(room_code: str, roomService: RoomService = Depends(get_room_service)):
        return roomService.delete_room_service(room_code)
from fastapi import HTTPException, status
from src.repositories.room_repository import RoomRepository
from src.responses.room_response import RoomsMessageResponse, RoomMessageResponse, CreateRoomMessageResponse, UpdateRoomResponse, UpdateRoomMessageResponse
from src.inputs.room_input import CreateRoomInput, UpdateRoomInput
from src.helper.index import generate_code
from datetime import datetime

class RoomService:
    def __init__(self, roomRepository: RoomRepository):
        self.roomRepository = roomRepository

    def get_rooms_service(self) -> RoomsMessageResponse:
        rooms = self.roomRepository.get_rooms_repository()

        if len(rooms) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="All rooms data are empty!"
            )
        else:
            return RoomsMessageResponse(
                status_code=status.HTTP_200_OK,
                message="All rooms data are succesfully appeared!",
                data=rooms
            )
        
    def get_rooms_by_user_service(self, current_user: dict) -> RoomsMessageResponse:
        owner_uuid = current_user.get("uuid")
        rooms = self.roomRepository.get_rooms_by_user_repository(owner_uuid)

        if len(rooms) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="All rooms data are empty!"
            )
        else:
            return RoomsMessageResponse(
                status_code=status.HTTP_200_OK,
                message="All rooms data are succesfully appeared!",
                data=rooms
            )
        
    def get_room_service(self, room_code: str) -> RoomMessageResponse:
        room = self.roomRepository.get_room_repository(room_code)

        if room is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A room data is not found!"
            )
        else:
            return RoomMessageResponse(
                status_code=status.HTTP_200_OK,
                message="A room data is succesfully appeared!",
                data=room
            )
        
    def create_room_service(self, payload: CreateRoomInput, current_user: dict) -> CreateRoomMessageResponse:
        room_set_data = payload.model_dump()
        room_set_data["owner_uuid"] = current_user.get("uuid")
        room_set_data["code"] = generate_code("RC")
        room_set_data["status_cd"] = "active"
        room_set_data["created_at"] = datetime.now()
        room_set_data["created_by"] = current_user.get("uuid")
        room_set_data["created_by_username"] = current_user.get("username")
        create_room = self.roomRepository.create_room_repository(room_set_data)
        return CreateRoomMessageResponse(
            status_code=status.HTTP_200_OK,
            message="A new room is succesfully created!",
            data=create_room
        )
    
    def update_room_service(self, room_code: str, payload: UpdateRoomInput, current_user: dict) -> UpdateRoomMessageResponse:
        room = self.roomRepository.get_room_repository(room_code)

        if room is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A room data is not found!"
            )
        else:
            room_set_data = payload.model_dump()
            room_set_data["updated_at"] = datetime.now()
            room_set_data["updated_by"] = current_user.get("uuid")
            room_set_data["updated_by_username"] = current_user.get("username")
            update_room = self.roomRepository.update_room_repository(room, room_set_data)
            update_room_data = UpdateRoomResponse.model_validate(update_room)
            return UpdateRoomMessageResponse(
                status_code=status.HTTP_200_OK,
                message="An existing room data is succesfully updated!",
                data=update_room_data
            )
        
    def delete_room_service(self, room_code: str) -> RoomMessageResponse:
        room = self.roomRepository.get_room_repository(room_code)

        if room is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A room data is not found!"
            )
        else:
            self.roomRepository.delete_room_repository(room)
            return RoomMessageResponse(
                status_code=status.HTTP_200_OK,
                message="An existing room data is succesfully deleted!"
            )
    
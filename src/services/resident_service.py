from fastapi import HTTPException, status
from datetime import datetime
from src.repositories.resident_repository import ResidentRepository
from src.repositories.room_repository import RoomRepository
from src.responses.resident_response import ResidentsResponse, ResidentResponse, CreateResidentResponse, UpdateResidentResponse, UpdateResidentMessageResponse
from src.inputs.resident_input import CreateResidentInput, UpdateResidentInput
from src.helper.index import generate_uuid

class ResidentService:
    def __init__(self, residentRepository: ResidentRepository, roomRepository: RoomRepository):
        self.residentRepository = residentRepository
        self.roomRepository = roomRepository

    def get_residents_service(self) -> ResidentsResponse:
        residents = self.residentRepository.get_residents_repository()

        if len(residents) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="All residents data are empty!"
            )
        else:
            return ResidentsResponse(
                status_code=status.HTTP_200_OK,
                message="All residents data are succesfully appeared!",
                data=residents
            )

    def get_residents_by_owner_service(self, current_user: dict) -> ResidentsResponse:
        owner_uuid = current_user.get("uuid")
        residents = self.residentRepository.get_residents_by_owner_repository(owner_uuid)

        if len(residents) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="All residents data are empty!"
            )
        else:
            return ResidentsResponse(
                status_code=status.HTTP_200_OK,
                message="All residents data are succesfully appeared!",
                data=residents
            )
    
    def get_resident_service(self, resident_uuid: str) -> ResidentResponse:
        resident = self.residentRepository.get_resident_repository(resident_uuid)

        if resident is None:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="A resident data is not found"
            )
        else:
            return ResidentResponse(
                status_code=status.HTTP_200_OK,
                message="A resident data is succesfully appeared!",
                data=resident
            )
        
    def create_resident_service(self, payload: CreateResidentInput, current_user: dict) -> ResidentResponse:
        check_room = self.roomRepository.get_room_repository(payload.room_code)

        if check_room is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A room is not found! Please try again!"
            )
        else:
            resident_set_data = payload.model_dump()
            resident_set_data["owner_uuid"] = current_user.get("uuid")
            resident_set_data["uuid"] = generate_uuid()
            resident_set_data["email"] = f"{resident_set_data["email"]}@kosbase.com"
            resident_set_data["created_at"] = datetime.now()
            resident_set_data["created_by"] = current_user.get("uuid")
            resident_set_data["created_by_username"] = current_user.get("username")
            create_resident = self.residentRepository.create_resident_repository(resident_set_data)
            validate_create_resident = CreateResidentResponse.model_validate(create_resident)
            return ResidentResponse(
                status_code=status.HTTP_200_OK,
                message="A new resident is succesfully created!",
                data=validate_create_resident
            )
    
    def update_resident_service(self, resident_uuid: str, payload: UpdateResidentInput, current_user: dict) -> UpdateResidentMessageResponse:
        resident = self.residentRepository.get_resident_repository(resident_uuid)

        if resident is None:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="A resident data is not found"
            )
        else:
            resident_set_data = payload.model_dump()
            resident_set_data["updated_at"] = datetime.now()
            resident_set_data["updated_by"] = current_user.get("uuid")
            resident_set_data["updated_by_username"] = current_user.get("username")
            update_resident = self.residentRepository.update_resident_repository(resident, resident_set_data)
            validate_update_resident = UpdateResidentResponse.model_validate(update_resident)
            return UpdateResidentMessageResponse(
                status_code=status.HTTP_200_OK,
                message="An existing resident data is succesfully updated!",
                data=validate_update_resident
            )
        
    def delete_resident_service(self, resident_uuid: str) -> ResidentResponse:
        resident = self.residentRepository.get_resident_repository(resident_uuid)

        if resident is None:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="A resident data is not found"
            )
        else:
            self.residentRepository.delete_resident_repository(resident)
            return ResidentResponse(
                status_code=status.HTTP_200_OK,
                message="An existing resident data is succesfully deleted!",
            )
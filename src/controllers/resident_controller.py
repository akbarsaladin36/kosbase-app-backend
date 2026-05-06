from fastapi import Depends, Request
from sqlalchemy.orm import Session
from src.repositories.resident_repository import ResidentRepository
from src.repositories.room_repository import RoomRepository
from src.services.resident_service import ResidentService
from src.config.database import get_db
from src.inputs.resident_input import CreateResidentInput, UpdateResidentInput

def get_resident_service(db: Session = Depends(get_db)) -> ResidentService:
    residentRepository = ResidentRepository(db)
    roomRepository = RoomRepository(db)
    return ResidentService(residentRepository, roomRepository)

class ResidentController:
    @staticmethod
    def get_residents_controller(residentService: ResidentService = Depends(get_resident_service)):
        return residentService.get_residents_service()
    
    @staticmethod
    def get_residents_by_owner_controller(req: Request, residentService: ResidentService = Depends(get_resident_service)):
        current_user = req.state.current_user
        return residentService.get_residents_by_owner_service(current_user)
    
    @staticmethod
    def get_resident_controller(resident_uuid: str, residentService: ResidentService = Depends(get_resident_service)):
        return residentService.get_resident_service(resident_uuid)
    
    @staticmethod
    def create_resident_controller(req: Request, payload: CreateResidentInput, residentService: ResidentService = Depends(get_resident_service)):
        current_user = req.state.current_user
        return residentService.create_resident_service(payload, current_user)
    
    @staticmethod
    def update_resident_controller(resident_uuid: str, req: Request, payload: UpdateResidentInput, residentService: ResidentService = Depends(get_resident_service)):
        current_user = req.state.current_user
        return residentService.update_resident_service(resident_uuid, payload, current_user)
    
    @staticmethod
    def delete_resident_controller(resident_uuid: str, residentService: ResidentService = Depends(get_resident_service)):
        return residentService.delete_resident_service(resident_uuid)
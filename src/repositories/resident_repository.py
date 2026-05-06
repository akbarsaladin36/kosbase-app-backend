from sqlalchemy.orm import Session
from src.models.resident_models import Resident

class ResidentRepository:
    def __init__(self, db = Session):
        self.db = db

    def get_residents_repository(self) -> tuple[list[Resident]]:
        residents = self.db.query(Resident).all()
        return residents
    
    def get_residents_by_owner_repository(self, owner_uuid: str) -> tuple[list[Resident]]:
        residents = self.db.query(Resident).filter(Resident.owner_uuid == owner_uuid).all()
        return residents
    
    def get_resident_repository(self, resident_uuid: str) -> Resident:
        resident = self.db.query(Resident).filter(Resident.uuid == resident_uuid).first()
        return resident
    
    def create_resident_repository(self, create_resident_input: dict) -> Resident:
        resident = Resident(**create_resident_input)
        self.db.add(resident)
        self.db.commit()
        self.db.refresh(resident)
        return resident
    
    def update_resident_repository(self, resident: Resident, update_resident_input: dict) -> Resident:
        for field,value in update_resident_input.items():
            setattr(resident, field, value)
        self.db.commit()
        self.db.refresh(resident)
        return resident
    
    def delete_resident_repository(self, resident: Resident) -> None:
        self.db.delete(resident)
        self.db.commit()
    

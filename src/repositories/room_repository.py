from sqlalchemy.orm import Session
from src.models.room_models import Room

class RoomRepository:
    def __init__(self, db = Session):
        self.db = db

    def get_rooms_repository(self) -> tuple[list[Room]]:
        users = self.db.query(Room).all()
        return users
    
    def get_rooms_by_user_repository(self, owner_uuid: str) -> tuple[list[Room]]:
        users = self.db.query(Room).filter(Room.owner_uuid == owner_uuid).all()
        return users
    
    def get_room_repository(self, room_code: str) -> Room:
        user = self.db.query(Room).filter(Room.code == room_code).first()
        return user
    
    def create_room_repository(self, create_room_input: dict) -> Room:
        room = Room(**create_room_input)
        self.db.add(room)
        self.db.commit()
        self.db.refresh(room)
        return room
    
    def update_room_repository(self, room: Room, update_room_input: dict) -> Room:
        for field, value in update_room_input.items():
            setattr(room, field, value)
        self.db.commit()
        self.db.refresh(room)
        return room
    
    def delete_room_repository(self, room: Room) -> Room:
        self.db.delete(room)
        self.db.commit()

    
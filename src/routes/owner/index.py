from fastapi import APIRouter
from src.routes.owner.rooms import router as rooms_router

router = APIRouter()

router.include_router(rooms_router, prefix="/rooms", tags=["Rooms - Owner"])
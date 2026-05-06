from fastapi import APIRouter
from src.routes.admin.users import router as users_router
from src.routes.admin.rooms import router as rooms_router
from src.routes.admin.residents import router as resident_router

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["Users - Admin"])
router.include_router(rooms_router, prefix="/rooms", tags=["Rooms - Admin"])
router.include_router(resident_router, prefix="/residents", tags=["Residents - Admin"])



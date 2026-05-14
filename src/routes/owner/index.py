from fastapi import APIRouter
from src.routes.owner.rooms import router as rooms_router
from src.routes.owner.residents import router as residents_router
from src.routes.owner.transactions import router as transactions_router
from src.routes.owner.profile import router as profile_router

router = APIRouter()

router.include_router(rooms_router, prefix="/rooms", tags=["Rooms - Owner"])
router.include_router(residents_router, prefix="/residents", tags=["Residents - Owner"])
router.include_router(transactions_router, prefix="/transactions", tags=["Transactions - Owner"])
router.include_router(profile_router, prefix="/profile", tags=["Profile - Owner"])
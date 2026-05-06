from fastapi import APIRouter, Depends
from src.routes.auth.auth import router as auth_router
from src.routes.admin.index import router as admin_router
from src.middlewares.auth_middleware import user_role_required

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Auth"])

router.include_router(admin_router, prefix="/admin", dependencies=[Depends(user_role_required("admin"))])
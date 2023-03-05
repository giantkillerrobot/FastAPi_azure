from fastapi import APIRouter

from .endpoints import users
from .endpoints import others

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(others.router, prefix="/others", tags=["Others"])
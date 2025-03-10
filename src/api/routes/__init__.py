from api.routes import items, user
from fastapi import APIRouter

router = APIRouter()
router.include_router(items.router)
router.include_router(user.router)

__all__ = ["router"]

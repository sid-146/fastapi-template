from fastapi import APIRouter

from api.routes import items, user

router = APIRouter()
router.include_router(items.router)
router.include_router(user.router)

__all__ = ["router"]

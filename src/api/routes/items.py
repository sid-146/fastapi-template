from fastapi import APIRouter


router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.get("/items")
def read_users():
    return [{"item": "Banana"}, {"username": "Rotten Banana"}]

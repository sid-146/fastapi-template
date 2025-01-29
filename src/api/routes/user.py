from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/user")
def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

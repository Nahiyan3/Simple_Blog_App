from fastapi import APIRouter, Depends
from controllers.auth_controller import signup
from models.user_model import UserCreate

router = APIRouter()

@router.post("/signup")
async def signup_route(user: UserCreate):
    return await signup(user)

from fastapi import APIRouter, Depends
from controllers.auth_controller import signup, login, get_user
from models.user_model import UserCreate
from models.user_model import UserLogin


router = APIRouter()

@router.post("/signup")
async def signup_route(user: UserCreate):
    return await signup(user)

@router.post("/login")
async def login_route(user: UserLogin):
    return await login(user)

@router.get("/user/{user_id}")
async def get_user_route(user_id: str):
    return await get_user(user_id)
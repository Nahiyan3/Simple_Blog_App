from fastapi import APIRouter, Depends
from controllers.auth_controller import signup
from models.user_model import UserCreate
from models.user_model import UserLogin
from services.auth_service import login_user


router = APIRouter()

@router.post("/signup")
async def signup_route(user: UserCreate):
    return await signup(user)

@router.post("/login")
async def login_route(user: UserLogin):
    return await login_user(user)
from fastapi import HTTPException
from models.user_model import UserCreate  
from models.user_model import UserLogin
from services.auth_service import create_user
from core.auth import create_access_token, hash_password, verify_password


async def signup(user: UserCreate):   
    try:
        user_id = await create_user(user)
        token = create_access_token({"user_id": user_id})
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def login(user: UserLogin):
    return await login_user(user)
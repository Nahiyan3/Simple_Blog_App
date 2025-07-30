from fastapi import HTTPException, status
from models.user_model import UserCreate
from services.auth_service import create_user

async def signup(user: UserCreate):
    try:
        user_id = await create_user(user)
        return {"message": "User created successfully", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

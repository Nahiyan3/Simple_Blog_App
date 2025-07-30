from core.database import user_collection
from core.auth import hash_password
from models.user_model import UserCreate
from models.user_model import UserLogin
from bson import ObjectId
from core.auth import create_access_token, verify_password


async def create_user(user: UserCreate):
    # Check if user exists
    if await user_collection.find_one({"email": user.email}):
        raise Exception("User with this email already exists.")
    
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    result = await user_collection.insert_one(user_dict)
    return str(result.inserted_id)

async def login_user(user: UserLogin):
    existing_user = await user_collection.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token_data = {"sub": user.email}
    token = create_access_token(token_data)
    
    return {"access_token": token, "token_type": "bearer"}
from core.database import user_collection
from core.auth import hash_password
from models.user_model import UserCreate
from bson import ObjectId

async def create_user(user: UserCreate):
    # Check if user exists
    if await user_collection.find_one({"email": user.email}):
        raise Exception("User with this email already exists.")
    
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    result = await user_collection.insert_one(user_dict)
    return str(result.inserted_id)

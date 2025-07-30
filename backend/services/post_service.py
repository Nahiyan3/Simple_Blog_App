from core.database import post_collection
from models.post_model import PostCreate
from bson import ObjectId
from datetime import datetime

def post_helper(post) -> dict:
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "content": post["content"],
        "author_id": post["author_id"],
        "created_at": post["created_at"]
    }

async def create_post(post: PostCreate):
    post_data = post.dict()
    post_data["created_at"] = datetime.utcnow()
    new_post = await post_collection.insert_one(post_data)
    created_post = await post_collection.find_one({"_id": new_post.inserted_id})
    return post_helper(created_post)

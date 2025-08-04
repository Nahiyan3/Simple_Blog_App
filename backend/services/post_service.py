from core.database import post_collection, user_collection
from models.post_model import PostCreate
from bson import ObjectId
from datetime import datetime

def post_helper(post) -> dict:
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "content": post["content"],
        "author_id": post["author_id"],
        "author_name": post.get("author_name", "Unknown"),
        "created_at": post["created_at"]
    }

async def create_post(post: PostCreate):
    post_data = post.dict()
    post_data["created_at"] = datetime.utcnow()
    new_post = await post_collection.insert_one(post_data)
    created_post = await post_collection.find_one({"_id": new_post.inserted_id})
    return post_helper(created_post)

async def all_posts():
    pipeline = [
        {
            "$addFields": {
                "author_object_id": {"$toObjectId": "$author_id"}
            }
        },
        {
            "$lookup": {
                "from": "users",
                "localField": "author_object_id",
                "foreignField": "_id",
                "as": "author_info"
            }
        },
        {
            "$addFields": {
                "author_name": {
                    "$ifNull": [
                        {"$arrayElemAt": ["$author_info.username", 0]},
                        "Unknown"
                    ]
                }
            }
        },
        {
            "$project": {
                "author_info": 0,  
                "author_object_id": 0  
            }
        }
    ]
    
    posts_cursor = post_collection.aggregate(pipeline)
    posts = []
    async for post in posts_cursor:
        posts.append(post_helper(post))
    return posts
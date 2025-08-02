from fastapi import HTTPException
from models.post_model import PostCreate
from services.post_service import create_post , all_posts

async def handle_create_post(post: PostCreate):
    try:
        return await create_post(post)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_all_posts():
    try:
        return await all_posts()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

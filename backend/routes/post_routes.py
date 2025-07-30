from fastapi import APIRouter
from models.post_model import PostCreate
from controllers.post_controller import handle_create_post

router = APIRouter()

@router.post("/posts")
async def create_new_post(post: PostCreate):
    return await handle_create_post(post)

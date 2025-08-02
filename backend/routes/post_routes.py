from fastapi import APIRouter
from models.post_model import PostCreate , PostOut
from controllers.post_controller import handle_create_post , get_all_posts

router = APIRouter()

@router.post("/posts")
async def create_new_post(post: PostCreate):
    return await handle_create_post(post)

@router.get("/posts",  response_model=list[PostOut])
async def fetch_all_posts():
    return await get_all_posts()    

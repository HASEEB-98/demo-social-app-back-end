from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from .dependencies import get_db
from .. import schemas, crud, auth, cache

router = APIRouter()

# Endpoint for adding a new post
@router.post("/posts", response_model=schemas.Post)
def add_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    if len(post.text.encode('utf-8')) > 1 * 1024 * 1024:  # 1 MB
        raise HTTPException(status_code=400, detail="Post too large")
    return crud.create_post(db=db, post=post, user_id=current_user.id)

# Endpoint for retrieving all posts by the current user
@router.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    if current_user.id in cache.post_cache:
        return cache.post_cache[current_user.id]
    posts = crud.get_posts_by_user(db, user_id=current_user.id)
    cache.post_cache[current_user.id] = posts
    return posts

# Endpoint for deleting a post by its ID
@router.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == post_id, models.Post.owner_id == current_user.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.delete_post(db=db, post_id=post_id)

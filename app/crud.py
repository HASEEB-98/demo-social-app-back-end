from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import get_password_hash

# Retrieve a user by their email address
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Create a new user in the database
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Create a new post in the database
def create_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(text=post.text, owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Retrieve all posts by a specific user
def get_posts_by_user(db: Session, user_id: int):
    return db.query(models.Post).filter(models.Post.owner_id == user_id).all()

# Delete a post by its ID
def delete_post(db: Session, post_id: int):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    db.delete(post)
    db.commit()
    return post
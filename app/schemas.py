from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional

# Base Pydantic model for User data validation
class UserBase(BaseModel):
    email: EmailStr

# Pydantic model for creating a new user
class UserCreate(UserBase):
    password: constr(min_length=8)

# Pydantic model for representing a user in responses
class User(UserBase):
    id: int

    class Config:
        from_attributes = True

# Base Pydantic model for Post data validation
class PostBase(BaseModel):
    text: constr(max_length=1024)

# Pydantic model for creating a new post
class PostCreate(PostBase):
    pass

# Pydantic model for representing a post in responses
class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

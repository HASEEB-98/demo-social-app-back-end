from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# SQLAlchemy model for the User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(10000), nullable=False)

    # Establish relationship with the Post table
    posts = relationship("Post", back_populates="owner")

# SQLAlchemy model for the Post table
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(10000), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Establish relationship with the User table
    owner = relationship("User", back_populates="posts")

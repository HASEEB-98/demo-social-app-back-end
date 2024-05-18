from fastapi import FastAPI
import app.models as models
from app.routers import users
from app.database import engine

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# Include the user router for handling user-related endpoints
app.include_router(users.router)

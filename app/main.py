from fastapi import FastAPI
from . import models, database
from .routes import router

# Create the database tables based on your models
models.Base.metadata.create_all(bind=database.engine)

# Initialize FastAPI app
app = FastAPI(
    title="Inventory Management System",
    description="A simple CRUD API to manage inventory items using FastAPI and PostgreSQL.",
    version="1.0.0"
)

# Register all API routes
app.include_router(router)

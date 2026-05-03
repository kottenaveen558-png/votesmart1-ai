"""FastAPI application factory"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import elections

def create_app() -> FastAPI:
    app = FastAPI(
        title="Election Process Education API",
        description="Interactive assistant for election process education",
        version="1.0.0"
    )
    
    # CORS middleware for security
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )
    
    # Include routes
    app.include_router(elections.router, prefix="/api/v1")
    
    return app

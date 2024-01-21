"""API routes for the Langchain Chat."""

from fastapi import APIRouter

from app.api.routes import (
    health_route,
)

api_router = APIRouter()

api_router.include_router(health_route.router)

"""Health Response Schema for the API"""

from typing import Literal
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health Response Schema"""
    status: Literal["ok"] = Field(default="ok")

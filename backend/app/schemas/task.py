from datetime import datetime

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = None
    status: str = Field(default="todo", max_length=50)
    position: int = Field(default=0, ge=0)
    assignee: str | None = Field(default=None, max_length=100)
    column_id: int


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    status: str | None = Field(default=None, max_length=50)
    position: int | None = Field(default=None, ge=0)
    assignee: str | None = Field(default=None, max_length=100)
    column_id: int | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    position: int
    assignee: str | None
    column_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

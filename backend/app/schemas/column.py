from pydantic import BaseModel, Field

from app.schemas.task import TaskResponse


class ColumnCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    position: int = Field(default=0, ge=0)


class ColumnUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    position: int | None = Field(default=None, ge=0)


class ColumnResponse(BaseModel):
    id: int
    name: str
    position: int

    model_config = {"from_attributes": True}


class ColumnWithTasksResponse(ColumnResponse):
    tasks: list[TaskResponse] = []

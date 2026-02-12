from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), nullable=False, default="todo")
    position = Column(Integer, nullable=False, default=0)
    assignee = Column(String(100), nullable=True)
    notes = Column(String(500), nullable=True)
    column_id = Column(Integer, ForeignKey("columns.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    column = relationship("Column_", back_populates="tasks")
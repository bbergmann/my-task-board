from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.column import Column_
from app.schemas.column import ColumnCreate, ColumnResponse, ColumnUpdate, ColumnWithTasksResponse

router = APIRouter(prefix="/api/columns", tags=["columns"])


@router.post("/", response_model=ColumnResponse, status_code=201)
def create_column(column: ColumnCreate, db: Session = Depends(get_db)) -> Column_:
    db_column = Column_(**column.model_dump())
    db.add(db_column)
    db.commit()
    db.refresh(db_column)
    return db_column


@router.get("/", response_model=list[ColumnWithTasksResponse])
def list_columns(db: Session = Depends(get_db)) -> list[Column_]:
    return db.query(Column_).order_by(Column_.position).all()


@router.get("/{column_id}", response_model=ColumnWithTasksResponse)
def get_column(column_id: int, db: Session = Depends(get_db)) -> Column_:
    column = db.query(Column_).filter(Column_.id == column_id).first()
    if not column:
        raise HTTPException(status_code=404, detail="Column not found")
    return column


@router.put("/{column_id}", response_model=ColumnResponse)
def update_column(column_id: int, column_update: ColumnUpdate, db: Session = Depends(get_db)) -> Column_:
    column = db.query(Column_).filter(Column_.id == column_id).first()
    if not column:
        raise HTTPException(status_code=404, detail="Column not found")
    for field, value in column_update.model_dump(exclude_unset=True).items():
        setattr(column, field, value)
    db.commit()
    db.refresh(column)
    return column


@router.delete("/{column_id}", response_model=ColumnResponse)
def delete_column(column_id: int, db: Session = Depends(get_db)) -> Column_:
    column = db.query(Column_).filter(Column_.id == column_id).first()
    if not column:
        raise HTTPException(status_code=404, detail="Column not found")
    db.delete(column)
    db.commit()
    return column

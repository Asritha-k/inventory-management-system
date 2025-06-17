from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /items
@router.get("/items", response_model=list[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

# POST /items
@router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

# PUT /items/{item_id}
@router.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, quantity: int, db: Session = Depends(get_db)):
    item = crud.update_item(db, item_id, quantity)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# DELETE /items/{item_id}
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}

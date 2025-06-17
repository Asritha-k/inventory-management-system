from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

# GET all items
def get_items(db: Session):
    return db.query(models.Item).all()

# CREATE a new item
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, quantity=item.quantity)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# UPDATE an existing item
def update_item(db: Session, item_id: int, quantity: int):
    item = db.query(models.Item).get(item_id)
    if item:
        item.quantity = quantity
        item.last_updated = datetime.utcnow()
        db.commit()
        db.refresh(item)
    return item

# 🔹 DELETE an item
def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).get(item_id)
    if item:
        db.delete(item)
        db.commit()
    return item

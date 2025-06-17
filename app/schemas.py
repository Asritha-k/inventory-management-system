from pydantic import BaseModel
from datetime import datetime

# Base class for shared fields
class ItemBase(BaseModel):
    name: str
    quantity: int

# Schema used for creating a new item
class ItemCreate(ItemBase):
    pass

# Schema used for reading an item from the DB
class Item(ItemBase):
    id: int
    last_updated: datetime

model_config = {
        "from_attributes": True
    }

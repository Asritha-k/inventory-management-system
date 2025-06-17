from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)              # Auto-incrementing unique ID
    name = Column(String, index=True, nullable=False)               # Item name (e.g., "Keyboard")
    quantity = Column(Integer, nullable=False)                      # Number of items
    last_updated = Column(DateTime, default=lambda: datetime.now(timezone.utc))      # Timestamp of last update

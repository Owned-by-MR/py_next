from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime
from ..database import Base  # Import Base from database.py

class ProductDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sku = Column(String, unique=True, index=True)
    category = Column(String)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class ProductBase(BaseModel):
    name: str
    sku: str
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

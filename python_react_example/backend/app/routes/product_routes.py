from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..models.product import Product, ProductCreate
from ..database import get_db
from ..crud import product as product_crud

router = APIRouter()

@router.get("/", response_model=List[Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = product_crud.get_products(db, skip=skip, limit=limit)
    return products

@router.post("/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create_product(db=db, product=product)

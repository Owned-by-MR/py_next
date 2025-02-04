from sqlalchemy.orm import Session
from ..models.product import ProductDB, ProductCreate

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProductDB).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = ProductDB(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

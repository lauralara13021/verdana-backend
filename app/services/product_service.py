from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

def create_product(db: Session, data: ProductCreate):
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db: Session):
    return db.query(Product).all()

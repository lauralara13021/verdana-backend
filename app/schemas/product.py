from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    category: str
    price: float
    amount: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True

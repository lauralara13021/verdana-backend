from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    category: str
    price: float
    amount: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    price: float | None = None
    amount: int | None = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True

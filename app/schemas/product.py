from pydantic import BaseModel


class ProductCreate(BaseModel):
    ''''''
    name: str
    info: str
    price: float
    category: str


class ProductDB(ProductCreate):
    id: int

    class Config:
        orm_mode = True


class ProductUpdate(ProductCreate):
    ''''''
    pass

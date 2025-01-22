from pydantic import BaseModel


class CategoryCreate(BaseModel):
    ''''''
    name: str
    description: str


class CategoryDB(CategoryCreate):
    id: int

    class Config:
        orm_mode = True


class CategoryUpdate(CategoryCreate):
    ''''''
    pass

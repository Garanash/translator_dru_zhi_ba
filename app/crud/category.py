from app.crud.base import CRUDBase
from app.models.category import Category


class CategoryCRUD(CRUDBase):
    """"""
    pass


category_crud = CategoryCRUD(Category)

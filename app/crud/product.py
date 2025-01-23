from app.crud.base import CRUDBase
from app.models.product import Product


class ProductCRUD(CRUDBase):
    """"""
    pass


product_crud = ProductCRUD(Product)

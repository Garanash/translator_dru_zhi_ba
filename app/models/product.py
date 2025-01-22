from sqlalchemy import Column, String, Text, Float, ForeignKey

from app.core.db import Base


class Product(Base):
    ''''''
    name = Column(String)
    info = Column(Text)
    price = Column(Float)
    category = Column(String, ForeignKey('category.id'))

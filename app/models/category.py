from sqlalchemy import Column, String, Text

from app.core.db import Base


class Category(Base):
    ''''''
    name = Column(String)
    description = Column(Text)

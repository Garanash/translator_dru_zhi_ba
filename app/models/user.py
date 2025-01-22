from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Text

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    language_prefered = Column(String)
    categories_prefered = Column(Text)
    legal_info = Column(Text)
    contacts = Column(Text)
    payment_method = Column(Text)

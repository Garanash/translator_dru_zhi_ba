from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    language_prefered: str
    categories_prefered: str
    legal_info: str
    contacts: str
    payment_method: str


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    language_prefered: str
    categories_prefered: str
    legal_info: str
    contacts: str
    payment_method: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
    language_prefered: str
    categories_prefered: str
    legal_info: str
    contacts: str
    payment_method: str

from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


async def create_category(
        new_item: CategoryCreate,
        session: AsyncSession
) -> Category:
    new_item_data = new_item.dict()
    db_category = Category(**new_item_data)
    session.add(db_category)
    await session.commit()
    await session.refresh(db_category)
    return db_category


async def read_all_categories_from_db(
        session: AsyncSession,
) -> list[Category]:
    db_category = await session.execute(select(Category))
    return db_category.scalars().all()


async def get_category_by_id(
        category_id: int,
        session: AsyncSession,
) -> Optional[Category]:
    db_category = await session.get(Category, category_id)
    return db_category


async def update_category(
        db_item: Category,
        item_in: CategoryUpdate,
        session: AsyncSession
) -> Category:
    obj_data = jsonable_encoder(db_item)
    update_data = item_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_item, field, update_data[field])
    session.add(db_item)
    await session.commit()
    await session.refresh(db_item)
    return db_item


async def delete_category(
        item: Category,
        session: AsyncSession
) -> Category:
    await session.delete(item)
    await session.commit()
    return item

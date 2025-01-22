from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


async def create_product(
        new_item: ProductCreate,
        session: AsyncSession
) -> Product:
    new_item_data = new_item.dict()
    db_product = Product(**new_item_data)
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return db_product


async def read_all_products_from_db(
        session: AsyncSession,
) -> list[Product]:
    db_product = await session.execute(select(Product))
    return db_product.scalars().all()


async def get_product_by_id(
        product_id: int,
        session: AsyncSession,
) -> Optional[Product]:
    db_product = await session.get(Product, product_id)
    return db_product


async def update_product(
        db_item: Product,
        item_in: ProductUpdate,
        session: AsyncSession
) -> Product:
    obj_data = jsonable_encoder(db_item)
    update_data = item_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_item, field, update_data[field])
    session.add(db_item)
    await session.commit()
    await session.refresh(db_item)
    return db_item


async def delete_product(
        item: Product,
        session: AsyncSession
) -> Product:
    await session.delete(item)
    await session.commit()
    return item

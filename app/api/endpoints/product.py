from typing import Annotated

from fastapi import APIRouter, Form, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.crud.product import product_crud
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductDB, ProductUpdate


router = APIRouter(prefix='/products', tags=['Товары'])


@router.post(
    '/create',
    response_model=ProductDB,
    )
async def create_new_product(
    product: Annotated[ProductCreate, Form()],
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    new_product = await product_crud.create(product, session)
    return new_product


@router.get(
    '/all_products',
    response_model=list[ProductDB]
)
async def get_all_products(
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    all_products = await product_crud.get_multi(session)
    return all_products


@router.patch(
    '/update',
    response_model=ProductDB,
    response_model_exclude_none=True,
)
async def update_product_in_db(
    product_id: int,
    obj_in: Annotated[ProductUpdate, Form()],
    session: AsyncSession = Depends(get_session)
):
    product = await check_product_exists(
        product_id, session
    )
    product = await product_crud.update(
        product, obj_in, session
    )
    return product


@router.delete(
    '/delete',
    response_model=ProductDB
)
async def delete_product_from_db(
    product_id: int,
    session: AsyncSession = Depends(get_session),
):
    product = await check_product_exists(
        product_id, session
    )
    product = await product_crud.remove(product, session)
    return product


async def check_product_exists(
    product_id: int,
    session: AsyncSession,
) -> Product:
    product = await product_crud.get(
        product_id, session
    )
    match product:
        case None:
            raise HTTPException(
                status_code=404,
                detail='Товар не найден!'
            )
    return product

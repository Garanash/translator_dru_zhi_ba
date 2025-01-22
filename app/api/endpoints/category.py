from typing import Annotated

from fastapi import APIRouter, Form, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.crud.category import (create_category, read_all_categories_from_db,
                               get_category_by_id,
                               update_category, delete_category)
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryDB, CategoryUpdate


router = APIRouter(prefix='/categories', tags=['Категории'])


@router.post(
    '/create',
    response_model=CategoryDB,
    )
async def create_new_metiz(
    category: Annotated[CategoryCreate, Form()],
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    new_category = await create_category(category, session)
    return new_category


@router.get(
    '/all_categories',
    response_model=list[CategoryDB]
)
async def get_all_metizes(
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    all_categories = await read_all_categories_from_db(session)
    return all_categories


@router.patch(
    '/update',
    response_model=CategoryDB,
    response_model_exclude_none=True,
)
async def update_category_in_db(
    category_id: int,
    obj_in: Annotated[CategoryUpdate, Form()],
    session: AsyncSession = Depends(get_session)
):
    category = await check_category_exists(
        category_id, session
    )
    category = await update_category(
        category, obj_in, session
    )
    return category


@router.delete(
    '/delete',
    response_model=CategoryDB
)
async def delete_category_from_db(
    category_id: int,
    session: AsyncSession = Depends(get_session),
):
    category = await check_category_exists(
        category_id, session
    )
    category = await delete_category(category, session)
    return category


async def check_category_exists(
    category_id: int,
    session: AsyncSession,
) -> Category:
    category = await get_category_by_id(
        category_id, session
    )
    match category:
        case None:
            raise HTTPException(
                status_code=404,
                detail='Категория не найдена!'
            )
    return category

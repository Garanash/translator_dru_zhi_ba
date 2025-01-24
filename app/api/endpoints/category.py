from typing import Annotated

from fastapi import APIRouter, Form, Depends, HTTPException, Query, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_session
from app.core.user import current_superuser
from app.crud.category import category_crud
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryDB, CategoryUpdate


router = APIRouter(prefix='/categories', tags=['Категории'])


@router.post(
    '/create',
    response_model=CategoryDB,
    dependencies=[Depends(current_superuser)],
    )
async def create_new_category(
    category: Annotated[CategoryCreate, Form()],
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    new_category = await category_crud.create(category, session)
    return new_category


@router.get(
    '/all_categories',
    response_model=list[CategoryDB]
)
async def get_all_categories(
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    all_categories = await category_crud.get_multi(session)
    return all_categories


@router.patch(
    '/update',
    response_model=CategoryDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def update_category_in_db(
    category_id: int,
    obj_in: Annotated[CategoryUpdate, Form()],
    session: AsyncSession = Depends(get_session)
):
    category = await check_category_exists(
        category_id, session
    )
    category = await category_crud.update(
        category, obj_in, session
    )
    return category


@router.delete(
    '/delete',
    response_model=CategoryDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_category_from_db(
    category_id: int,
    session: AsyncSession = Depends(get_session),
):
    category = await check_category_exists(
        category_id, session
    )
    category = await category_crud.remove(category, session)
    return category


@router.get(
    '/{category_id}',
    response_model=CategoryDB
)
async def search_products(
    search_field: str = Query(..., description="Field to search by"),
    search_term: str = Query(..., description="Term to search for"),
    session: AsyncSession = Depends(get_session),
):
    products = await category_crud.get_by_attribute(
        attr_name=search_field,
        attr_value=search_term,
        session=session,
    )
    return products


async def check_category_exists(
    category_id: int,
    session: AsyncSession,
) -> Category:
    category = await category_crud.get(
        category_id, session
    )
    match category:
        case None:
            raise HTTPException(
                status_code=404,
                detail='Категория не найдена!'
            )
    return category

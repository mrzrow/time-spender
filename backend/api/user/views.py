from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.user import crud
from backend.api.user.schemas import User, UserCreate
from backend.core.models import db_helper

router = APIRouter(tags=['Users'], prefix='/user')


@router.get('/', response_model=list[User])
async def get_users(
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_users(session=session)


@router.post('/', response_model=User)
async def create_user(
        user_in: UserCreate,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_user(session=session, user_in=user_in)


@router.get('/tg/{tg_id}/', response_model=User)
async def get_user_by_tg_id(
        tg_id: str,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    user = await crud.get_user_by_tg_id(session=session, tg_id=tg_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with {tg_id=} not found'
    )


@router.get('/{user_id}/', response_model=User)
async def get_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_user_by_id(session=session, user_id=user_id)

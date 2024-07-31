from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.event.schemas import EventCreate, Event
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


@router.get('/{user_id}/', response_model=User)
async def get_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_user_by_id(session=session, user_id=user_id)


@router.get('/{user_id}/event/', response_model=list[Event])
async def get_user_events(
        user_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_user_events(session=session, user_id=user_id)


@router.post('/{user_id}/event/', response_model=Event)
async def create_user_event(
        user_id: int,
        event_in: EventCreate,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_user_event(
        session=session,
        user_id=user_id,
        event_in=event_in
    )

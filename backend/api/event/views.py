from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.event import crud

from fastapi import APIRouter, Depends

from backend.api.event.schemas import Event, EventCreate
from backend.core.models import db_helper

router = APIRouter(tags=['Events'], prefix='/event')


@router.get('/{user_id}/', response_model=list[Event])
async def get_user_events(
        user_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_user_events(session=session, user_id=user_id)


@router.post('/{user_id}/', response_model=Event)
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

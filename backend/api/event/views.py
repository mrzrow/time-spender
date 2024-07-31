from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.event import crud

from fastapi import APIRouter, Depends

from .schemas import Event
from ...core.models import db_helper

router = APIRouter(tags=['Events'], prefix='/event')


@router.get('/{event_id}/', response_model=Event)
async def get_events_by_id(
        event_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_event_by_id(session=session, event_id=event_id)

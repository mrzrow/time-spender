from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.event.schemas import EventCreate
from backend.core.models import Event


async def get_user_events(
        session: AsyncSession,
        user_id: int
) -> list[Event]:
    req = (
        select(Event)
        .where(Event.user_id == user_id)
        .order_by(Event.date_start)
    )
    result: Result = await session.execute(req)
    events = result.scalars().all()
    return list(events)


async def create_user_event(
        session: AsyncSession,
        user_id: int,
        event_in: EventCreate
) -> Event:
    event = Event(user_id=user_id, **event_in.model_dump())
    session.add(event)
    await session.commit()
    return event

from sqlalchemy import select, DateTime, Result
from sqlalchemy.ext.asyncio import AsyncSession

from backend.api.event.schemas import EventCreate
from backend.api.user.schemas import UserCreate
from backend.core.models import User, Event


async def get_users(
        session: AsyncSession
) -> list[User]:
    req = select(User).order_by(User.id)
    result: Result = await session.execute(req)
    users = result.scalars().all()
    return list(users)


async def get_user_by_id(
        session: AsyncSession,
        user_id: int
) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_tg_id(
        session: AsyncSession,
        tg_id: str
) -> User | None:
    req = select(User).where(User.tg_id == tg_id)
    user: User | None = await session.scalar(req)
    return user


async def get_user_events(
        session: AsyncSession,
        user_id: int
) -> list[Event]:
    req = select(Event).where(Event.user_id == user_id).order_by(Event.date_start)
    result: Result = await session.execute(req)
    events = result.scalars().all()
    return list(events)


async def create_user(
        session: AsyncSession,
        user_in: UserCreate
) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def create_user_event(
        session: AsyncSession,
        user_id: int,
        event_in: EventCreate
) -> Event:
    event = Event(user_id=user_id, **event_in.model_dump())
    session.add(event)
    await session.commit()
    return event

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.api.user.schemas import UserCreate
from backend.core.models import User


async def get_users(
        session: AsyncSession
) -> list[User]:
    req = (
        select(User)
        .options(
            selectinload(User.events)
        )
        .order_by(User.id)
    )
    result: Result = await session.execute(req)
    users = result.scalars().all()
    return list(users)


async def get_user_by_id(
        session: AsyncSession,
        user_id: int
) -> User | None:
    req = (
        select(User)
        .options(
            selectinload(User.events)
        )
        .where(User.id == user_id)
    )
    user: User | None = await session.scalar(req)
    return user


async def get_user_by_tg_id(
        session: AsyncSession,
        tg_id: str
) -> User | None:
    req = (
        select(User)
        .options(
            selectinload(User.events)
        )
        .where(User.tg_id == tg_id)
    )
    user: User | None = await session.scalar(req)
    return user


async def create_user(
        session: AsyncSession,
        user_in: UserCreate
) -> User:
    req = (
        select(User)
        .options(
            selectinload(User.events)
        )
        .where(User.tg_id == user_in.tg_id)
    )
    user: User | None = await session.scalar(req)
    if user is None:
        user = User(**user_in.model_dump(), events=[])
        session.add(user)
        await session.commit()
    return user

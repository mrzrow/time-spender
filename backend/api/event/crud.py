from sqlalchemy.ext.asyncio import AsyncSession

from ...core.models import Event


async def get_event_by_id(
        session: AsyncSession,
        event_id: int
) -> Event | None:
    return await session.get(Event, event_id)

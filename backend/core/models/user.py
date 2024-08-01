from backend.core.models.base import Base

from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from backend.core.models.event import Event


class User(Base):
    tg_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    events: Mapped[list['Event']] = relationship(back_populates='user')

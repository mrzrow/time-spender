from backend.core.models.base import Base

from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from backend.core.models.user import User


class Event(Base):
    title: Mapped[str] = mapped_column(
        String(32),
        nullable=False
    )

    date_start: Mapped[datetime] = mapped_column(
        nullable=False
    )

    duration: Mapped[int] = mapped_column(
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'),
        unique=False,
        nullable=False
    )

    user: Mapped['User'] = relationship(
        'User',
        back_populates='events'
    )

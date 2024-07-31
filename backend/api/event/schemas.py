from typing import Annotated

from annotated_types import MaxLen
from pydantic import BaseModel, PastDatetime, Field, ConfigDict


class EventBase(BaseModel):
    title: Annotated[str, MaxLen(32)]
    date_start: PastDatetime
    duration: Annotated[int, Field(gt=0)]


class EventCreate(EventBase):
    pass


class Event(EventBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

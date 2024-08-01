from pydantic import BaseModel, ConfigDict

from backend.api.event.schemas import Event


class UserBase(BaseModel):
    tg_id: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    events: list[Event]

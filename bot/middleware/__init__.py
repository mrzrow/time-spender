__all__ = ['IsRegisteredMiddleware']

import aiohttp
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from bot.config import API_URL
from bot.utils.messages import msg_mw_register


class IsRegisteredMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{API_URL}/user/tg/{event.from_user.id}/') as rg:
                if (rg.status // 100) == 2:
                    user = await rg.json()
                    user_id = user['id']
                    await data['state'].update_data(user_id=user_id)
                    return await handler(event, data)
                return await event.answer(text=msg_mw_register)

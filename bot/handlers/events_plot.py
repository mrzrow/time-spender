from datetime import datetime

import aiohttp
from aiogram.enums import ParseMode
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext

from bot.config import API_URL, IMG_PATH
from bot.utils.messages import msg_plot_error
from bot.utils.utils import create_plot


async def h_plot(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = data['user_id']
    async with aiohttp.ClientSession() as session:
        async with session.get(
                url=f'{API_URL}/event/{user_id}/',
        ) as req:
            if (req.status // 100) != 2:
                await message.answer(
                    text=msg_plot_error,
                    parse_mode=ParseMode.MARKDOWN_V2
                )
                return await state.set_state('*')
            user_events = await req.json()
            user_events = [
                {
                    'title': event['title'],
                    'date_start': datetime.strptime(event['date_start'], '%Y-%m-%dT%H:%M:%S'),
                    'duration': event['duration']
                } for event in user_events
            ]
            create_plot(message.from_user.id, user_events)
            photo_path = f'{IMG_PATH}/{message.from_user.id}.png'
            await message.answer_photo(FSInputFile(photo_path))
            await state.set_state('*')


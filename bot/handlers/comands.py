import aiohttp

from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.config import API_URL
from bot.utils.messages import (msg_start, msg_help, msg_register_success, msg_register_error)


async def h_start(message: Message, state: FSMContext):
    await message.answer(
        text=msg_start,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await state.set_state('*')


async def h_help(message: Message, state: FSMContext):
    await message.answer(
        text=msg_help,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await state.set_state('*')


async def h_register(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=f'{API_URL}/user/',
            json={'tg_id': tg_id}
        ) as req:
            if (req.status // 100) == 2:
                await message.answer(
                    text=msg_register_success,
                    parse_mode=ParseMode.MARKDOWN_V2
                )
                return await state.set_state('*')
            await message.answer(
                text=msg_register_error,
                parse_mode=ParseMode.MARKDOWN_V2
            )
            await state.set_state('*')


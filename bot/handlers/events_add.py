import re
import aiohttp

from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.config import API_URL
from bot.utils.fsm import StateMachine
from bot.utils.messages import msg_add_title, msg_add_date, msg_add_date_error, msg_add_title_error, msg_add_duration, \
    msg_add_duration_error, msg_add_success, msg_add_error
from bot.utils.utils import conv_str_to_datetime, conv_str_to_seconds


async def h_add(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(
        text=msg_add_title,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await state.set_state(StateMachine.add_title)
    await state.update_data(**data)


async def h_add_title(message: Message, state: FSMContext):
    data = await state.update_data()
    title = message.text.strip().capitalize()
    if not title.isalnum():
        await message.answer(
            text=msg_add_title_error,
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return await state.set_state(StateMachine.add_title)
    await message.answer(
        text=msg_add_date,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await state.set_state(StateMachine.add_date)
    await state.update_data(title=title, **data)


async def h_add_date(message: Message, state: FSMContext):
    data = await state.get_data()
    date = message.text.strip()
    pattern = r'\[\d{4}-\d{2}-\d{2}\]\d{2}:\d{2}'
    if re.fullmatch(pattern, date) is None:
        await message.answer(
            text=msg_add_date_error,
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return await state.set_state(StateMachine.add_date)
    date = conv_str_to_datetime(date)
    await message.answer(
        text=msg_add_duration,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await state.set_state(StateMachine.add_duration)
    await state.update_data(date=date, **data)


async def h_add_duration(message: Message, state: FSMContext):
    data = await state.get_data()
    duration = message.text.strip()
    pattern = r'\d{2}:\d{2}'
    if re.fullmatch(pattern, duration) is None:
        await message.answer(
            text=msg_add_duration_error,
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return await state.set_state(StateMachine.add_duration)
    duration = conv_str_to_seconds(duration)
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=f'{API_URL}/event/{data["user_id"]}/',
            json={
                'title': data['title'],
                'date_start': data['date'],
                'duration': duration
            }
        ) as req:
            if (req.status // 100) == 2:
                await message.answer(
                    text=msg_add_success,
                    parse_mode=ParseMode.MARKDOWN_V2
                )
                return await state.set_state('*')
            await message.answer(
                text=msg_add_error,
                parse_mode=ParseMode.MARKDOWN_V2
            )
            await state.set_state('*')

from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.utils.messages import msg_start, msg_help


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

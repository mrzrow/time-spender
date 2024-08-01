import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import create_commands, register_commands


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    await bot.set_my_commands(commands=create_commands())

    register_commands(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

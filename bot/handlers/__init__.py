__all__ = (
    'create_commands',
    'register_commands'
)

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import BotCommand

from bot.handlers.comands import h_start, h_help


def create_commands():
    bot_commands = [
        ('start', 'Начать диалог с ботом'),
        ('help', 'Вывести справку о работе бота'),
        ('register', 'Зарегистрировать свой Telegram ID'),
        ('add', 'Добавить событие'),
        ('infograph', 'Вывести инфографику')
    ]
    return [BotCommand(command=cmd[0], description=cmd[1]) for cmd in bot_commands]


def register_commands(router: Router):
    router.message.register(h_start, Command(commands=['start']))
    router.message.register(h_help, Command(commands=['help']))

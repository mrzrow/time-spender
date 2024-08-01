__all__ = (
    'create_commands',
    'register_commands',
    'register_commands_add'
)

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import BotCommand

from bot.handlers.comands import h_start, h_help, h_register
from bot.handlers.events_add import h_add, h_add_title, h_add_date, h_add_duration
from bot.utils.fsm import StateMachine


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
    router.message.register(h_register, Command(commands=['register']))


def register_commands_add(router: Router):
    router.message.register(h_add, Command(commands=['add']))
    router.message.register(h_add_title, StateMachine.add_title)
    router.message.register(h_add_date, StateMachine.add_date)
    router.message.register(h_add_duration, StateMachine.add_duration)

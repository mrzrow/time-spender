__all__ = (
    'create_commands',
    'register_commands'
)

from aiogram import Router


def create_commands():
    bot_commands = [
        ('start', 'Начать диалог с ботом'),
        ('help', 'Вывести справку о работе бота'),
        ('register', 'Зарегистрировать свой Telegram ID'),
        ('add', 'Добавить событие'),
        ('infograph', 'Вывести инфографику')
    ]


def register_commands(router: Router):
    pass

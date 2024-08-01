from aiogram.fsm.state import StatesGroup, State


class StateMachine(StatesGroup):
    add_title = State()
    add_date = State()
    add_duration = State()

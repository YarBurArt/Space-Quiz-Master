from aiogram import types
from aiogram.fsm.state import State, StatesGroup

markup1 = types.KeyboardButton(text="Random fact")
startmenu = types.ReplyKeyboardMarkup(keyboard=[[markup1,],],resize_keyboard=True)

markup2 = types.KeyboardButton(text="Exit")
votemenu = types.ReplyKeyboardMarkup(keyboard=[[markup2],],resize_keyboard=True)


class QuestionnaireState(StatesGroup):
    step_1_start = State()  # start
    step_2_try = State()  # try
    step_3_exit = State()  # exit


async def setup_bot_commands(): # TODO
    bot_commands = [
        types.BotCommand(command="/help", description="Get info about me"),
        types.BotCommand(command="/start", description="start message"),
        types.BotCommand(command="/cancel", description="cancel quiz")
    ]
    await bot.set_my_commands(bot_commands)
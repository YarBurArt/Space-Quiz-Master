"""
Space Quiz Bot by yarburart
"""
import logging

from aiogram import types, Bot, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import (
        TOKEN, bcolors, 
        questions, HELPME,
        help_img_url,
        )
from rnd_img import get_img_with_descr

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize FSM storage
memory_storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=memory_storage)

startmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup1 = types.KeyboardButton("Random fact")
startmenu.add(markup1)

markup2 = types.KeyboardButton("Exit")
votemenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
votemenu.add(markup2)


class QuestionnaireState(StatesGroup):
    step_1 = State()  # start
    step_2 = State()  # try
    step_3 = State()  # exit


async def setup_bot_commands(): # TODO
    bot_commands = [
        types.BotCommand(command="/help", description="Get info about me"),
        types.BotCommand(command="/start", description="start message"),
        types.BotCommand(command="/cancel", description="cancel quiz")
    ]
    await bot.set_my_commands(bot_commands)


@dp.message_handler(commands=['start'])
async def startpg(message: types.Message, state: FSMContext):
    async with state.proxy() as data: # set random question key at start fsm
        data['random_key'] = random.choice(list(questions.keys()))

    await bot.send_photo(message.chat.id,
                         photo=questions[data['random_key']]["image"])
    await message.reply('Welcome to our bot! '
                        '\nYou will learn many interesting facts about space ', 
                        reply_markup=startmenu)
    await helppg(message)


@dp.message_handler(commands=['cancel'], state='*')
async def cancelpg(message: types.Message, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await message.reply('Exit from quiz',
                        reply_markup=startmenu)


@dp.message_handler(commands=['help'])
async def helppg(message: types.Message):
    await bot.send_video(message.chat.id, help_img_url, None, '...')
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELPME,
                           parse_mode="MarkdownV2")


@dp.message_handler(commands=['rndimg'])
async def rndimg(message: types.Message):
    msg = await message.answer("Search  . . . ")
    resj = await get_img_with_descr()
    await message.reply_photo(photo=resj['url'], 
                            caption=resj['title'])
    await message.answer('History / \n' + resj['explanation'])
    try:
        await msg.delete()
    except Exception as e:
        return 


@dp.message_handler(commands=['next'], state='*')
async def osnova_v1(message: types.Message, state: FSMContext):
    await osnova(message, state)


@dp.message_handler(text='Random fact')
async def osnova(message: types.Message, state: FSMContext):
    await message.reply(questions["quriosity_meaning"]["question"],
                        reply_markup=types.ReplyKeyboardRemove())  # types.ReplyKeyboardRemove() здесь нужен для того чтобы удалить reply_markup с надписью "Посмотреть анкету" от глаз пользывателя
    await QuestionnaireState.step_1.set()  


@dp.message_handler(state=QuestionnaireState.step_3)
async def exitpg(message: types.Message, state: FSMContext): 
    async with state.proxy() as data:
        random_key = data['random_key']
    logging.debug("%d ext start %d", bcolors.OKBLUE, bcolors.ENDC)
    await message.reply(questions[random_key]["explanation"],
                        reply_markup=startmenu)
    await state.finish()


@dp.message_handler(state=QuestionnaireState.step_2)
async def restart(message: types.Message, state: FSMContext):
    if message.text == "Exit":
        logging.debug(f"{bcolors.OKBLUE}ext restart{bcolors.ENDC}")
        await state.set_state(QuestionnaireState.step_3)
        await exitpg(message, state)
    else:
        await message.reply("Try it again",
                            reply_markup=types.ReplyKeyboardRemove())  
        # types.ReplyKeyboardRemove() здесь нужен для того чтобы удалить reply_markup 
        # с надписью "Посмотреть анкету" от глаз пользывателя
        await QuestionnaireState.step_1.set()


@dp.message_handler(state=QuestionnaireState.step_1, content_types=types.ContentTypes.TEXT)
async def questionnaire_state_1_message(message: types.Message, state: FSMContext):
    async with state.proxy() as user_data:
        user_data['name'] = message.text.replace('\n', ' ')
        random_key = user_data['random_key']
    # await message.reply(f"Ваше имя: {user_data['name']}")

    unique_key_words = set()
    for word in questions[random_key]["explanation"].lower().split():
        if word.isalpha() and len(word) >= 4:
            unique_key_words.add(word)

    if set(user_data['name'].lower().split()) <= unique_key_words:
        await message.reply("That's the right answer, " + 
                            questions[random_key]["explanation"]
                            , reply_markup=startmenu)
        await state.finish()  # Оканчиваем наш FSM опрос от пользывателя
    elif message.text.replace('\n', ' ') == "Exit": 
        await message.reply(questions[random_key]["explanation"]
                            , reply_markup=startmenu)
        await state.finish()  # Оканчиваем наш FSM опрос от пользывателя
    else:
        await message.reply("wrong answer", reply_markup=votemenu)
        await state.set_state(QuestionnaireState.step_2)
     

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

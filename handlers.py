import random
import logging
from aiogram import Router, types, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from rnd_img import get_img_with_descr
from handlers_helper import *
from config import questions, help_img_url, HELPME, bcolors

base_r = Router(name=__name__)

@base_r.message(Command('start'))
async def startpg(message: types.Message, state: FSMContext):
    # set random question key at start fsm
    await state.update_data({"random_key": random.choice(list(questions.keys()))})
    data = await state.get_data()
    await message.answer_photo(photo=questions[data['random_key']]["image"])
    await message.reply('Welcome to our bot! '
                        '\nYou will learn many interesting facts about space ', 
                        reply_markup=startmenu)
    await helppg(message)


@base_r.message(Command('cancel'), StateFilter(None))
async def cancelpg(message: types.Message, state: FSMContext):
    if state is None:
        return
    await state.clear()
    await message.reply('Exit from quiz',
                        reply_markup=startmenu)


@base_r.message(Command('help'))
async def helppg(message: types.Message):
    await message.answer_animation(animation=help_img_url, caption="...")
    await message.answer(text=HELPME, parse_mode="MarkdownV2")


@base_r.message(Command('rndimg'))
async def rndimg(message: types.Message):
    """ get random image via NASA API """
    msg = await message.answer("Search  . . . ")
    resj = await get_img_with_descr()
    await message.reply_photo(photo=resj['url'], 
                            caption=resj['title'])
    await message.answer('History / \n' + resj['explanation'])
    try:
        await msg.delete()
    except Exception as e:
        return 


@base_r.message(Command('next'), StateFilter(None))
async def osnova_v1(message: types.Message, state: FSMContext):
    await osnova(message, state)


@base_r.message(F.text=='Random fact')
async def osnova(message: types.Message, state: FSMContext):
    await message.reply(questions["quriosity_meaning"]["question"],
                        reply_markup=types.ReplyKeyboardRemove())  
    await state.set_state(QuestionnaireState.step_1_start) 


@base_r.message(QuestionnaireState.step_3_exit)
async def exitpg(message: types.Message, state: FSMContext): 
    state_data: dict = await state.get_data()
    random_key: str = state_data['random_key']
    logging.debug("%d ext start %d", bcolors.OKBLUE, bcolors.ENDC)
    await message.reply(questions[random_key]["explanation"],
                        reply_markup=startmenu)
    await state.clear()


@base_r.message(QuestionnaireState.step_2_try)
async def restart(message: types.Message, state: FSMContext):
    if message.text == "Exit":
        logging.debug(f"{bcolors.OKBLUE}ext restart{bcolors.ENDC}")
        await state.set_state(QuestionnaireState.step_3_exit)
        await exitpg(message, state)
    else:
        await message.reply("Try it again",
            reply_markup=types.ReplyKeyboardRemove())  
        await state.set_state(QuestionnaireState.step_1_start)


@base_r.message(QuestionnaireState.step_1_start)
async def questionnaire_state_1_message(message: types.Message, state: FSMContext):
    """ check answer and show explanation, then restart """
    await state.update_data({"name": (message.text or "nasa").replace('\n', ' ')})
    data = await state.get_data()
    random_key = data['random_key'] # key that already get from db/config 

    # collect key words from config, without meaningless 
    unique_key_words = set(
        word for word in questions[random_key]["explanation"].lower().split()
        if len(word) >= 4)

    # well, it works for 2 sentences about the same mission
    if set(data['name'].lower().split()) <= unique_key_words: 
        await message.reply("That's the right answer, " + 
                            questions[random_key]["explanation"]
                            , reply_markup=startmenu)
        await state.clear()  # Оканчиваем наш FSM опрос от пользывателя
    elif (message.text or "Exit").replace('\n', ' ') == "Exit": 
        await message.reply(questions[random_key]["explanation"]
                            , reply_markup=startmenu)
        await state.clear()  # Оканчиваем наш FSM опрос от пользывателя
    else:
        await message.reply("wrong answer", reply_markup=votemenu)
        await state.set_state(QuestionnaireState.step_2_try)

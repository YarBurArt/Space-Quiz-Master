"""
Space Quiz Bot by yarburart
"""
import asyncio
import logging
import sys

from aiogram import types, Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import base_r
from config import (
        TOKEN, bcolors, 
        questions, HELPME,
        help_img_url,
        )


# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize FSM storage
memory_storage = MemoryStorage()
     
async def main() -> None:
    bot = Bot(TOKEN)
    dp = Dispatcher(bot, storage=memory_storage)
    db.include_routes(base_r)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
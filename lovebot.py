from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart
from handlers.user_private import user_private_router
import asyncio
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())


bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(user_private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

print('LoveBot запущен!')

asyncio.run(main())
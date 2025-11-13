import os
from dotenv import load_dotenv

import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=telegram_token)
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__== "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exits')
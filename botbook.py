from aiogram import Bot, Dispatcher
import asyncio
from app.handlers import router

API_TOKEN = "7812472136:AAGawLkKxHVsPsEs1mutu-CKoPLveFiPr1A"

async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os, asyncio
from handlers import work, video_conv


async def main():
    dp = Dispatcher()
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp.include_routers(video_conv.router, work.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
import asyncio
import logging
from aiogram import Bot, Dispatcher
import handlers

from CONFIG import TOKEN

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
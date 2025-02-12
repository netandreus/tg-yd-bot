import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import BOT_TOKEN
from app.middlewares.access import AccessMiddleware
from app.handlers import get_handlers_router


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(get_handlers_router())
    dp.message.middleware(AccessMiddleware())

    logging.info("Starting bot...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    logging.info("Bot stopped.")


if __name__ == "__main__":
    asyncio.run(main())

def start():
    asyncio.run(main())  # Ensures execution inside an event loop
import logging
import asyncio
from typing import NoReturn

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import BOT_TOKEN
from app.middlewares.access import AccessMiddleware
from app.handlers import get_handlers_router


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )


async def setup_bot() -> tuple[Bot, Dispatcher]:
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(get_handlers_router())
    dp.message.middleware(AccessMiddleware())

    return bot, dp


async def main() -> NoReturn:
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        logger.info("Starting bot...")
        bot, dp = await setup_bot()
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot stopped due to error: {e}")
        raise
    finally:
        logger.info("Bot stopped.")


def start() -> None:
    """Entry point for running the bot."""
    asyncio.run(main())


if __name__ == "__main__":
    start()
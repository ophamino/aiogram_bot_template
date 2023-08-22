import logging
import asyncio

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage

from middlewares import ThrottlingMiddleware

from settings import load_settings


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    
    settings = load_settings()
    storage = RedisStorage() if settings.tg_bot.use_redis else MemoryStorage()
    
    bot = Bot(token=settings.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=storage)

    dp.message.middleware(ThrottlingMiddleware())
    
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.INFO("Bot is stopped")

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from handlers.menu_handlers import set_main_menu

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='{filename}:{lineno} {levelname:8}'
               '[{asctime}] - {name} {message}',
        style='{'
    )
    logger.info('Starting bot')
    
    config: Config = load_config()
    
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    dp.startup.register(set_main_menu)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
from aiogram import Bot
from aiogram.types import BotCommand

from config_data.config import Config, load_config
from lexicon.lexicon_ru import LEXICON_RU

config: Config = load_config()

bot = Bot(token= config.tg_bot.token)

async def set_main_menu(bot: Bot):
    main_menu_command = [
        BotCommand(command='/help',
                   description=LEXICON_RU['/help']),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Способ связи 89*********'),
        BotCommand(command='/payemts',
                   description='Платежи')
    ]
    await bot.set_my_commands(main_menu_command)
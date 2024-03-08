from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.client.session.aiohttp import AiohttpSession

import pytz

from app.dbms import DBMS, create_db
from app.config_reader import load_config


config = load_config("config/bot.ini")

# session = AiohttpSession(proxy="")
bot = Bot(token=config.bot.TOKEN, parse_mode="HTML")  # , session=session)
dp = Dispatcher(storage=MemoryStorage())

create_db(config.base.dbname)
BotDB = DBMS(
	config.base.dbname, config.base.user, config.base.host, config.base.port, local_tz
)

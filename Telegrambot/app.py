import logging
from vendor import Settings
from aiogram import (
    Bot,
    Dispatcher,
    executor,
)
from db.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


logging.basicConfig(level=logging.INFO)

engine = create_engine(Settings.DB_CONN) 
meta = Base.metadata
session = Session(engine)

bot = Bot(token=Settings.API_TOKEN)
dp = Dispatcher(bot)


import routes


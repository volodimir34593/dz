import logging
from vendor import Settings
from aiogram import Bot, Dispatcher, executor, types
from db.base import Base
from db.models import Product
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from aiogram.types import ParseMode 
engine = create_engine("postgresql+psycopg2:///internet_shop", echo=True) #/acuta@internet_shop
Base.metadata.create_all(engine)
session = Session(engine)


logging.basicConfig(level=logging.INFO)


bot = Bot(token=Settings.API_TOKEN)
dp = Dispatcher(bot)

# Що повинен вміти бот:
# 1) Привітатись та видати список з таблицями;
# 2) Вивести список записів таблиці "Товари" із бази даних;

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    
@dp.message_handler(commands=['tables'])
async def send_table_names(message: types.Message):
    #select table_name from information_schema.tables where table_schema = 'public'
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")    

@dp.message_handler(commands=['products'])
async def send_product_list(message: types.Message):
    #SELECT * FROM public.products ORDER BY id ASC 
    stmt = select(Product)
    reply_text = '<code>' + ' '.join([str(x) for x in session.scalars(stmt)])
    reply_text += '</code>'
    # for product in session.scalars(stmt):
    #     print(product)
    await message.reply(reply_text, parse_mode=ParseMode.HTML)    
    
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
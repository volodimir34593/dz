from app import dp, meta, session
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery
)
from sqlalchemy import select
from db.models import Product


@dp.message_handler(commands=["start"])
async def send_welcome(message: Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=["tables"])
async def send_table_names(message: Message):
    markup = InlineKeyboardMarkup(row_width=2)
    tables = meta.tables
    for table in tables:
        kbtn = InlineKeyboardButton(
            text=str(table).capitalize(),
            callback_data=str(table),
        )
        markup.add(kbtn)
    await message.reply("Вітання! Виберіть таблицю для роботи", reply_markup=markup)


@dp.message_handler(commands=["products"])
async def send_product_list(message: Message):
    products = select(Product).order_by(Product.id)
    products = " ".join([str(x) for x in session.scalars(products)])

    await message.reply(f"Products: {products}")


@dp.callback_query_handler(lambda callb: callb.data == "products")
async def send_products(callb: CallbackQuery):
    products = select(Product).order_by(Product.id)
    products = " ".join([str(x) for x in session.scalars(products)])

    await callb.message.reply(f"Products: {products}")
# bot.py

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram import executor
import sqlite3

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'  # Потрібно отримати токен від BotFather

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

DATABASE_NAME = 'users.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, first_name, last_name):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, first_name, last_name) VALUES (?, ?, ?)',
                   (username, first_name, last_name))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT username, first_name, last_name FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! Я бот для роботи з користувачами. Введіть /add_user для додавання нового користувача або /get_users для виведення списку користувачів.")

@dp.message_handler(commands=['add_user'])
async def add_user_command(message: types.Message):
    await message.reply("Введіть дані нового користувача у форматі: username first_name last_name")
    # Очікуємо введення в форматі: username first_name last_name
    await bot.register_next_step_handler(message, process_add_user_step)

async def process_add_user_step(message: types.Message):
    try:
        username, first_name, last_name = message.text.split()
        add_user(username, first_name, last_name)
        await message.reply(f"Користувач {username} успішно доданий до бази даних!")
    except Exception as e:
        await message.reply(f"Помилка при додаванні користувача. Перевірте формат введених даних.")

@dp.message_handler(commands=['get_users'])
async def get_users_command(message: types.Message):
    users = get_users()
    if users:
        user_list = "\n".join([f"@{username} - {first_name} {last_name}" for username, first_name, last_name in users])
        await message.reply(f"Список користувачів:\n{user_list}", parse_mode=ParseMode.MARKDOWN)
    else:
        await message.reply("Немає жодного користувача в базі даних.")

if __name__ == '__main__':
    create_table()
    executor.start_polling(dp, skip_updates=True)

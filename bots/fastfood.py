from telegram.utils import helpers

from telegram import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Update, 
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    Update
)
from telegram.ext import (
    Updater, 
    CommandHandler, 
    CallbackQueryHandler, 
    CallbackContext, 
    CallbackContext
)

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
                    )

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
        update.message.reply_text("Вас вітає бот Macmini\n /help - Команди")


def pizza(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Бургер", callback_data='11'),InlineKeyboardButton("з Говядиною", callback_data='55')],
        [InlineKeyboardButton("Хотдог", callback_data='33'),InlineKeyboardButton("Баварська сосиска", callback_data='44')],
        [InlineKeyboardButton("Піцца", callback_data='22')],
        [InlineKeyboardButton("Індивідуальне замовлення", callback_data='88 ')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Виберіть Фаст фуд:', reply_markup=reply_markup)


def give_data(update: Update, context: CallbackContext) -> None:
    keyboard_r = [
        [
            KeyboardButton("Номер ☎️", request_contact=True),
            KeyboardButton("Локация 🗺️", request_location=True),
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard_r)
    update.message.reply_text("Будь ласка дайте мені свої дані для замовлення!🤠", reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    
    query = update.callback_query

    keyboard_16p = [
        [InlineKeyboardButton("📏Бургер -💵Цена - 60грн", callback_data='111')],
        [InlineKeyboardButton("📏Хотдог -💵Цена - 80грн", callback_data='222')],
        [InlineKeyboardButton("📏Піцца -💵Цена - 120грн", callback_data='333')]]

    reply_markup_16p = InlineKeyboardMarkup(keyboard_16p)

    query.answer()
    print(query.data)


    if query.data == '11':
        query.edit_message_text(text=f"Виберіть Ваше замовлення", reply_markup=reply_markup_16p)
    elif query.data == '22':
        query.edit_message_text(text=f"Виберіть Ваше замовлення", reply_markup=reply_markup_16p)
    elif query.data == '33':
        query.edit_message_text(text=f"Виберіть Ваше замовлення", reply_markup=reply_markup_16p)
    elif query.data == '44':
        query.edit_message_text(text=f"Виберіть Ваше замовлення", reply_markup=reply_markup_16p)
    elif query.data == '55':
        query.edit_message_text(text=f"Виберіть Ваше замовлення", reply_markup=reply_markup_16p)
    elif query.data == '8':
        query.edit_message_text(text=f"Введіть свій номер☎️\n І ми передзвонимо Вам протягом 5 хвилин\n /give_data")
    elif query.data == '1':
        query.edit_message_text(text=f"Введіть свій номер і ми Вам передзвонимо!- /give_data")
    elif query.data == '111':
        query.edit_message_text(text=f"Надішліть мені свої дані ☎️ 🗺️\n Спец команда - /give_data")
    elif query.data == '222':
        query.edit_message_text(text=f"Надішліть мені свої дані ☎️ 🗺️\n Спец команда - /give_data")
    elif query.data == '333':
        query.edit_message_text(text=f"Надішліть мені свої дані ☎️ 🗺️\n Спец команда - /give_data")

    else:
        query.edit_message_text(text=f"Ссилка на оплату замовлення")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("/call - Для того что бы позвонить нам\n /sale - акиции\n /friend - приведи друга отримай знижку10%\n /pizza- для вибору фаст фуда\n /give_data - поділись своїми даними")


def call_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Ось мій номер телефону: +380735422797\n Звони !😏\n Я завжди відповім!🤙")


def sale_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("✅Купляючи 3 бургера 2 бургера в подарунок!\n ✅Купи сьогодні фаст фуд!\n ✅Завтра для всіх відвідувачів Macmini напої безкоштовно, за умови купівлі великої склянки!")


def friend_command(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.username)
    text = "Ось твоя силка:\n\n" + url
    update.message.reply_text(text)


def info(context: CallbackContext) -> None:
    job = context.job
    context.bot.send_message(job.context, text='Купи 3 отримай 2 безкоштовно!')


def main() -> None:
    updater = Updater("5607439064:AAE7_M0aS8TzQlQ5QGsZMbtWgoUSgNdJNko")
    a = updater.dispatcher.add_handler
    a(CommandHandler('start', start))
    a(CommandHandler( 'pizza',pizza))
    a(CallbackQueryHandler(button))
    a(CommandHandler('help', help_command))
    a(CommandHandler('call', call_command))
    a(CommandHandler('sale', sale_command))
    a(CommandHandler('friend', friend_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
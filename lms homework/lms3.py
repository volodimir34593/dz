from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# Функція для обробки команди /start та відправлення reply-клавіатури
def start(update, context):
    user_id = update.message.from_user.id
    reply_markup = ReplyKeyboardMarkup([['Хочу подивитись фільм', 'Хочу послухати музику']], one_time_keyboard=True)
    context.bot.send_message(chat_id=user_id, text='Виберіть бажання:', reply_markup=reply_markup)

# Функція для обробки текстового повідомлення з reply-клавіатурою
def handle_text(update, context):
    user_id = update.message.from_user.id
    text = update.message.text

    if text == 'Хочу подивитись фільм':
        # Inline-клавіатура для фільмів
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton('Рекомендації для фільмів', callback_data='movies')]
        ])
        context.bot.send_message(chat_id=user_id, text='Оберіть опцію для фільмів:', reply_markup=inline_keyboard)
    elif text == 'Хочу послухати музику':
        # Inline-клавіатура для музики
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton('Рекомендації для музики', callback_data='music')]
        ])
        context.bot.send_message(chat_id=user_id, text='Оберіть опцію для музики:', reply_markup=inline_keyboard)

# Функція для обробки inline-клавіатури
def handle_inline_keyboard(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    option = query.data

    if option == 'movies':
        context.bot.send_message(chat_id=user_id, text='Ось рекомендації для фільмів:\n1. [Фільм 1](посилання_на_фільм1)\n2. [Фільм 2](посилання_на_фільм2)')
    elif option == 'music':
        context.bot.send_message(chat_id=user_id, text='Ось рекомендації для музики:\n1. [Пісня 1](посилання_на_пісню1)\n2. [Пісня 2](посилання_на_пісню2)')

def main():
    updater = Updater('YOUR_BOT_TOKEN', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    dp.add_handler(CallbackQueryHandler(handle_inline_keyboard))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

# Стани для машини станів
START, QUESTION_1, QUESTION_2, END = range(4)

# Клавіатура для варіантів відповідей
reply_keyboard = [['Відповідь 1', 'Відповідь 2'],
                  ['Відповідь 3', 'Відповідь 4']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

# Початок роботи з ботом
def start(update, context):
    user = update.message.from_user
    update.message.reply_text(
        f"Привіт, {user.first_name}! Я запитатиму в тебе кілька питань. Вибери відповідь на клавіатурі.",
        reply_markup=markup,
    )
    return QUESTION_1

# Обробка відповідей на питання
def question(update, context):
    user = update.message.from_user
    text = update.message.text

    # Тут ви можете обробити вибір відповіді та взяти наступне питання
    # У цьому прикладі переходимо до наступного питання або завершаємо тест

    if context.user_data.get('answers') is None:
        context.user_data['answers'] = []

    context.user_data['answers'].append(text)

    if len(context.user_data['answers']) == 1:
        update.message.reply_text("Гарно! Тепер обери іншу відповідь.", reply_markup=markup)
        return QUESTION_2
    else:
        update.message.reply_text("Дякую за відповіді! Тест завершено.")
        return END

# Завершення роботи з ботом
def end(update, context):
    user = update.message.from_user
    answers = context.user_data['answers']
    update.message.reply_text(f"Дякую за твої відповіді: {', '.join(answers)}", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
    # Ініціалізація бота
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Створення машини станів для обробки питань
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            QUESTION_1: [MessageHandler(Filters.text & ~Filters.command, question)],
            QUESTION_2: [MessageHandler(Filters.text & ~Filters.command, question)],
            END: [MessageHandler(Filters.text & ~Filters.command, end)],
        },
        fallbacks=[],
        allow_reentry=True
    )

    dp.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

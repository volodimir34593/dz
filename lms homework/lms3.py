from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функція для обробки повідомлень
def handle_messages(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text.lower()

    if "доброго ранку" in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Доброго ранку, чим будеш снідати?')

# Функція для обробки команди /saysomething
def saysomething(update: Update, context: CallbackContext) -> None:
    # Ваша логіка для генерації цитати тут
    quote = "Життя - це те, що трапляється, поки ви зайняті планами."

    context.bot.send_message(chat_id=update.effective_chat.id, text=quote)

def main():
    # Встановлення токену бота
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    # Отримання об'єкта розподілювача
    dp = updater.dispatcher

    # Додавання обробників повідомлень та команд
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_messages))
    dp.add_handler(CommandHandler("saysomething", saysomething))

    # Запуск бота
    updater.start_polling()

    # Бот працює до зупинки вручну
    updater.idle()

if __name__ == '__main__':
    main()

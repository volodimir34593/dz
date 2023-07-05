import telebot

bot = telebot.TeleBot('5820764624:AAHsk3Gtqe2iwrsElH6a7bTekkxJwVgKozc')

# ... ваші обробники команд і функції бота ...

# Функція для зупинки бота
def stop_bot():
    bot.stop_polling()

# Запускаємо бота
bot.polling()

# Для зупинки бота програмно викличте функцію stop_bot()
stop_bot()
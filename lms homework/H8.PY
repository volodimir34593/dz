import random

class MoodBot:
    def __init__(self):
        self.mood = 'neutral'
        self.responses = {
            'greeting': ['Привіт!', 'Привіт-привіт!', 'Вітаю вас!'],
            'farewell': ['До побачення!', 'Бувайте!', 'До зустрічі!'],
            'neutral': ['Цікаво...', 'Добре.', 'Не зовсім зрозуміло.'],
            'happy': ['Вибільшений настрій! 😄', 'Супер, що ви так веселі!', 'Радію за вас!'],
            'sad': ['Сумно чути...', 'Як можна допомогти?', 'Сподіваюсь, що ви скоро почуєтеся краще.']
        }

    def set_mood(self, mood):
        self.mood = mood

    def get_response(self, user_input):
        if 'привіт' in user_input.lower():
            return random.choice(self.responses['greeting'])
        elif 'до побачення' in user_input.lower():
            return random.choice(self.responses['farewell'])
        elif 'настрій' in user_input.lower():
            return f"Ваш поточний настрій: {self.mood.capitalize()}."
        elif 'встановити настрій' in user_input.lower():
            parts = user_input.lower().split()
            if len(parts) >= 3:
                new_mood = parts[2]
                if new_mood in ['neutral', 'happy', 'sad']:
                    self.set_mood(new_mood)
                    return f"Настрій встановлено на {new_mood.capitalize()}."
                else:
                    return "Неправильний настрій. Доступні варіанти: neutral, happy, sad."
            else:
                return "Будь ласка, введіть настрій, наприклад: 'встановити настрій радісний'."
        else:
            return random.choice(self.responses[self.mood])


# Приклад використання:

mood_bot = MoodBot()

while True:
    user_input = input("Введіть ваше повідомлення: ")
    if user_input.lower() == 'вийти':
        print("Дякую за розмову! До побачення!")
        break
    else:
        response = mood_bot.get_response(user_input)
        print("Бот:", response)

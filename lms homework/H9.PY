class UserRegistrationStateMachine:
    def __init__(self):
        self.state = 'start'
        self.user_data = {'ім’я': None, 'електронна_пошта': None, 'вік': None}

    def start(self):
        print("Ласкаво просимо! Виберіть дію:")
        print("1. Реєстрація нового користувача")
        print("2. Змінити дані користувача")
        print("3. Вийти")

        choice = input("Ваш вибір: ")
        if choice == '1':
            self.state = 'registration'
        elif choice == '2':
            self.state = 'edit'
        elif choice == '3':
            print("До побачення!")
            exit()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    def registration(self):
        print("Реєстрація нового користувача:")
        name = input("Введіть ім’я: ")
        email = input("Введіть електронну пошту: ")
        age = input("Введіть вік: ")

        self.user_data['ім’я'] = name
        self.user_data['електронна_пошта'] = email
        self.user_data['вік'] = age

        print("Реєстрація успішна!")
        self.state = 'start'

    def edit(self):
        print("Редагування даних користувача:")
        print(f"Поточні дані: {self.user_data}")
        field_to_edit = input("Введіть поле для редагування (ім’я, електронна_пошта, вік): ").lower()

        if field_to_edit in self.user_data:
            new_value = input(f"Введіть нове значення для {field_to_edit}: ")
            self.user_data[field_to_edit] = new_value
            print("Дані змінено успішно!")
        else:
            print("Невірне поле для редагування. Спробуйте ще раз.")

        self.state = 'start'

    def run(self):
        while True:
            if self.state == 'start':
                self.start()
            elif self.state == 'registration':
                self.registration()
            elif self.state == 'edit':
                self.edit()


# Приклад використання:

registration_machine = UserRegistrationStateMachine()
registration_machine.run()

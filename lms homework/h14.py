import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('toys.db')
cursor = conn.cursor()

# Створення таблиці "toys"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS toys (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT,
        price REAL,
        stock_quantity INTEGER
    )
''')

# Вставка даних
toys_data = [
    ('Teddy Bear', 'Stuffed Animal', 15.99, 20),
    ('Doll', 'Plush', 18.50, 15),
    ('Toy Car', 'Soft Toy', 12.99, 25),
    ('Penguin', 'Stuffed Animal', 9.99, 12),
]

cursor.executemany('INSERT INTO toys (name, type, price, stock_quantity) VALUES (?, ?, ?, ?)', toys_data)

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()
# Підключення до бази даних
conn = sqlite3.connect('toys.db')
cursor = conn.cursor()

# Запит SELECT для виведення всіх імен м'яких іграшок
cursor.execute('SELECT name FROM toys')
all_toy_names = cursor.fetchall()
print("Всі імена м'яких іграшок:", all_toy_names)

# Запит SELECT для виведення імен та цін м'яких іграшок, де ціна менше 20
cursor.execute('SELECT name, price FROM toys WHERE price < 20')
affordable_toys = cursor.fetchall()
print("Імена та ціни м'яких іграшок, де ціна менше 20:", affordable_toys)

# Запит SELECT для виведення типів м'яких іграшок та загальної кількості товарів кожного типу
cursor.execute('SELECT type, SUM(stock_quantity) FROM toys GROUP BY type')
toy_types_quantity = cursor.fetchall()
print("Типи м'яких іграшок та загальна кількість товарів кожного типу:", toy_types_quantity)

# Запит SELECT для виведення імен та кількості на складі м'яких іграшок, де кількість на складі менше 10
cursor.execute('SELECT name, stock_quantity FROM toys WHERE stock_quantity < 10')
low_stock_toys = cursor.fetchall()
print("Імена та кількість на складі м'яких іграшок, де кількість на складі менше 10:", low_stock_toys)

# Видалення м'якої іграшки, де кількість на складі менше або дорівнює 0
cursor.execute('DELETE FROM toys WHERE stock_quantity <= 0')

# Оновлення кількості на складі для одного з товарів (наприклад, збільшення на 5 одиниць)
cursor.execute('UPDATE toys SET stock_quantity = stock_quantity + 5 WHERE name = "Teddy Bear"')

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()


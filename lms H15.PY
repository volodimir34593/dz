import sqlite3

# З'єднання з базою даних (SQLite)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# 1. Вибір імен користувачів з електронною адресою в домені "gmail.com"
cursor.execute("SELECT name FROM users WHERE email LIKE '%@gmail.com%'")
result_1 = cursor.fetchall()
print("1. Імена користувачів з gmail.com:", result_1)

# 2. Вибір м'яких іграшок, відсортованих за спаданням ціни
cursor.execute("SELECT * FROM toys WHERE category = 'soft' ORDER BY price DESC")
result_2 = cursor.fetchall()
print("2. М'які іграшки за спаданням ціни:", result_2)

# 3. Знайдення кількості замовлень для кожної м'якої іграшки
cursor.execute("""
    SELECT toy_name, COUNT(order_id) AS order_count
    FROM orders
    JOIN toys ON orders.toy_id = toys.toy_id
    WHERE toys.category = 'soft'
    GROUP BY toys.toy_id, toy_name
""")
result_3 = cursor.fetchall()
print("3. Кількість замовлень для м'яких іграшок:", result_3)

# ... і так далі ...

# Закриття з'єднання з базою даних
conn.close()

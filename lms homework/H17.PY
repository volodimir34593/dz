import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Приклад оновлення даних користувача (замість 'your_query' введіть свій SQL-запит)
update_query = 'UPDATE users SET column_name = new_value WHERE condition;'
cursor.execute(update_query)
conn.commit()

# Приклад вибірки імен користувачів, які зробили замовлення на суму більше 1000 грн
select_query = "SELECT name FROM users WHERE user_id IN (SELECT user_id FROM orders WHERE total_amount > 1000);"
cursor.execute(select_query)
result = cursor.fetchall()

# Виведення результатів
print(result)

# Закриття з'єднання
conn.close()

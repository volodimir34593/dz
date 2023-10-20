import sqlite3

# Підключення до бази даних (або створення нової, якщо вона не існує)
conn = sqlite3.connect("subjects.db")
cursor = conn.cursor()

# Створення таблиці subjects
cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id_subject INTEGER PRIMARY KEY,
        subject_name TEXT,
        subject_description TEXT,
        hours INTEGER,
        semester_number INTEGER
    )
''')

# Додавання даних до таблиці
subjects_data = [
    (1, 'Math', 'Mathematics Course', 60, 1),
    (2, 'Physics', 'Physics Course', 45, 2),
    (3, 'Biology', 'Biology Course', 30, 1),
    (4, 'Chemistry', 'Chemistry Course', 50, 2),
    (5, 'History', 'History Course', 40, 1),
    (6, 'Computer Science', 'Programming Basics', 75, 2),
    (7, 'English', 'English Language Course', 50, 1),
    (8, 'Art', 'Art and Design', 30, 2)
]

cursor.executemany('''
    INSERT INTO subjects (id_subject, subject_name, subject_description, hours, semester_number)
    VALUES (?, ?, ?, ?, ?)
''', subjects_data)

# Збереження змін та закриття підключення
conn.commit()
conn.close()

# Читання даних з колонок subject_name, semester_number
conn = sqlite3.connect("subjects.db")
cursor = conn.cursor()

cursor.execute('SELECT subject_name, semester_number FROM subjects')
data = cursor.fetchall()

# Виведення результатів
print("Дані з колонок subject_name, semester_number:")
for row in data:
    print(f"Subject: {row[0]}, Semester: {row[1]}")

# Закриття підключення
conn.close()


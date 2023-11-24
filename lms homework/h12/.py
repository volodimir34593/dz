import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Створення таблиці працівників
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL
    )
''')

# Створення таблиці пацієнтів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        dob DATE NOT NULL,
        gender TEXT NOT NULL
    )
''')

# Створення таблиці візитів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS visits (
        visit_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        employee_id INTEGER,
        visit_date DATE NOT NULL,
        diagnosis TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
''')

# Створення таблиці записів до лікарів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        employee_id INTEGER,
        appointment_date DATE NOT NULL,
        notes TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
''')

# Створення таблиці рецептів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS prescriptions (
        prescription_id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        employee_id INTEGER,
        prescription_date DATE NOT NULL,
        medication TEXT NOT NULL,
        dosage TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
''')

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()

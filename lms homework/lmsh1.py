import pandas as pd
import matplotlib.pyplot as plt

# Створення DataFrame для зберігання оцінок
data = {'Дата': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'],
        'Оцінка': [90, 85, 92, 88]}

df = pd.DataFrame(data)
df['Дата'] = pd.to_datetime(df['Дата'])

# Вивід інформації про DataFrame
print(df)

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(df['Дата'], df['Оцінка'], marker='o')
plt.title('Динаміка оцінок')
plt.xlabel('Дата')
plt.ylabel('Оцінка')
plt.grid(True)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Створити дані
data = {
    'Місяці': ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень'],
    'Години навчання': [50, 45, 55, 60, 70],
    'Години хобі': [20, 25, 15, 10, 5]
}

# Створити DataFrame зі стовпцями
df = pd.DataFrame(data)

# Зберегти DataFrame у форматі Excel
excel_path = 'дані.xlsx'
df.to_excel(excel_path, index=False)

# Побудувати стовпчасту діаграму
plt.figure(figsize=(10, 6))
plt.bar(df['Місяці'], df['Години навчання'], label='Навчання')
plt.bar(df['Місяці'], df['Години хобі'], label='Хобі', bottom=df['Години навчання'])
plt.xlabel('Місяці')
plt.ylabel('Години')
plt.title('Години навчання та хобі за місяцями')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Зберегти графік у файл
plot_path = 'графік.png'
plt.savefig(plot_path)

plt.show()

print(f'Аркуш з даними збережено у файлі: {excel_path}')
print(f'Графік збережено у файлі: {plot_path}')

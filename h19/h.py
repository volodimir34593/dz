import pandas as pd
from datetime import datetime, timedelta

# Створити список дат
dates = [datetime.now() + timedelta(days=i) for i in range(4)]

# Створити DataFrame зі списком дат
df = pd.DataFrame({'Дата': dates})

# Зберегти DataFrame у форматі Excel
excel_path = 'дати.xlsx'
df.to_excel(excel_path, index=False)

print(f'Аркуш з датами збережено у файлі: {excel_path}')

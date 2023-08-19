from bs4 import BeautifulSoup

# Ваш HTML-код
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Мій HTML-файл</title>
</head>
<body>
    <!-- Ваша HTML-структура тут -->
</body>
</html>
"""

# Створюємо об'єкт BeautifulSoup для парсингу
soup = BeautifulSoup(html_content, 'html.parser')

# Отримуємо дані з заголовків та класів
headings = soup.find_all(['h1', 'h2'])  # Знайдемо всі h1 та h2 заголовки
classes = soup.find_all(class_=True)    # Знайдемо всі елементи з класами

# Виведемо знайдені дані
print("Заголовки:")
for heading in headings:
    print(heading.text)

print("\nКласи:")
for element in classes:
    print(element['class'])

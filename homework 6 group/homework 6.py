with open('data.txt', 'w') as f:
    f.write('Hello, world!\n')
    f.write('This is some data.\n')
    f.write('It can be anything.\n')

# читання файлу та запис до нового файлу
with open('data.txt', 'r') as f1, open('new_data.txt', 'w') as f2:
    data = f1.read()
    f2.write(data)

# виведення даних на екран
with open('new_data.txt', 'r') as f:
    print(f.read())
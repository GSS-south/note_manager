# Обработка ошибок
try:
    with open('test_file.txt', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    file = open('test_file.txt', 'w', encoding='utf-8')
    print('Файл example.txt не найден. Создан новый файл.')
except UnicodeDecodeError:
    print('Ошибка при чтении файла test_file.txt. Проверьте его содержимое.')
except PermissionError:
    print('Ошибка при работе с файлом test_file.txt. Нет прав доступа')
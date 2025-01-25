# Импорт модуля
import json
# Заметка json
note = [
            {
            "username": "Алексей",
            "title": "Список покупок",
            "content": "Купить продукты",
            "status": "новая",
            "created_date": "27-11-2024",
            "issue_date": "30-11-2024"
            }
        ]
# Заметка для перезаписи и добавления python/txt
notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
           'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}]

# Заметка для добавления python/txt
new_notes = [{"username": "Мария",
              "title": "План работы",
              "content": "Подготовить отчёт",
              "status": "в процессе",
              "created_date": "27-11-2024",
              "issue_date": "28-11-2024"}]
# Функция для перезаписи данных из notes в файл
def save_notes_to_file(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as filename:
            for note in notes:
                filename.write(f'Имя пользователя: {note['username']}\n')
                filename.write(f'Заголовок: {note['title']}\n')
                filename.write(f'Описание: {note['content']}\n')
                filename.write(f'Статус: {note['status']}\n')
                filename.write(f'Дата создания: {note['created_date']}\n')
                filename.write(f'Дедлайн: {note['issue_date']}\n')
                filename.write('--\n')
                break
    except PermissionError:
        print('Ошибка доступа')
    except Exception as inform:
        print(f'Произошла ошибка: {inform}')
save_notes_to_file(notes, "notes.txt")

# Функция для возврата списка словарей из файла txt
def load_notes_from_file(filename):

    notes = []
    try:
        file = open(filename, encoding='utf-8')
        note = file.read().split('\n')[:-1]
# Делаем переменную глобальной, чтобы избежать ошибки Unboundlocalerror:
        global dict
        dict = dict()
# Перебираем каждый элемент и разбиваем ":"
        for item in note:
            key = item.split(':')[0]
            value = item.split(': ')[1:]
            dict[key] = str(*value)
# Изменяем имена ключей
        dict['username'] = dict.pop('Имя пользователя')
        dict['title'] = dict.pop('Заголовок')
        dict['content'] = dict.pop('Описание')
        dict['status'] = dict.pop('Статус')
        dict['created_date'] = dict.pop('Дата создания')
        dict['issue_date'] = dict.pop('Дедлайн')
        notes.append(dict)
        file.close()
        print(dict)
    except FileNotFoundError:
        file = open(filename, 'w')
        print('Файл не найден. Создан новый файл.')
    except UnicodeDecodeError:
        print('Ошибка при чтении файла filename. Проверьте его содержимое.')
    except PermissionError:
        print('Ошибка доступа')
    except Exception as inform:
        print(f'Произошла ошибка: {inform}')
load_notes_from_file('notes.txt')
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

try:
    notes = load_notes_from_file("corrupted_file.txt")
except Exception as e:
    print(f"Ошибка: {e}")

# Функция для добавления новых заметок в файл
def append_notes_to_file(new_notes, filename):
    try:
        with open(filename, 'a', encoding='utf-8') as filename:
            for note in new_notes:
                filename.write(f'Имя пользователя: {note['username']}\n')
                filename.write(f'Заголовок: {note['title']}\n')
                filename.write(f'Описание: {note['content']}\n')
                filename.write(f'Статус: {note['status']}\n')
                filename.write(f'Дата создания: {note['created_date']}\n')
                filename.write(f'Дедлайн: {note['issue_date']}\n')
                filename.write('--\n')
                break
    except PermissionError:
        print('Ошибка доступа')
    except Exception as inform:
        print(f'Произошла ошибка: {inform}')
append_notes_to_file(new_notes, "notes.txt")

# Функция для сохранения заметки в формате JSON
def save_notes_json(notes, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, indent=4, ensure_ascii=False)
    except Exception as inform:
        print(f'Произошла ошибка: {inform}')
save_notes_json(note, 'notes.json')
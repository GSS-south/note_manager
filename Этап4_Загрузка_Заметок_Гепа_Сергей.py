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

load_notes_from_file('filename.txt')

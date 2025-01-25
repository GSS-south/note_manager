# Переменные


# Заметка
notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
           'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}]
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
# Вызов функции
save_notes_to_file(notes, 'filename.txt')
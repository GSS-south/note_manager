# Переменные
username = 'Имя пользователя'
title = 'Заголовок заметки'
content = 'Содержание заметки'
status = 'Статус'
created_date = 'Дата создания'
issue_date = 'Дедлайн'
# Заметки
notes = [{username: 'Алексей', title: 'Список покупок', content: 'Купить продукты на неделю',
           status: 'новая', created_date: '27-11-2024', issue_date: '30-11-2024'},
          {username: 'Мария', title: 'Учеба', content: 'Подготовиться к экзамену',
           status: 'в процессе', created_date: '25-11-2024', issue_date: '01-12-2024'},
          {username: 'Иван', title: 'План работы', content: 'Завершить проект',
           status: 'выполнено', created_date: '20-11-2024', issue_date: '26-11-2024'}]
# Функция для поиска заметок
def search_notes_(notes, keyword = None, status = None):
    # Список, который берет существующие заметки
    search_notes = notes
    # Поиск по ключевым словам с нечувствительностью к регистру
    if keyword:
        keyword = keyword.lower()
        search_notes = [i for i in notes if keyword == i[title].lower()
                        or keyword == i[content].lower()
                        or keyword == i[username].lower()]
    # Поиск по статусу
    if status:
        status = status.lower()
        search_notes = [i for i in notes if status == i[status].lower()]

    if not notes:
        print('Заметки не найдены.')
    # Вывод найденной заметки
    else:
        print('\nВот что мы нашли:')
        for i in search_notes:
            for key, val in i.items():
                print(key, ':', val)
        print()
# Функция для выбора формата поиска
def search_():

    while True:
        if not notes:
            print('У вас нет заметок')
            break
        print('Выберите формат поиска. \n1 - поиск по ключевому слову заметки. \n2 - поиск по статусу заметки. '
              '\n3 - поиск по ключевому слову и статусу заметки.')
        answer_ = input('Введите номер формата поиска (1, 2, 3): ')
        if answer_ == '1':
            search_notes_(notes, keyword = input('\nВведите ключевое слово: '))
        elif answer_ == '2':
            search_notes_(notes, status = input('\nВведите статус: '))
        elif answer_ == '3':
            search_notes_(notes, keyword = input('\nВведите ключевое слово: '), status = input('Введите статус: '))
        else:
            print('Не корректно введены данные для поиска.')

from colorama import *
init(autoreset=True)
import datetime
from itertools import islice

username = 'Имя пользователя'
title = 'Заголовок заметки'
content = 'Содержание заметки'
status = 'Статус'
created_date = 'Дата создания'
issue_date = 'Дедлайн'


def create_note():
# Ввод данных в заметку для каждого ключа: Имя, Заголовок, Содержание, Статус, Дата создания и Дедлайн.
# Проверка на пустой ввод каждого ключа
    username = input("Введите ваше имя: ")
    if len(username.split()) == 0:
        while len(username.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            username = input("Введите ваше имя: ")
    title = input("Введите заголовок: ")
    if len(title.split()) == 0:
        while len(title.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            title = input("Введите заголовок: ")
    content = input("Введите описание заметки: ")
    if len(content.split()) == 0:
        while len(content.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            content = input("Введите описание заметки: ")
# Выбор статуса заметки
    print("Выберите статус заметки:")
    print("1 Выполнено")
    print("2 В процессе")
    print("3 Отложено")
# Ввод статуса заметки
    while True:
        i = input("Введите выбранный вами статус: ")
        if i.lower() in ['1', 'выполнено']:
            status = "Выполнено"
            print("Статус заметки успешно обновлён на: Выполнено")
            break
        elif i.lower() in ['2', 'в процессе']:
            status = "В процессе"
            print("Статус заметки успешно обновлён на: В процессе")
            break
        elif i.lower() in ['3', 'отложено']:
            status = "Отложено"
            print("Статус заметки успешно обновлён на: Отложено")
            break
        else:
            print(input("Выбрано не существующее значение, нажмите Enter и попробуйте снова."))
# Дата создания - текущая дата из библиотеки datetime
    create_date = datetime.datetime.now().strftime('%d-%m-%Y')
    issue_date = input("Введите дату дедлайна (день-месяц-год 15-01-2024): ")
# Цикл для правильности ввода даты
    while True:
        try:
            date = datetime.datetime.strptime(issue_date, '%d-%m-%Y')
        except ValueError:
            try:
                date = datetime.datetime.strptime(issue_date, '%d/%m/%Y')
            except ValueError:
                issue_date = input(
                    "Введен не верный формат даты. \nПопробуйте ещё раз (день-месяц-год 15-01-2024): ")
                continue
        break

# Меняем / на - для единого формата при выводе
    issue_date = issue_date.replace('/', '-')
    note = {'Имя пользователя': username,
              'Заголовок': title,
              'Содержание': content,
              'Статус': status,
              'Дата создания': create_date,
              'Дедлайн': issue_date}
    print("Заметка создана: ", note)
    return note

# Функция для отображения заметок и уникального номера начиная с 1
def print_notes():
    itr = 1
    for note in notes:
        print('\nЗаметка №' + str(itr) + '\n', end = '')
        itr = itr + 1
        for key, val in note.items():
            print(key, ':', val)
    print()

# Функция для вывода всей информации из заметок
def display_notes(notes):
    if len(notes) == 0:
        print(Back.BLACK + 'У вас нет сохранённых заметок.' + Style.RESET_ALL)
    else:
        itr = 1
        print(Fore.LIGHTYELLOW_EX + '\nСписок заметок:')
        for note in notes:
            print('----------')
            print(Back.BLACK + 'Заметка №' + str(itr) + Style.RESET_ALL + '\n', end='')
            itr = itr + 1
            for key, val in note.items():
                print(Fore.CYAN + key, ':', Fore.LIGHTBLUE_EX + val)
        print('----------')


# Функция для частичного вывода информации из заметок islice(i.items(),0,2)
def display_notes_min(notes):
    if len(notes) == 0:
        print(Back.BLACK + 'У вас нет сохранённых заметок.' + Style.RESET_ALL)
    else:
        itr = 1
        print(Fore.LIGHTYELLOW_EX + '\nСписок заметок:')
        for note in notes:
            print('----------')
            print(Back.BLACK + 'Заметка №' + str(itr) + Style.RESET_ALL + '\n', end='')
            itr = itr + 1
            for key, val in islice(note.items(),0,2):
                print(Fore.CYAN + key, ':', Fore.LIGHTBLUE_EX + val)
        print('----------')

# Выбор функции по формату отображения
def format_notes():
    print('Выберите формат просмотра данных. \n 1 - все данные о заметках \n 2 - краткая информация(Имя, Заголовок)')
    while True:
        notes_format = input('Ваш ответ: ')
        if notes_format == '1':
            display_notes(notes)
            break
        elif notes_format == '2':
            display_notes_min(notes)
            break
        else:
            print('Выбран не существующий ответ, попробуйте снова.')

def update_note(note):
    print('Текущие данные заметки:')
    print(note)
    print('Вы можете обновить данные полей (Имя пользователя, Заголовок, Содержание, Статус, Дедлайн).')
# Цикл для изменения данных, с проверкой на правильность ввода
    while True:
# Переменная для ключа
        update_a = input('\nВыберите данные для обновления и введите(Имя пользователя, Заголовок, Содержание, Статус,'
                         ' Дедлайн): ')
        if update_a not in note:
            print('Вы ввели не корректные данные, попробуйте снова.')
            continue
        if update_a == 'Дедлайн':
            issue_date = input("Введите дату дедлайна (день-месяц-год 15-01-2024): ")
# Цикл для правильности ввода даты
            while True:
                try:
                    date = datetime.datetime.strptime(issue_date, '%d-%m-%Y')
                    break
                except ValueError:
                    try:
                        date = datetime.datetime.strptime(issue_date, '%d/%m/%Y')
                        break
                    except ValueError:
                        issue_date = input(
                            "Введен не верный формат даты. \nПопробуйте ещё раз (день-месяц-год 15-01-2024): ")
                        continue
# Меняем / на - для единого формата при выводе
            issue_date = issue_date.replace('/', '-')
# Цикл для подтверждения изменения даты
            while True:
                f = input('Вы уверены, что хотите обновить поле? (да/нет): ')
                if f.lower() in ['да']:
                    note[update_a] = issue_date
                    print('Данные обновлены:\n', note)
                    break
                elif f.lower() in ['нет']:
                    print('Ваша заметка:\n', note)
                    break
                else:
                    print('Выбрано не существующее значение, попробуйте снова.')
                    continue
            break
        if update_a == 'Имя пользователя' or update_a == 'Заголовок' or update_a == 'Содержание' or update_a == 'Статус':
# Переменная для значения
            update_b = input('Введите новые данные: ')
# Цикл для подтверждения изменения
            while True:
                g = input('Вы уверены, что хотите обновить поле? (да/нет): ')
                if g.lower() in ['да']:
                    note[update_a] = update_b
                    print('Данные обновлены:\n', note)
                    return note
                elif g.lower() in ['нет']:
                    print('Ваша заметка:\n', note)
                    break
                else:
                    print('Выбрано не существующее значение, нажмите Enter и попробуйте снова.')
                    continue

def delete_note():
# Цикля для удаления заметки по имени пользователя или заголовку
    while True:
        i = input("Желаете удалить заметку? да/нет: ")
        if i in ["нет"]:
            print("Ваши заметки:")
            break
        elif i in ["да"]:
            print("Хорошо.")
            deleted_note = input("\nВведите имя пользователя или заголовок для удаления заметки: ")
            for note in range(0, len(notes)):
                if (deleted_note.lower() == notes[note]['Имя пользователя'].lower()
                        or deleted_note.lower() == notes[note]['Заголовок'].lower()):
                    notes.pop(note)
                    print('\nОставшиеся заметки:')
                    display_notes(notes)
                    break
                else:
                    print("Заметка не найдена, попробуйте снова.")
        else:
            print("Некорректный ответ, попробуйте снова: ")
    display_notes(notes)
    # Проверка на наполненность списка, при отсутсвии заметок выводится соответствующее сообщение
    if len(notes) == 0:
        print("Заметок больше не осталось.")

# Функция для поиска заметок
def search_notes_(notes, keyword = None, status = None):
    # Список, который берет существующие заметки
    search_notes = notes
    # Поиск по ключевым словам с нечувствительностью к регистру
    if keyword:
        keyword = keyword.lower()
        search_notes = [i for i in notes if keyword == i['Заголовок'].lower()
                        or keyword == i['Содержание'].lower()
                        or keyword == i['Имя пользователя'].lower()]
    # Поиск по статусу
    if status:
        status = status.lower()
        search_notes = [i for i in notes if status == i[status].lower()]

    if not notes:
        print('Заметки не найдены.')
    # Вывод найденной заметки
    else:
        print('----------')
        print(Fore.LIGHTYELLOW_EX + '\nВот что мы нашли:')
        for i in search_notes:
            for key, val in i.items():
                print(Fore.CYAN + key, ':', Fore.LIGHTBLUE_EX + val)
        print('----------')
        return menu()
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

notes = []
# Функция меню
def menu():
    while True:
        print(Fore.CYAN + 'Меню: '
              '\n1. Создать новую заметку '
              '\n2. Показать все заметки '
              '\n3. Обновить заметку '
              '\n4. Удалить заметку '
              '\n5. Найти заметку '
              '\n6. Выйти из программы')
        answer = input(Fore.CYAN + 'Введите выбранный вами ответ: ')
        if answer == '1':
            note = create_note()
            notes.append(note)
        elif answer == '2':
            format_notes()
        elif answer == '3':
            if notes:
                display_notes(notes)
                index = int(input('Введитете номер заметки для обновления: ')) - 1
                if 0 <= index < len(notes):
                    notes[index] = update_note(notes[index])
                else:
                    print('Не верный номер заметки.')
            else:
                print('Список заметок пуст.')
        elif answer == '4':
            delete_note()
        elif answer == '5':
            search_()
        elif answer == '6':
            print(Fore.CYAN + '\nПрограмма завершена. Спасибо за использование!')
            break
        else:
            print(Fore.CYAN + '\nНеверный выбор. Пожалуйста, выберите действие из списка.')
menu()
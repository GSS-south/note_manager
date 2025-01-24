# Цветовая библиотека
from colorama import *
init(autoreset=True)
# Библиотека datetime
import datetime
# Импорт функции islice из модуля itertools в Python
# Функция islice позволяет извлечь определённые элементы из итератора,
# указав диапазон элементов для извлечения.
from itertools import islice
# Переменные
username = 'Имя пользователя'
title = 'Заголовок заметки'
content = 'Содержание заметки'
status = 'Статус'
created_date = 'Дата создания'
issue_date = 'Дедлайн'
# Заметки
notes = [{username: 'Алексей', title: 'Список покупок', content: 'Купить продукты на неделю', status: 'Новая',
        created_date: '27-11-2024', issue_date: '30-11-2024'},
         {username: 'Мария', title: 'Учеба', content: 'Подготовиться к экзамену', status: 'В процессе',
          created_date: '25-11-2024', issue_date: '01-12-2024'},
         {username: 'Иван', title: 'План работы', content: 'Завершить проект', status: 'Выполнено',
          created_date: '20-11-2024', issue_date: '26-11-2024'}]

# Функция для вывода всей информации из заметок
def display_notes(notes):
    if len(notes) == 0:
        print(Back.BLACK + 'У вас нет сохранённых заметок.' + Style.RESET_ALL)
    else:
        itr = 1
        print(Fore.LIGHTYELLOW_EX + '\nСписок заметок:')
        for i in notes:
            print('----------')
            print(Back.BLACK + 'Заметка №' + str(itr) + Style.RESET_ALL + '\n', end='')
            itr = itr + 1
            for key, val in i.items():
                print(Fore.CYAN + key, ':', Fore.LIGHTBLUE_EX + val)
        print('----------')

# Функция для частичного вывода информации из заметок islice(i.items(),0,2)
def display_notes_min(notes):
    if len(notes) == 0:
        print(Back.BLACK + 'У вас нет сохранённых заметок.' + Style.RESET_ALL)
    else:
        itr = 1
        print(Fore.LIGHTYELLOW_EX + '\nСписок заметок:')
        for i in notes:
            print('----------')
            print(Back.BLACK + 'Заметка №' + str(itr) + Style.RESET_ALL + '\n', end='')
            itr = itr + 1
            for key, val in islice(i.items(),0,2):
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
        if notes_format == '2':
            display_notes_min(notes)
            break
format_notes()
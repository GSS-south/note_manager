# Импорт библиотек и функций
from colorama import *
init(autoreset=True)
import datetime
from itertools import islice
from create_note_function import create_note
from display_notes import display_notes
from display_notes import display_notes_min
from display_notes import format_notes
from update_note_function import update_note
from delete_note import delete_note
from search_notes import search_notes_
from search_notes import search_



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
            create_note()
        elif answer == '2':
            format_notes()
        elif answer == '3':
            update_note()
        elif answer == '4':
            delete_note()
        elif answer == '5':
            search_()
        elif answer == '6':
            print(Fore.CYAN + '\nПрограмма завершена. Спасибо за использование!')
            break
        else:
            print(Fore.CYAN + '\nНеверный выбор. Пожалуйста, выберите действие из списка.')

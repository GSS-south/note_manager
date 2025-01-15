# Программа для добавления и удаления заметок
import datetime

# Функция для отображения заметок и индекса начиная с 1
def print_notes():
    itr = 1
    for i in notes:
        print('\nЗаметка №' + str(itr) + '\n', end = '')
        itr = itr + 1
        for key, val in i.items():
            print(key, ':', val)
    print()


username = "Имя пользователя"
title = "Заголовок заметки"
content = "Содержание заметки"
status = "Статус"
created_date = "Дата создания"
issue_date = "Дедлайн"

notes = []
titles = []

# Цикл добавления заметок
while True:
# Ввод имя пользователя и проверка на пустую строку
    username = input("\nВведите имя пользователя: ")
# Проверка на пустой ввод
    if len(username.split()) == 0:
        while len(username.split()) == 0:
            print("Вы ничего не ввели. Попробуйте снова")
            username = input("Введите имя пользователя: ")
    while True:
        title = input("Введите заголовок:  ")
        print("Вы можете добавить несколько залоговков. Что бы закончить напишите 'стоп': ")
        # Условие для завершения
        if title.lower() == 'стоп':
            break
# Предотвращение пустого ввода
        if len(title.split()) == 0:
            print("\nВы ввели пустую строку, попробуйте ещё раз")
            continue
        else:
            titles.append(title)
    # Определяем уникальность
    titl = set(titles)
    if titles == titl:
        print("Все заголовки уникальны")
    else:
        print("Есть одинаковые заголовки")
    title = titles
# Ввод имя пользователя и проверка на пустую строку
    content = input("\nВведите описание заметки: ")
# Проверка на пустой ввод
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
# Дата создания - текущая дата, импортируемая из библиотеки
    create_date = datetime.datetime.now().strftime('%d-%m-%Y')
    while True:
        try:
            issue_date = datetime.datetime.strptime(
                input("Введите дату дедлайна (в формате день-месяц-год: 28-12-2023): "), '%d-%m-%Y')
            break
        except ValueError:
            print("Введен не верный формат даты, попробуйте снова")
        if create_date == issue_date:
            print("Дедлайн Сегодня!")
        elif create_date > issue_date:
            print("Время вышло.")
        else:
            days_ = issue_date - create_date
            print("Дней осталось: ", days_.days)
# Сохранение заметки
    note1 = {"Имя пользователя": username,
             "Заголовок заметки": title,
             "Содержание": content,
             "Статус": status,
             "Дата создания": create_date,
             "Дедлайн": issue_date.strftime('%d-%m-%Y')}
    notes.append(note1)
# Добавление заметки в том же цикле
    note2 = input("Хотите добавить ещё одну заметку? Ответ да или нет: ")
    if note2.lower() in ["нет"]:
        print("Оставим все ваши заметки ниже.")
        break
    elif note2.lower() in ["да"]:
        print("Продолжим.")
    else:
        print("Некорректный ответ, попробуйте снова: ")
# Вывод заметок с функцией def для оформления
print_notes()
# Цикл удаления созданных заметок по имени или заголовку
while True:
    i = input("Желаете удалить заметку? да/нет: ")
    if i in ["нет"]:
        print("Ваши заметки:")
        break
    elif i in ["да"]:
        print("Хорошо.")
        deleted_note = input("\nВведите имя пользователя или заголовок для удаления заметки: ")
        for j in range(0, len(notes)):
            if deleted_note.lower() == notes[j][username].lower() or deleted_note.lower() == notes[j][
                title].lower():
                notes.pop(j)
                print('\nОставшиеся заметки:')
                print_notes()
                break
            else:
                print("Заметка не найдена, попробуйте снова.")
    else:
        print("Некорректный ответ, попробуйте снова: ")
# Проверка на наполненность списка, при отсутсвии заметок выводится соответствующее сообщение
if len(notes) == 0:
    print("Заметок больше не осталось.")
else:
    print("Ваши заметки:")
print_notes()

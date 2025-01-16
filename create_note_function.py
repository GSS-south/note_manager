import datetime
# Функция для создания заметки
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
    note_1 = {'username': username, 'titles': title, 'content': content, 'status': status,
             'created_date': create_date,
             'issue_date': issue_date}
    print("Заметка создана: ", note_1)
# Вызов функции
create_note()
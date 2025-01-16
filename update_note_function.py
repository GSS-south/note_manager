import datetime

# Текущая заметка
note = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
        'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
# Функция
def update_note():
    print('Текущие данные заметки:')
    print(note)
    print('Вы можете обновить данные полей (username, title, content, status, issue_date).')
# Цикл для изменения данных, с проверкой на правильность ввода
    while True:
# Переменная для ключа
        update_a = input('\nВыберите данные для обновления и введите(username, title, content, status, issue_date): ')
        if update_a not in note:
            print('Вы ввели не корректные данные, попробуйте снова.')
            continue
        break
    if update_a == 'issue_date':
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


# Переменная для значения
    update_b = input('Введите новые данные: ')
# Цикл для подтверждения изменения
    while True:
        g = input('Вы уверены, что хотите обновить поле? (да/нет): ')
        if g.lower() in ['да']:
            note[update_a] = update_b
            print('Данные обновлены:\n', note)
            break
        elif g.lower() in ['нет']:
            print('Ваша заметка:\n', note)
            break
        else:
            print('Выбрано не существующее значение, нажмите Enter и попробуйте снова.')
            continue
# Вывод функции
update_note()
# Цикл для повторного обновления данных с последующим выводом функции update_note
while True:
    ff = input('Хотите продолжить обновление данных? (да/нет): ')
    if ff.lower() in ['да']:
        update_note()
    else:
        print('Ваша заметка:\n', note)
        break


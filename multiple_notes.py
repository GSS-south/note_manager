# Используем библиотеку, что бы узнать текущую дату
import datetime
# Переменные
username = "Имя пользователя"
title = "Заголовок заметки"
content = "Содержание заметки"
status = "Статус"
notes = []
print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
while True:
# Вводим данные для создания заметки
    username = input("Введите ваше имя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    print("Для изменения статуса выберите соответствующее значение:")
    print("1 Выполнено")
    print("2 В процессе")
    print("3 Отложено")
# Выбор статуса
    while True:
        i_ = input("Введите выбранный вами статус: ")
        if i_.lower() in ['1', 'выполнено']:
            print("Статус заметки успешно обновлён на: Выполнено")
            break
        elif i_.lower() in ['2', 'в процессе']:
            print("Статус заметки успешно обновлён на: В процессе")
            break
        elif i_.lower() in ['3', 'отложено']:
            print("Статус заметки успешно обновлён на: Отложено")
            break
        else:
            print(input("Выбрано не существующее значение, нажмите Enter и попробуйте снова."))
# Текущая дата
    create_date = datetime.datetime.now().strftime('%d-%m-%Y')
    print("Дата создания: ",datetime.datetime.now().strftime('%d-%m-%Y'))
# Проверка правильности ввода
    while True:
        try:
            issue_date = datetime.datetime.strptime(
                input("Введите дату дедлайна (в формате день-месяц-год: 28-12-2023): "), '%d-%m-%Y')
            break
        except ValueError:
            print("Введен не верный формат даты, попробуйте снова")
# Добавление готовой заметки в список
    note1 = {"Имя пользователя": username,
              "Название заметки": title,
              "Содержание": content,
              "Статус": status,
              "Дата создания": create_date,
              "Дедлайн": issue_date.strftime('%d-%m-%Y')}
    notes.append(note1)
# Можем добавить еще заметки либо завершить ввод
    note2 = input("Хотите добавить ещё одну заметку? Ответ да или нет: ")
    if note2.lower() in ["нет"]:
        print("Оставим все ваши заметки ниже.")
        break
    elif note2.lower() in ["да"]:
        print("Продолжим.")
    else:
        print("Некорректный ответ, попробуйте снова: ")
# Функция для отображения номера заметок по индексу
def print_():
    itr = 1
    for i in notes:
        print('\nЗаметка №' + str(itr)  + '\n', end = '')
        itr = itr + 1
        for key, val in i.items():
            print(key, ':', val)
    print()

print_()
# Удаление заметки по индексу
while True:
    i = input("Желаете удалить заметку? да/нет: ").lower()
    if i in ["нет"]:
        print("Ваши заметки:")
        break
    elif i in ["да"]:
        print("Хорошо.")
        i_ = input("Введите номер заметки: ")
        print("Готово.")
        i_ = int(i_) - 1
        deleted_note = notes.pop(int(i_))
    else:
        print("Некорректный ответ, попробуйте снова: ")

print_()



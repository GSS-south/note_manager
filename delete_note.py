# Переменные
username = "Имя пользователя"
title = "Заголовок заметки"
content = "Содержание заметки"
status = "Статус"
created_date = "Дата создания"
issue_date = "Дедлайн"
# Заметки
notes = [{username: "Алексей", title: "Список продуктов", content: "Купить продукты на неделю", status: "В процессе",
          created_date: "10-10-1010", issue_date: "10-10-1010"},
         {username: "Мария", title: "Учеба", content: "Подготовиться к экзамену", status: "Отложено",
          created_date: "10-10-1010", issue_date: "10-10-1010"}]
# Функция для отображения заметок и индекса начиная с 1
def print_notes():
    itr = 1
    for i in notes:
        print('\nЗаметка №' + str(itr) + '\n', end='')
        itr = itr + 1
        for key, val in i.items():
            print(key, ':', val)
    print()
print_notes()
# Цикля для удаления заметки по имени пользователя или заголовку
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
print_notes()
# Проверка на наполненность списка, при отсутсвии заметок выводится соответствующее сообщение
if len(notes) == 0:
    print("Заметок больше не осталось.")

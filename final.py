# Список информации заметки
username = "Имя пользователя"
title = "Заголовок заметки"
content = "Содержание заметки"
status = "Статус"
created_date = "17.12.2024"
issue_date = "17.01.2025"

# Данные от пользователя
username = input ("Введите имя пользователя ")
title = input ("Введите заголовок заметки ")
content = input ("Введите содержание заметки ")
status = input ("Введите статус заметки ")
created_date = input ('Введите дату создания заметки в формате "дд-мм-гггг" ')
issue_date = input ('Введите дату завершения заметки в формате "дд-мм-гггг" ')
changed_date = input('Введите дату изменения заметки в формате "дд-мм-гггг" ')
temp_created_date = created_date [0:5]
temp_issue_date = issue_date [0:5]

# Заголовки
title_1 = input("Введите заголовок 1 ")
title_2 = input("Введите заголовок 2 ")
titles = [title_1, title_2,]

# Полученные данные
note = [  "Имя пользователя: ", username,
        "Содержание заметки: ", content,
                    "Статус: ", status,
             "Дата создания: ", created_date,
            "Дата изменения: ", changed_date,
        [title_1, title_2]]
print(note)


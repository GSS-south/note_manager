username = input ("Введите имя пользователя ")
title = input ("Введите заголовок заметки ")
content = input ("Введите содержание заметки ")
status = input ("Введите статус заметки ")
created_date = input ('Введите дату создания заметки в формате "дд-мм-гггг" ')
issue_date = input ('Введите дату завершения заметки в формате "дд-мм-гггг" ')
changed_date = input('Введите дату изменения заметки в формате "дд-мм-гггг" ')
temp_created_date = created_date [0:5]
temp_issue_date = issue_date [0:5]
title_1 = input("Введите заголовок 1 ")
title_2 = input("Введите заголовок 2 ")
titles = [title_1, title_2,]

note = [  "Имя пользователя: ", username,
        "Содержание заметки: ", content,
                    "Статус: ", status,
             "Дата создания: ", created_date,
            "Дата изменения: ", changed_date,
        [title_1, title_2]]
print(note)


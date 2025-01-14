# Используем библиотеку, что бы узнать текущую дату
import datetime
create_date = datetime.datetime.now()
# Текущая дата
print("Дата создания: ", datetime.datetime.now().strftime('%d-%m-%Y'))
while True:
# Проверка правильности ввода
    try:
        issue_date = datetime.datetime.strptime(input("Введите дату дедлайна (в формате день-месяц-год: 28-12-2023): "), '%d-%m-%Y')
        break
    except ValueError:
        print("Введен не верный формат даты, попробуйте снова")
# Проверка дедлайна
if create_date.day == issue_date.day and create_date.month == issue_date.month and create_date.year == issue_date.year:
    print("Дедлайн Сегодня!")
elif create_date > issue_date:
    print("Время вышло.")
else:
    days_ = issue_date - create_date
    print("Дней осталось: ", days_.days)

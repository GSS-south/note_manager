# Список заголовков
titles = []
# Цикл для введения заголовков
while True:
    title = input("Введите заголовок ")
    print("Нажмите 'Enter', что бы закончить ")
    titles.append(title)
# Условие для завершения
    if title == "":
        break
# Убираем пустое значение
titles.remove("")
# Определяем уникальность
titl = set(titles)
if titles == titl:
    print("Все заголовки уникальны")
else:
    print("Есть одинаковые заголовки")
print(titles)


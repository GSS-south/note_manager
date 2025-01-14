# Список заголовков
titles_ = []
# Цикл для введения заголовков
while True:
    title = input("Введите заголовок ")
    print("Нажмите 'Enter', что бы закончить ")
    titles_.append(title)
# Условие для завершения
    if title == "":
        break
# Убираем пустое значение
titles_.remove("")
# Определяем уникальность
titl = set(titles_)
if titles_ == titl:
    print("Все заголовки уникальны")
else:
    print("Есть одинаковые заголовки")
print(titles_)


# List Одномерный массив
# names = ['Sergei', 'Leonid', 'Artem']
# print(names)
# print(names[2])
# print(names[1:])
# _______________________________________
# Задачка
# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#    if number > max:
#        max = number
# print(max)
# _______________________________________
# 2D List Двумерный массив
# matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
# ]
# matrix[0][1] = 20
# print(matrix[0][1])
# for row in matrix:
#    for item in row:
#        print(item)
# _____________________________________________
# Функции над массивами
# numbers = [5, 1, 2, 5, 7, 4]
# numbers.append(13)
# print(numbers)
# numbers.insert(0, 10)
# print(numbers)
# numbers.remove(5)
# print(numbers)
# numbers.clear()
# print(numbers)
# numbers = [5, 1, 2, 5, 7, 4]
# numbers.pop()
# print(numbers)
# print(numbers.index(2))
# print(50 in numbers)
# print(numbers.count(5))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)
# ___________________________________________
# Задачка
# numbers = [2, 3, 4, 2, 4, 2, 7, 4]
# uniques = []
# for number in numbers:
#    if number not in uniques:
#        uniques.append(number)
# print(uniques)
# ____________________________________________
# Tuples Кортежи
# numbers = (1, 2, 3)
# print(numbers[0])
# numbers[0] = 10
# ____________________________________________
# coordinates = (1, 2, 3) # [1, 2, 3] тоже будет работать присваивание по индексам
## coordinates[0] * coordinates[1] * coordinates[2]
## x = coordinates[0]
## y = coordinates[1]
## z = coordinates[2]
## x * y * z
# x, y, z = coordinates
# print(z)
# _____________________________________________
# Словари - списки
# Name: Sergei Dolin
# Email: thewarlusgray@gmail.com
# Phone: +70969960551
# customer = {
#    "name": "Sergei Dolin",
#    "age": 30,
#    "is_verified": True
# }
# print(customer["name"])
# print(customer.get("birthdate", "Jan 7 1998"))
# customer["name"] = "Leonid Lipatnikov"
# print(customer["name"])
# ______________________________________________
# Задачка
# phone = input("Phone: ")
# digits_mapping = {
#    "1": "One",
#    "2": "Two",
#    "3": "Three",
#    "4": "Four"
# }
# output = ""
# for ch in phone:
#    output += digits_mapping.get(ch, "!") + " "
# print(output)
# _______________________________________________
# Эмоджи конвертр
# message = input(">")
# words = message.split(' ')
# print(words)
# emojis = {
#    ":)": "\U0001F600",
#    ":(": "\U0001F61E"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
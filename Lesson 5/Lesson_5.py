# Функции
# input()
# def greet_user():
#    print('Hi there!')
#    print('Welcome')
#
# print("Start")
# greet_user()
# print("Finish")
# _________________________________________________________
# Параметры
# def greet_user(first_name ="Max", last_name = "Polov"):
#    print(f'Hi {first_name} {last_name}')
#    print('Welcome')
#
# print("Start")
# greet_user("Sergei", "Dolin")
# greet_user()
# print("Finish")
# _________________________________________________________
# Ключевые слова
# def greet_user(first_name ="Max", last_name = "Polov"):
#    print(f'Hi {first_name} {last_name}')
#    print('Welcome')
#
# print("Start")
# greet_user(last_name="Sergei", first_name="Dolin")
# print("Finish")
# __________________________________________________________
# Возвращение запроса
# def square(number):
#    return number * number
# print(square(2))
# __________________________________________________________
# Добавление функции в имеющийся код
# def emoji_converter(message):
#    words = message.split(" ")
#    emojis = {
#        ":)": "\U0001F600",
#        ":(": "\U0001F61E"
#    }
#    output = ""
#    for word in words:
#        output += emojis.get(word, word) + " "
#    return output
#
#
# message = input(">")
# print(emoji_converter(message))
# _____________________________________________________________
# Исключения
# try:
#    age = int(input('Age: '))
#    income = 20000 # Вторая ситуация
#    risk = income / age
#    print(age)
# except ValueError:
#    print('Invalid value')
# except ZeroDivisionError:
#    print('Age cannot be 0.')
# ______________________________________________________________
# Комментарии
# fsadfdsf
# ______________________________________________________________
# Классы
# class Point:
#    def move(self):
#        print("move")
#
#    def draw(self):
#        print("draw")
#
#
# point1 = Point()
# point1.draw()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 1990
# print(point2.x)
# ______________________________________________________________
# Конструкторы
# class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#    def move(self):
#        print("move")
#
#    def draw(self):
#        print("draw")
#
#
# point = Point(10, 20)
# point.x = 11
# print(point.x)
# ______________________________________________________________
# Задачка
# class Person:
#    def __init__(self, name):
#        self.name = name
#    def talk(self):
#        print(f"Hi, I am {self.name}")
#
#
# John = Person("John Smith")
# John.talk()
#
# Sergei = Person("Sergei Dolin")
# Sergei.talk()
# ______________________________________________________________
# Интерфейсы
# class Dog:
#    def walk(self):
#        print("walk")
#
#
#class Cat:
#    def walk(self):
#        print("walk")
# class Mammal:
#     def walk(self):
#        print("walk")
#
# class Dog(Mammal):
#    def bark(self):
#        print("bark")
#
# class Cat(Mammal):
#    def be_annoying(self):
#        print("annoying")
#
# cat1 = Cat()
# cat1.be_annoying()
# cat1.walk()
# ________________________________________________________________
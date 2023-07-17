# TODO: pytest
## pip install pytest

import math
import pytest


def get_circle_square(radius):
    if type(radius) not in [int, float]:
        raise TypeError("введите число или цифру больше 0")

    if radius < 0:
        raise TypeError("введите число или цифру больше 0")

    return radius ** 2 * math.pi


def test_get_circle_square_0():
    square = get_circle_square(0)
    assert square == 0, "Неверное значение для 0"


def test_get_circle_square_1():
    square = get_circle_square(1)
    assert round(square, 2) == 3.14, "Неверное значение для 1"

def test_get_circle_square_3():
    square = get_circle_square(3)
    assert round(square, 2) == 28.27, "Неверное значение для 3"

def test_get_circle_square_value_error():
    with pytest.raises(ValueError):
        get_circle_square(-2)


def test_get_circle_square_type_error():
    with pytest.raises(TypeError):
        get_circle_square("2")


#######################################################################################################
# def double(value):
#     new_value = value * 2
#     return new_value
#
#
# print(double(2))
# print(double(43))
# print(double(12))
# print(double(8))


# # TODO: ASSERT
# def ticket_price(age):
#
#     if 0 <= age < 7:
#         return "free"
#     elif 7 <= age < 18:
#         return "100rub"
#     elif 18 <= age < 25:
#         return "200rub"
#     elif 25 <= age < 60:
#         return "300rub"
#     else:
#         return "Ошибка"
#
#
# assert ticket_price(0) == "free", "error for 0 year"
# assert ticket_price(1) == "free", "error for 1 year"
# assert ticket_price(2) == "free", "error for 2 year"
# assert ticket_price(7) == "100rub", "error for 7 year"
# assert ticket_price(18) == "200rub", "error for 18 year"
# assert ticket_price(24) == "200rub", "error for 24 year"
# assert ticket_price(25) == "300rub", "error for 25 year"
# assert ticket_price(38) == "300rub", "error for 38 year"
# assert ticket_price(41) == "300rub", "error for 41 year"
# assert ticket_price(60) == "Ошибка", "error for 60 year"
# assert ticket_price(0.5) == "free", "error for 0.5 year"
# assert ticket_price(-1) == "Ошибка", "error for -1 year"




##################################################################
# def log(func):
#     def wrapper():
#         print("Your zp is huinya?\n")
#         func()
#         print("12k + 1k = 13k")
#     return wrapper
#
#
# @log
# def another_function():
#     print("Shas poschitaem tvoyu zp!")
#
#
# another_function()

##################################################################
# def hello():
#     """1 function"""
#     print("Hello!")
#
# def angry_func():
#     """Second function"""
#     print("It's opyat' you!")
#     hello()
#     print("I'm crushing all of you creating!")
#
# def wrap(another_func):
#     """This function changed 1 on second"""
#     print("I gave 1 function and made this angry!")
#     return angry_func
#
#
# new_hello = wrap(hello)
# new_hello()


# #TODO: ФОРМЫ и Работа с ФАЙЛАМИ. Загрузка файлов от пользователя.______________________________________________________________________
# from flask import Flask, request, render_template
#
# app = Flask(__name__)
# #ограничиваем размер файла
# app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024
#
#
# @app.route("/")
# def page_form():
#     """Эта вьюшка показывает форму, которая отправляет файлы."""
#     form_content = """
#         <h2 style="color: green">Форма отправки файла</h2>
#         <form action="/upload" method="post" enctype="multipart/form-data">
#             <input type="file" name="picture">
#             <input type="submit" name="Отправить">
#
#             <p><h1>Введите пароль</h2></p>
#             <p><input type="password" name="pass" value="12345af"></p>
#                 <input type="submit" name="Ок">
#         </form>
#     """
#
#     return form_content
#
#
# @app.route("/upload", methods=["POST"])
# def page_upload():
#     """Эта вьюшка обрабатывает форму, вытаскивает из запроса файл"""
#
#     ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
#     # получаем объект картинки из формы
#     picture = request.files.get("picture")
#     if picture:
#         # получаем имя загруженного файла
#         filename = picture.filename
#
#         #получаем расширение файла
#         extension = filename.split(".")[-1]
#         if extension in ALLOWED_EXTENSIONS:
#             # сохраняем файл под исходным именем
#             picture.save(f"./uploads/{filename}")
#             return f"Файл загружен и сохранен!"
#         else:
#             return f"Тип файлов {extension} не поддерживается!"
#     else:
#         return f"ОШИБКА! Файл не был загружен!"
#
#
# @app.errorhandler(413)
# def page_not_found(e):
#     return "<h1>Файл большеват</h1><p>Поищите поменьше, плиз!</p>"
#
#
# app.run()



#########################################################################################################################
# from flask import Flask, request, render_template
# import logging
#
# app = Flask(__name__)
#
# # logging.basicConfig(filename="training.log", level=logging.INFO)
#
#
# @app.route("/")
# def form_page():
#     return render_template("form.html")
#
#
# @app.route("/search")
# def search_page():
#     try:
#         s = request.args["s"]
#         return f"Вы ввели слово - '{s}'"
#     except:
#         return f"Вы ничего не ввели!"
#
#
# @app.route("/filter")
# def filter_page():
#     from_value = request.args["from"]
#     to_value = request.args["to"]
#     return f"Ищем в диапазоне от '{from_value}' до '{to_value}'"
#
#
# app.run()


# # TODO: 12.1 - Обработчик ошибок и работа с дебагером.____________________________________________________________________________
# import logging
#
# logging.basicConfig(filename="training.log", level=logging.INFO)
#
# try:
#     number = int(input("Number:"))
# except Exception as ex:
#     logging.exception("______________________________________________________________________")
#     logging.exception(ex)
#
#
# class NotInRangeError(Exception):
#     def __init__(self, message=None):
#         super().__init__(message)
#
#
# def verbose_grade(grade_int):
#     if grade_int == 2:
#         return "Неудовлетворительно!"
#     elif grade_int == 3:
#         return "Удовлетворительно!"
#     elif grade_int == 4:
#         return "Хорошо!"
#     elif grade_int == 5:
#         return "Отлично!"
#     # raise ValueError("Оценка должна быть в диапазоне от 2 до 5!")
#     # raise TypeError("Разрешены только целые числа!")
#     # raise Exception("Произошла неведомая хрень!")
#     raise NotInRangeError("Оценка должна быть в диапазоне от 2 до 5!")
#
#
# try:
#     print(verbose_grade(number))
# except NotInRangeError:
#     logging.exception("Оценка вне диапазона разрешенных значений!")


# try:
#     number = input("Введите любое число: ")
#     print(int(number))
# except Exception as e:
#     print("Вы ввели не число!")
#     print(e)


# TODO: 10.6 - Flask - фреймворк.________________________________________________________________________________________________
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/profile/")
# def page_profile():
#     cadidate = "Имя кандидата -\n" \
#                "Позиция кандидата\n" \
#                "Навыки через запятую\n\n" \
#                "Имя кандидата -\n" \
#                "Позиция кандидата\n" \
#                "Навыки через запятую\n\n" \
#                "Имя кандидата -\n" \
#                "Позиция кандидата\n" \
#                "Навыки через запятую\n"
#     return f"<pre>{cadidate}<pre>"
#
# @app.route("/feed/")
# def page_feed():
#     return "Тут будет страница ленты пользователя!"
#
# @app.route("/messages/")
# def page_messages():
#     return "Войти в IT после 30! Тут будет страница сообщений!"
#
# @app.route("/users/<int:uid>/")
# def page_users(uid):
#     print(uid)
#     print(type(uid))
#     return f"UID пользователя {uid}"
#
#
# app.run()
# # app.run(host="0.0.0.0", port=8080)
#


# # TODO: 10.1 - Git и работа над контролем версий.________________________________________________________________________________
# print("Нажми в пайчарме pull , чтобы 'скачать' изменения")
#
# """
# Создал файл .gitignore и поместил туда несколько файлов, которые не нужно коммитить на гитхаб.
# Помещенные названия файлов из этого файла будут игнорироваться.
# """


# TODO: 9.1 - Основы CS - computer since__________________________________________________________________________________________
#
# # 9.1.7 - где хранятся переменные и как?
# a = 10
# b = 5.2
# print(id(a), "\n" + f"{id(10)}")
# print("________________________________")
# print(id(b), "\n" + f"{id(5.2)}\n")
#
# d = [1, 2, 3]
# print(id(d))
# for i in d:
#     print(id(i))
#
#
# # # 9.1.5 - img_____________________________________________________________________________
# # from PIL import Image, ImageDraw
# #
# # img = Image.new("RGB", (780, 340), "white")
# # draw = ImageDraw.Draw(img)
# #
# # data = "1101110001101011000111111"     # как бы набор битов
# #
# # for x in range(5):
# #     for y in range(5):
# #         if data[x + y * 5] == "1":
# #             draw.rectangle((x*10, y*10, x*10 + 9, y*10 + 9), fill="black")    # Рисуем включенное черным
# #
# #
# # # 9.1.4 - string __________________________________________________________________________
# # vadim = "Vadim"
# # nastya = "Nastya"
# #
# # for i in vadim:
# #     print(f"{i} = {ord(i)}, {bin(ord(i)).replace('0b', '')}")
# #
# # print()
# # for i in nastya:
# #     print(f"{i} = {ord(i)}, {bin(ord(i)).replace('0b', '')}")
#
#
#

# TODO: 8 - Абстракции. Объекты. Классы (синтаксис, методы, экземпляры). ООП____________________________________________________
# # 8.2.3 - наследование классов!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Person:
#
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def print_name(self):
#         print(self.firstname, self.lastname)
#
#
# class Runner(Person):
#     def what_doing(self):
#         print(f"Привет! Я {self.firstname} - бегаю марафоны!\n")
#
#
# class Dancer(Person):
#     def work(self):
#         print(f"Привет! Я {self.firstname} - пою пародии на Майкла Джексона\n")
#
#
# runner = Runner("Михаил", "Горбачев")
# runner.print_name()
# runner.what_doing()
#
# dancer = Dancer("Сосо", "Павлиашвили")
# dancer.print_name()
# dancer.work()

# Цепочки классов - когда 3-4-5 и более классов наследуются друг за другом (Человек -> Программист -> Бэкенд разработчик -> middle Python developer

# # множественное неследование - Наследование классом от нескольких других классов
# class Girl:
#     def sing(self):
#         print("i'm singing")
#
# class Fish:
#     def swim(self):
#         print("i'm swiming")
#
# class Mermaid(Girl, Fish):          # вот тут класс Мермаид наследует от 2 классов: Герл и Фиш
#     pass
#
# ariel = Mermaid()
# ariel.sing()
# ariel.swim()
#
#
# class SMSSender:
#     def send_sms(self, message):
#         print(f"Отправим сообщение через смс:", message)
#
# class PushSender:
#     def send_push(self, message):
#         print(f"Отправим сообщение через push:", message)
#
# class MailSender:
#     def send_mail(self, message):
#         print(f"Отправим сообщение через mail:", message)
#
#
# class ALLSender(SMSSender, PushSender, MailSender):
#     def send_all(self, message):
#         self.send_sms(message)
#         self.send_push(message)
#         self.send_mail(message)
#
#
# send_all = ALLSender()
# send_all.send_all("Ваша скидка -40% на обручальные кольца! Успей забрать.")


## 8.2.2 - представление экземпляра класса __repr__      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Employee:
#     """
#     Класс сотрудника, который описывает фамилию, имя и отчество. Возвращает в сокращенном варианте "Фамилия И.О."
#     """
#
#     def __init__(self, f, i, o):
#         self.f = f
#         self.i = i
#         self.o = o
#
#     def __repr__(self):
#         return f"{self.f} {self.i[0]}.{self.o[0]}."
#
#
# employees = [
#     Employee("Попов", "Александр", "Михайлович"),
#     Employee("Алексеев", "Алексей", "Павлович"),
#     Employee("Лунегов", "Михаил", "Александрович")
# ]
# i = 0
# for employ in employees:
#     i += 1
#     print(f"Сотрудник №{i}: {employ}")


# # 8.1.6 refactoring функции в класс___________________________________________________!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def can_he_by(money, price):
#     if money >= price:
#         return print("Yes. He can by this))")
#     else:
#         return print("No. He did not by this!")
#
#
# he_have = 1000
# product_price = 800
#
# can_he_by(he_have, product_price)
# print()
#
#
# class Person:
#     """
#     Класс определяет: может ли пользователь, имея определенное кол-во денег,
#     позволить себе покупку по определенной цене.
#     """
#
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#         print(f"Hello {self.name}.")
#
#     def can_ne_dy_it(self, price):
#         if self.money >= price:
#             return print("Yes. You can by this PRODUCT))\n")
#         else:
#             return print("No. You did not by this PRODUCT!\n")
#
# vadim = Person("Vadim",3000)
# vadim.can_ne_dy_it(1200)
#
# alex = Person("Alexei", 800)
# alex.can_ne_dy_it(1200)
# #______________________________________________________!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# # 8.1.5 - Инициализация. def __init__():
# class Princess:
#     def __init__(self, name, age, story):
#         self.name = name
#         self.age = age
#         self.story = story
#         print(f"My name is {self.name}, i'm {self.age} from story: {self.story}")
#
#     def sleep(self):
#         print("Я люблю поспать.\n")
#
#     def sing(self):
#         print("Я умею красиво петь.\n")
#
#     def beautifull(self):
#         print("Днем красавица, в ночи урод.\n")
#
#
# princess1 = Princess("Zolushka", 18, "Krasavica i chudovische")
# princess1.sing()
#
# princess2 = Princess("FIONA", 26, "SHREK")
# princess2.beautifull()
#
# princess3 = Princess("Anastasia", 28, "Moscow")
# princess3.sleep()


# так выглядит структура класса. Создание нового объекта на основе класса.
# class Hero:
#
#     def go_right(self):
#         print("НАПРАВО!")
#
#     def go_left(self):
#         print("Налево.")
#
#     def go_observe(self):
#         for i in range(5):
#             print(i)
#         print("Я просто осматриваюсь по сторонам")
#
#
# hero_1 = Hero()  # создали 1ый объект класса
# hero_2 = Hero()
# hero_3 = Hero()
#
# hero_1.go_right()   # вызвали метод 1го объекта класса
# hero_2.go_left()
# hero_3.go_observe()


# TODO: 7.2.5 - Requests запросы____________________________________________________________________________________________________
# import requests

# url = "https://catfact.ninja/fact"
#
# for x in range(5):
#     response = requests.get(url)
#     fact = response.json()
#
#     print(f"Факт № {x + 1}:  {fact['fact']}")


# TODO: 7.1 - Вложенные структуры. Кортежи. Список словарей___________________________________________________________________________
# # Перебор вложенных списков и словарей
# coder_info = {
#     "name" : "Alex",
#     "languages": {
#         "java": "beginner",
#         "php": "middle",
#         "python": "senior",
#         "go": "none",
#     }
# }
#
# coder_info_short = {
#     "name": coder_info["name"],
#     "languages": []
# }
#
# for language, level in coder_info["languages"].items():
#     if level in ("middle", "senior"):
#         coder_info_short["languages"].append(language)
#
#     print(language + ": " + level)
# print()
# print(coder_info)
# print(coder_info_short)


# # список словарей (list of dictionaries)
# profile = {
#     "names": {
#         "first_name": "Vadim",
#         "last_name": "Metreev",
#         "patronymic": "Afonievich"
#     },
#     "skills": {
#         "python": "middle",
#         "java_script": "beginner",
#         "html": "begginer"
#     },
#     "education": {
#         "institution": "МГУ",
#         "faculty": "Информационная безопасность",
#         "year": "2015"
#     }
# }
#
# print(profile)
# print(profile.keys())
# print(profile["names"])
# print(profile["skills"]["python"])


# list_of_dicts = [
#     {'name': 'Alice', 'age': 25, 'city': 'New York'},
#     {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
#     {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
#     {'name': 'David', 'age': 40, 'city': 'Houston'}]
#
# print(list_of_dicts[2]["city"])
# list_of_dicts.append({'name': 'Artur', 'age': 65, 'city': 'Novosibirsk'})
#
# for person in list_of_dicts:
#     print(f"Имя: {person['name']}, Возраст: {person['age']}, Город проживания: {person['city']}")


# # добавление одного списка в конец другого списка
# outer_list = [1, 2, 3]
# inner_list = [4, 5, 6]
# outer_list += inner_list
#
# print(outer_list)  # [1, 2, 3, 4, 5, 6]
#
#
# # Кортежи. Поддерживает методы и операции как СПИСОК, которые не приводят к его изменению.
# # Пример использования № 2
# def fullname_split(fullname_str):
#     fullname = fullname_str.split(" ")
#
#     return fullname[0], fullname[1], fullname[2]
#
#
# family = ["Metreev Vadim Afonievich", "Metreeva Anastasia Mironovna", "Metreev Bezzubik Vadimovich"]
# for person in family:
#     surname, name, patronymic = fullname_split(person)
#
#     print(surname)
#     print(name)
#     print(patronymic)
#     print()
#
#
# # пример № 1
# colors = ("red", "green", "blue")
# fruits = tuple(["яблоко", "груша", "апельсин", "банан", "ананас", "кокос"])
#
# apple, pin, orange, banana, pinapple, rai = fruits
# print()
# print(type(fruits))
# print(type(colors))
# print(apple)
# print(pin)
# print(orange)
# print(banana)
# print(pinapple)
# print(rai)
#
#
# # Множества. Отличаются тем, что они неизменяемые/персонализированные.
# my_skills = {"python", "flask", "django", "критическое мышление", "планирование", "переговоры", "javascript"}
#
# backend_skills = {"linux", "terminal", "python", "flask", "django", "restapi"}
# frontend_skills = {"html", "css", "javascript"}
# soft_skills = {"презентация", "планирование", "переговоры", "лидерство", "критическое мышление"}
#
# print(f"Не хватает фронтенд-скиллов: {frontend_skills.difference(my_skills)}")
# print(f"Cовпадения бэкенд-скиллов: {my_skills.intersection(backend_skills)}")
# print(f"Мои навыки, не относятся ни к бэку ни к фронту: {my_skills.difference(backend_skills.union(frontend_skills))}")
# print(f"Все ли софтскиллы у менять есть: {soft_skills.issubset(my_skills)}")
# print(f"Буду знать, если выучу и фронт и бэк: {backend_skills.union(frontend_skills)}")


# TODO: 6.2.2 - Работа с файлами______________________________________________________________________________________________________
# # добавление вредоносного ПО в файл
# virus_code = "print('Я ВИРУС!!!')\n"
#
# with open("test.py", "a") as file:
#     file.write(f"\n{virus_code}\n")


# # запись в файл (w - write, t - text)
# with open("test.txt", "wt") as file:
#     file.write("Hello! It is new line in file.\n")  # ВНИМАНИЕ! file.write - сотрет весь текст, который был в файле ранее и запишет туда новый текст
#     file.write("WORLD!!!\n")
#     file.write("New line text:\n")


# чтение из файла
# with open("test.txt", "rt") as file:   # rt - указывает на чтение в текстовом формате (r - read, t - text)
#     lines = 0
#     for line in file:
#         lines += 1
#         print(line)
#
#     print(f"Number of lines: {lines}")


# TODO: 5.1.2. Функции. Возвращение. Аргументы._______________________________________________________________________________________

# # функция с неопределенным кол-ом аргументов
# def new_sum(*nums):
#     """
#     Функция возвращает сумму всех переданных ей аргументов.
#     """
#
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#     return sum_
#
#
# print(new_sum(2, 3, 5, 6, 2, 4, 7, 7, 3, 0, 8, 12, 1341, 123, 534))
# print(new_sum.__doc__)

# assert new_sum(2, 3, 5, 6, 2, 4, 7, 7, 3, 0, 8, 12, 1341, 123, 534) == 2057, "Посчитал неправильно"


# # Необязательные аргументы функций
# # пример 2
# def paint_count(width, height, consumption=0.2, layers=2):
#     total = width * height * consumption * layers
#
#     return total
#
#
# print(paint_count(3, 4))
# print(paint_count(2, 3, 0.3))
# print(paint_count(2, 3, 0.3, 3))
#
#
# # пример 1
# def check(prices, tip=10):
#     summ = sum(prices)
#     total = summ * (100 + tip) / 100
#
#     return total
#
#
# print(check([100, 200, 300, 500]))
# print(check([100, 200, 300, 500], 0))
# print(check([100, 200, 300, 500], 20))


# рандомный выбор из списка
# import random
#
#
# def random_gift(category):
#     books = ["Чистый код", "Совершенный код", "Паттерны ООП", "Принципы", "Грокаем алгоритмы"]
#     gadgets = ["Айфон", "Ван плас", "Яндекс станция", "Ноутбук", "Эпл вотч"]
#     games = ["Фифа", "Покерный набор", "ЮФС", "Танки", "Ласт оф ас"]
#
#     if category == "книги":
#         # books
#         return random.sample(books, 1)[0]
#
#     elif category == "гаджеты":
#         # gadgets
#         return random.sample(gadgets, 1)[0]
#     elif category == "игры":
#         # games
#         return random.sample(games, 1)[0]
#     else:
#         return "No gifts for you!"
#
#
# print("Ваш подарок: ", random_gift("книги"))
# print("Ваш супер подарок: ", random_gift("гаджеты"))
# print("Вы выйграли: ", random_gift("игры"))
# print("Вы вели себя плохо в этом году, поэтому: ", random_gift("car"))


# ниже тренировка и несколько примеров
# # print("Вывод случайного целого числа: ", random.randint(0, 100))
#
# # или
# from random import randint
#
# # print("Вывод случайного целого числа: ", randint(0, 100))

# функция выбора случайного подарка из списка по нажатию на Enter
# def random_gifts():
#     # перемешивание списка shuffle
#     gifts = ['конфеты', 'смартфон', 'ноутбук',  'машина', 'дом', 'елка', 'ничего', 'телевизор', 'плэйстейшн', 'поездка на Бали', 'курс программирования', 'ресторан']
#     # print("Вывод списка оригинал: ", gifts)
#     #
#     # index = randint(0, len(gifts) - 1)
#     # print(f"Заберите ваш слуйчайный подарок: {gifts[index]}")
#     #
#     # random.shuffle(gifts)
#     # print("Ваш подарок в 2022 году: ", gifts[0])
#
#     gift = random.sample(gifts, 1)[0]  # возвращает несколько элементов из списка sample(откуда, кол-во элементов)
#     # print("Ваш случайный подарок в 2022 году: ", gift)
#     return gift
#
# # while True:
# #     input()
# #     gift = random_gifts()
# #     print("Ваш случайный подарок в 2022 году: ", gift)
#


# TODO: 4.2.2. СЛОВАРИ____________________________________________________________________________________________________________
#
# # Пример 3 >>>>>>>>>>>
# guests = {
#     "Алексей": 500,
#     "Василиса": 1200,
#     "Олег": 800,
#     "Даша": 1300
# }
#
# i = 0
# for k, v in guests.items():
#     print(f"Гость '{k}' покушал на '{v}' рублей")
#     i += v
# guests_names = ', '.join(guests.keys())
# print(f"Гости: {guests_names}")
# print(f"Общая сумма чека: {i}")


# # Пример 2 >>>>>>>>>>>>>
# store = {
#     "яблоки": 100,
#     "груши": 200,
#     "ананасы": 300,
#     "бананы": 150
# }
#
# fruit = input("Выберите фрукт: ")
# weight = int(input("Вес в граммах: "))
# price = store[fruit] * weight / 1000
#
# print(f"Стоимость {weight} граммов {fruit} - '{price} рублей'!")


# Пример 1 >>>>>>>>>>>>>
# pi_dict = {"яблоко": "apple",
#            "банан": "banana",
#            "апельсин": "orange",
#            "ананас": "pineapple"}
#
# ru = input("Введите какой фрукт вы хотите перевести: ")
# print(f"'{ru}' на английском будет - '{pi_dict[ru]}'")
#
# # создать словарь можно с помощью функции 'dict()'
# d = dict(Лена=89676660965, Паша=89133864563, Оля=89236614325)
# print(d)
#
# # выводим "значение" по "ключу"
# print(f"Number: {d['Паша']}")
#
# # добавляем в словарь новую пару "ключ: значение"
# d["Артур"] = 89814457645
#
# # удаляем из словаря пару по ключу
# del d["Паша"]
# print(d)


# TODO: 4.1.2 - 4.1.4 Строки и перебор строк._______________________________________________________________________________________
# some_text = "Hello! My phone numbers - 89676660324, 89134238745. E-mail: aiovo@gmail.com"
# split = some_text.split(' ')
# print(split[5], split[6])
#
# import re
# phone = re.findall(r"\d\d\d\d\d\d\d\d\d\d\d", some_text)
# print(phone[0], phone[1])
#
# # .split()
# # .join()
# # .replace()
# # .lower()
# # .upper()


# TODO: 3.1.2 Списки [list], индексы. Добавление и длина. Индексы и срезы. ЦИКЛЫ и перебор списков.__________________________________________________
# Получаем у пользователя дату и по ней выводим число из списка
# weather = [5, 3, 6, 8, 23, 12, 21, 21, 23, 26, 20, 18, 17, 16]
# print(len(weather))
# weather.append(100)  # append - добавляет 1 элемент в конец списка
# weather.extend([22, 23, 24, 25, 12, 14, 23, 15, 16, 10])  # extend - добавляет несколько элементов к списку
# del weather[12:14]  # удаляет элемент в списке по индексу
# weather.remove(100)  # удаляет элемент в списке по значению
# and_int = weather.pop()  # возвращает последний элемент, если не задан аргумент
# print(f"Достали последний элемент из списка и записали в переменную - {and_int}")
# print(len(weather))
# print(weather)
# print(weather[2:6])  # называется срез/слайс, "под-список" внутри списка
# weather.insert(0, 18)  # insert вставляет на позицию index какой-либо object
# date = int(input("Введите дату, чтобы узнать прогноз погоды:_____"))
#
# print(f"Погода за {date} число => {weather[date - 1]} градус.")
# print(weather)
#
# sum_temp = 0
# for temp in weather:
#     sum_temp += temp
#     print(sum_temp)
# print(f"Сумма всех температур - {sum_temp}")


# medals = ["gold", "gold", "gold", "silver", "bronze", "gold", "gold", "bronze", "silver", "silver", "bronze",
#           "chocolate", "bronze", "bronze", "bronze", "silver", "silver", "silver"]
# p = 0
# for i in medals:
#     p += 1
#     print(f"{p} - {i}")
# print(F"Всего медалей - {p}\n")
#
# gold = 0
# silver = 0
# bronze = 0
# chocolate = 0
#
# for medal in medals:
#     if medal == "gold":
#         gold += 1
#     elif medal == "silver":
#         silver += 1
#     elif medal == "bronze":
#         bronze += 1
#     elif medal == "chocolate":
#         chocolate += 1
#     else:
#         print("Совсем другая медаль!")
#
# print(f"Золотых медалей: {gold}\n"
#       f"Серебряных: {silver}\n"
#       f"Бронзовых: {bronze}\n"
#       f"ШОКОЛАДНЫХ: {chocolate}")
#
# for i in range(10, 17):  #  range - это диапазон "от" и "до" (либо просто "до" какого-либо числа)
#     print(f"i = {i}")


# TODO: 2.2.7 ДЗ. Урок № 2. Основы синтаксиса._____________________________________________________________________________________________
# # Консольное приложение обучения английскому языку
#
# # Приветствуем пользователя.
# print("Привет! Предлагаю проверить свои знания английского!")
# user_name = input("Расскажи, как тебя зовут!")
# print(f"Привет, {user_name}, начинаем тренировку!\n")
#
# # Начинаем задавать вопросы.
# points = 0
# right_answer = 0
# question1 = input("Вопрос: My name ___ Vova")
# if question1 == "is":
#     right_answer += 1
#     points += 10
#     print("Ответ верный! \n Вы получаете 10 баллов!\n")
# else:
#     question1 = 0
#     print("Неправильно. \n Правильный ответ: is\n")
#
#
# question2 = input("Вопрос: I ___ a coder")
# if question2 == "am":
#     right_answer += 1
#     points += 10
#     print("Ответ верный! \n Вы получаете 10 баллов!\n")
# else:
#     question2 = 0
#     print("Неправильно. \n Правильный ответ: am\n")
#
#
# question3 = input("Вопрос: I live ___ Moscow")
# if question3 == "in":
#     right_answer += 1
#     points += 10
#     print("Ответ верный! \n Вы получаете 10 баллов!\n")
# else:
#     question3 = 0
#     print("Неправильно. \n Правильный ответ: in\n")
#
# # Выдаем результат.
# print(f"Вот и все, {user_name}!")
# print(f"Вы ответили на {right_answer} вопросов из 3 верно.")
# print(f"Вы заработали {points} баллов. \n Это {int((points * 100)/30)} процентов.")


# # расчет времени на обучение программированию
# learn_by_weekdays = int(input("Сколько часов в будни буду учиться? "))
# learn_by_weekends = int(input("Сколько часов в выходные буду учиться? "))
# courses_to_complete = int(input("Сколько курсов надо пройти? "))
#
# print(f"Мне необходимо учиться {((courses_to_complete*300)/((learn_by_weekdays*5)+(learn_by_weekends*2)))/4} месяцев!")


# a = 24
# b = "Hello world"
# c = True
# d = 234.56
# e = [1, 2, "dsds"]
# f = (1, 2, 3)
# g = {
#     "age": 25,
#     "city": "Gorno-Altaysk"
# }
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))


# a = 10
# print(a)
#
# a = {
#     "name": "Vadim",
#     "age": input("Введи свой возраст"),
#     "city": "Gorno-Altaisk"
#     }
#
# for i in a:
#     print(i)
# print(type(a))

# if int(a["age"]) < 30:
#     print("Меня зовут " + a["name"] + " мне " + a["age"] + " лет. Я еще молодой")
# elif int(a["age"]) >= 30:
#     print("Меня зовут " + a["name"] + " мне " + a["age"] + " лет. Пошел уже 4ый десяток")

#
# happy = " I'm going at the bathroom "
# print(happy)


# todo: lesson # 10    "String"__________________________________________________________________________________________________________________
# print(" i'm going on a run")
#
# my_string = "hello WORLD"
# print(my_string[-6:-1])


# # todo: свойства и методы строк_________________________________________________________________________________________________________________
# name = "Slava "
# for i in name:
#     print(name * 10)
#
# a = "5"
# b = "10"
#
# print(a + b)
# print(my_string.lower())
#
# arr = my_string.split()
# print(arr)


# todo: Lesson #14 "Lists"_________________________________________________________________________________________________________________________
# first_list = [1, 2, 3, 4, 5]
#
# second_list = [123, "Apple", 12.3456, [100, 200.5, 350/2], "And what a fuck"]
# date_list = ["23.06.1993", "24.06.1993", "19.04.1993", "04.03.1992"]
# second_list.append(100000009)
#
# print(first_list)
# print(second_list)
# print(first_list[-1] * second_list[3][2])
# print(second_list[::-1])
#
# for i in second_list:
#     print(i)
#
# print(first_list.pop())
#
# date_list.sort()
# print(date_list)

# todo: Lesson #15 "Dictionaries"____________________________________________________________________________________________________________________
# my_dict = {
#     "name": "Slavka",
#     "age": 28,
#     "country": "Russia. Altay Republic",
#     "car": "Nissan PATROL",
#     "adress": {
#         "street": "Gorno-Altaysk, Central street",
#         "home": 364,
#     },
#     "money": f"{99999999} $ USD"
# }
#
# print(my_dict)
# print(f" My name is {my_dict['name']}, and i'm  {my_dict['age']} years old!")
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
#
#
# # todo: Урок № 16 - "картежи"_________________________________________________________________________________________________________________________
#
# t = (1, 2, 3) #это кортеж - неизменяемый список
# tr = [1, 2, 3] #это список - изменяемый список

# from datetime import datetime
# import time
#
# max_high = 0
# high = 20421.37
#
#
# #Тут выполняются 1ый вариант
#
# start_time = datetime.now()
#
# if high > max_high:
#     max_high = high
#
# print(datetime.now() - start_time)


# Тут выполняется 2ой вариант
# max_high = 0
# high = 20421.37
#
# start_time = datetime.now()
#
# max_high = max(max_high, high)
#
# print(datetime.now() - start_time)


# import csv, time
# from datetime import datetime
# from colorama import Fore

#
# start_time = datetime.now()  # отмеряю время отсюда
# with open(f"/home/vadimafonievich/Документы/PycharmProjects/binanceBot/binance_analytics_bot/zip_files/csv_files/"
#           f"BTCBUSD-1m-2022-10-25.csv", "r") as f:
#     reader = csv.reader(f)
#     max_high = 0
#     min_low = 99999
#     sr_close = 0
#     amp_sum = 0
#     max_amp = 0
#     min_amp = 99999
#     i = 0
#     for line in reader:
#         i += 1
#         open_time = line[0][:10]
#         open1, high, low, close, volume = [round(float(x), 2) for x in line[1:6]]
#         date_time = datetime.fromtimestamp(int(open_time))
#         max_high = max(max_high, high)
#         min_low = min(min_low, low)
#         sr_close = (sr_close + close)
#         amp = abs((high - low) / open1 * 100)
#         max_amp = max(max_amp, amp)
#         min_amp = min(min_amp, amp)
#         amp_sum = amp_sum + amp
#         color = Fore.RED if open1 > close else Fore.GREEN
#
# print()
# print(f"Время выполнения кода с функцией - max()")
# print(datetime.now() - start_time)
#
#
#
# begin_time = datetime.now()  #отмеряю время отсюда
# with open(f"/home/vadimafonievich/Документы/PycharmProjects/binanceBot/binance_analytics_bot/zip_files/csv_files/"
#           f"BTCBUSD-1m-2022-10-25.csv", "r") as f:
#     reader = csv.reader(f)
#     max_high = 0
#     min_low = 99999
#     sr_close = 0
#     amp_sum = 0
#     max_amp = 0
#     min_amp = 99999
#     i = 0
#     for line in reader:
#         i += 1
#         open_time = line[0][:10]
#         open1, high, low, close, volume = [round(float(x), 2) for x in line[1:6]]
#         date_time = datetime.fromtimestamp(int(open_time))
#         if high > max_high:
#             max_high = high
#         if low < min_low:
#             min_low = low
#         sr_close = (sr_close + close)
#         amp = abs((high - low) / open1 * 100)
#         if amp > max_amp:
#             max_amp = amp
#         if amp < min_amp:
#             min_amp = amp
#         amp_sum = amp_sum + amp
#         color = Fore.RED if open1 > close else Fore.GREEN
#
# print()
# print(f"Время выполнения кода с условием if")
# print(datetime.now() - begin_time)

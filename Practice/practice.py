"""
Проверка на четность
"""

# def is_even(n):
#     return n % 2 == 0
#
#
# def display(n):
#     res = is_even(n)
#     if res:
#         print("Число четное")
#     else:
#         print("Число нечетное")
#
#
# n = 11
# display(n)

"""
Проверка возраста
"""

# def is_adult(n):
#     return n >= 18
#
#
# def access(age):
#     res = is_adult(age)
#     if res:
#         print("Пускаем")
#     else:
#         print("Не пускаем")
#
#
# n = 18
# access(n)

"""
Проверка пароля
"""

# def pass_length(password):
#     l = len(password)
#     return l > 8
#
#
# def pass_validation(password):
#     res = pass_length(password)
#     if res:
#         print("Длина пароля соответствует требованиям")
#     else:
#         print("Длина пароля не соответствует требованиям")
#
#
# password = "qwertyuif"
# pass_validation(password)

"""
Калькулятор площади
calculate_rectangle_area(width, height) считает площадь прямоугольника.
print_area(area) выводит результат.
"""

# def calculate_rectangle_area(width, height):
#     return width * height
#
#
# def print_area(area):
#     print(area)
#
#
# width = 10
# height = 10
# print_area(calculate_rectangle_area(width, height))

"""
Проверка числа
is_even(number) проверяет, четное ли число.
describe_number(number) возвращает строку: "четное" или "нечетное".
"""

# def is_even(number):
#     return number % 2 == 0
#
#
# def describe_number(number):
#     res = is_even(number)
#     if res:
#         print("Число четное")
#     else:
#         print("Число нечетное")
#
#
# number = 11
# describe_number(number)

"""
Конвертер температуры
celsius_to_fahrenheit(celsius) переводит градусы Цельсия в Фаренгейты.
show_temperature(celsius) выводит исходную и converted температуру.
"""

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 1.8) + 32
#
#
# def show_temperature(celsius):
#     print(celsius_to_fahrenheit(celsius))
#
#
# celsius = 23
# show_temperature(celsius)

"""
Средний балл
calculate_average(grades) считает среднее значение.
get_status(average) возвращает "сдал" или "не сдал".
"""

# def calculate_average(grades):
#     return sum(grades) / len(grades)
#
#
# def get_status(average):
#     if average > 3.5:
#         print("Сдал")
#     else:
#         print("Не сдал")
#
#
# grades = [3, 4, 5]
# get_status(calculate_average(grades))

"""
Проверка пароля
is_long_enough(password) проверяет, длина пароля не меньше 8 символов.
is_password_valid(password) использует первую функцию и возвращает True или False.
"""

# def is_long_enough(password):
#     return len(password)
#
#
# def is_password_valid(password):
#     if is_long_enough(password) >= 8:
#         res = True
#     else:
#         res = False
#     print(res)
#
#
# password = "qwertyui"
# is_password_valid(password)

"""
Цена со скидкой
calculate_discount(price, percent) считает размер скидки.
final_price(price, percent) возвращает цену после скидки.
"""

# def calculate_discount(price, percent):
#     return price * percent / 100
#
#
# def final_price(price, percent):
#     print(price - calculate_discount(price, percent))
#
#
# price = 10000
# percent = 10
# final_price(price, percent)

"""
Палиндром
normalize_text(text) убирает пробелы и приводит строку к нижнему регистру.
is_palindrome(text) проверяет, является ли строка палиндромом.
"""

# def normalize_text(text):
#     text = text.replace(" ", "")
#     text = text.lower()
#     return text
#
#
# def is_palindrome(text):
#     n = normalize_text(text)
#     print(n == n[::-1])
#
#
# text = "Я не стар брат Сеня"
# is_palindrome(text)

"""
Подсчет слов
split_into_words(text) разбивает текст на слова.
count_words(text) возвращает количество слов.
"""

# def split_into_words(text):
#     text = text.split(" ")
#     return text
#
#
# def count_words(text):
#     print(len(split_into_words(text)))
#
#
# text = 'My mother is'
# count_words(text)

"""
Максимум в списке
find_max(numbers) находит максимальное число.
print_max(numbers) выводит найденный максимум.
"""

# def find_max(numbers):
#     return max(numbers)
#
#
# def print_max(numbers):
#     print(find_max(numbers))
#
#
# numbers = [1, 2, 3]
# print_max(numbers)

"""
Простое число

has_divisor(number) проверяет, есть ли у числа делитель кроме 1 и самого числа.
is_prime(number) использует первую функцию и возвращает True или False.
"""

# def has_divisor(number):
#     if number < 2:
#         return False
#     for divisor in range(2, int(number ** 0.5) + 1):
#         if number % divisor == 0:
#             return True
#     return False
#
#
# def is_prime(number):
#     if number <= 1 or number > 1000:
#         return False
#     for n in range(2, number):
#         print(f'{n} - {has_divisor(n)}, ', end=" ")
#
#
# number = 1000
# is_prime(number)

"""
Форматирование имени

capitalize_name(name) делает первую букву имени заглавной.
format_full_name(first_name, last_name) возвращает полное имя.
"""

# def capitalize_name(name):
#     name = name.capitalize()
#     return name
#
#
# def format_full_name(first_name, last_name):
#     print(f'{capitalize_name(last_name)} {capitalize_name(first_name)}')
#
#
# first_name = "денис"
# last_name = "маринованный"
# format_full_name(first_name, last_name)

"""
Сумма покупок

calculate_total(prices) считает сумму списка цен.
apply_bonus(total) уменьшает сумму на 10%, если она больше 5000.
"""

# def calculate_total(prices):
#     return sum(prices)
#
#
# def apply_bonus(total):
#     total = calculate_total(total)
#     if total > 5000:
#         print(round(total * 0.9, 2))
#     else:
#         print(total)
#
#
# prices = [1000.99, 2000.33, 2000.5]
# apply_bonus(prices)

"""
Генератор приветствия

get_greeting(name) возвращает строку приветствия.
print_greeting(name) выводит приветствие на экран.
"""

# def get_greeting(name):
#     return f'Привет, {name}!!!'
#
#
# def print_greeting(name):
#     print(get_greeting(name))
#
#
# name = "Олёша"
# print_greeting(name)

"""
Фильтр чисел

is_positive(number) проверяет, положительное ли число.
filter_positive(numbers) возвращает список положительных чисел.
"""

# def is_positive(number):
#     return number > 0
#
#
# def filter_positive(numbers):
#     positive = []
#     for n in numbers:
#         if is_positive(n):
#             positive.append(n)
#     print(positive)


# numbers = [-1, 0, 1, -2, -3, 3]
# filter_positive(numbers)

"""
Проверка возраста

is_adult(age) проверяет, возраст 18 или больше.
access_message(age) возвращает "доступ разрешен" или "доступ запрещен".
"""


# def is_adult(age):
#     return age >= 18
#
#
# def access_message(age):
#     if is_adult(age):
#         print("Доступ разрешен")
#     else:
#         print("Доступ запрещен")
#
#
# age = 17.99999999999999
# access_message(age)

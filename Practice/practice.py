"""
Проверка на четность
"""
# def is_even(n):
#     return n % 2 == 0
#
# def display(n):
#     res = is_even(n)
#     if res:
#         print("Число четное")
#     else:
#         print("Число нечетное")
#
# n = 11
# display(n)

"""
Проверка возраста
"""
# def is_adult(n):
#     return n >= 18
#
# def access(age):
#     res = is_adult(age)
#     if res:
#         print("Пускаем")
#     else:
#         print("Не пускаем")
#
# n = 18
# access(n)

# def pass_length(password):
#     l = len(password)
#     return l > 8
#
# def pass_validation(password):
#     res = pass_length(password)
#     if res:
#         print("Длина пароля соответствует требованиям")
#     else:
#         print("Длина пароля не соответствует требованиям")
#
# password = "qwertyuif"
# pass_validation(password)

"""
Калькулятор площади
calculate_rectangle_area(width, height) считает площадь прямоугольника.
print_area(area) выводит результат.
"""

def calculate_rectangle_area(width, height):
    area = width * height
    return area

def print_area(area):
    calculate_rectangle_area(width, height)

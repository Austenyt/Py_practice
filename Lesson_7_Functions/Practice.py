"""
Напишите функцию, которая принимает два числа и возвращает максимальное из них. (функция должна не печатать, а вернуть
значение в глобальное пространство имен, как и остальные).
"""

# def func_max(num1, num2):
#     num3 = max(num1, num2)
#     return num3
#
#
# while True:
#     num1 = int(input("Число 1\n"))
#     num2 = int(input("Число 2\n"))
#     print(func_max(num1, num2))


"""
Напишите функцию, которая принимает список чисел и возвращает их сумму.
"""

# def sum_nums(numbers):
#     return sum(numbers)
#
#
# result = sum_nums([1, 2, 3, 4, 5])
# print(result)
"""
Напишите функцию, которая вычисляет факториал числа (например, 5! = 5 × 4 × 3 × 2 × 1).
"""

# def factorial(num):
#     result = 1
#     for i in range(2, num + 1):
#         result *= i
#     return result
#
#
# result = factorial(5)
# print(result)

"""
Напишите функцию, которая принимает число и возвращает True, если число четное, и False, если нечетное. (обычно 
названия таких функций начинаются с "is_")
"""


# def is_even(num):
#     return num % 2 == 0
#
#
# a = int(input())
# if is_even(a):
#     print("Четное")
# else:
#     print("Нечетное")

"""
Напишите функцию, которая принимает строку и возвращает количество гласных букв в этой строке. (решай в лоб)
"""

# def is_vowel(string):
#     num = 0
#     for char in string:
#         if char in 'aeiouy':
#             num += 1
#     return num
#
#
# result = is_vowel('vowel')
# print(result)
"""
Напишите функцию, которая проверяет, является ли строка палиндромом (то есть читается одинаково слева направо и справа 
налево).
"""

# def is_palindrome(word):
#     if word == word[::-1]:
#         return "Палиндром"
#     else:
#         return "Не палиндром"
#
#
# result = is_palindrome('ротор')
# print(result)

"""
Напишите функцию, которая принимает два числа (начало и конец диапазона) и возвращает список чисел, кратные 3 
или 5 в этом диапазоне. (хорошо решить через генератор внутри функции)
"""


def is_divisible(num1, num2):
    lst = []
    for i in range(num1, num2 + 1):
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)
    lst = [i for i in range(num1, num2 + 1) if i % 3 == 0 or i % 5 == 0] # слева от фора варианты, а справа фильтр
    return lst


result = is_divisible(1, 20)
print(result)
"""
Калькулятор
"""

# def sub(num1, num2):
#     num3 = num1 - num2
#     return num3
#
#
# def total(num1, num2):
#     num3 = num1 + num2
#     return num3
#
#
# def mult(num1, num2):
#     num3 = num1 * num2
#     return num3
#
#
# def div(num1, num2):
#     num3 = num1 / num2
#     return num3
#
#
# while True:
#     num1 = int(input("Число 1"))
#     num2 = int(input("Число 2"))
#     op = input("Оператор")
#     match op:
#         case "+":
#             result = total(num1, num2)
#         case "-":
#             result = sub(num1, num2)
#         case "*":
#             result = mult(num1, num2)
#         case "/":
#             result = div(num1, num2)
#         case _:
#             continue
#     print(result)


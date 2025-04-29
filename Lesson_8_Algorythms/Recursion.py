"""
Реализуйте рекурсивную функцию factorial(n), которая вычисляет факториал числа.
"""

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
#
# n = 1
# print(factorial(n))
"""
Напишите рекурсивную функцию fibonacci(n), которая возвращает n-е число Фибоначчи.
"""

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


"""
Создайте рекурсивную функцию sum_digits(n), которая принимает число и возвращает сумму его цифр.
"""

# def sum_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_digits(n // 10)


n = 12345

"""
Реализуйте рекурсивную функцию power(base, exp), которая возводит число base в степень exp.
"""

# def power(base, exp):
#     if exp == 0:
#         return 1
#     elif exp < 0:
#         return 1 / (base * power(base, -exp - 1))
#     return base * power(base, exp - 1)
#
#
# print(power(2, -2))

"""
Рекурсивная функция gcd(a, b), которая находит НОД двух чисел с использованием алгоритма Евклида.
"""

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# print(gcd(12, 8))

"""
Обратная строка
Напишите рекурсивную функцию для переворота строки (например, «hello» → «olleh»).
"""

# def rev(word):
#     if len(word) == 0:
#         return word
#     return word[-1] + rev(word[:-1])
#
#
# print(rev("olleh"))

"""
ДОМАШКА
Рекурсивная функция на проверку палиндрома
"""


def palindrome(word):
    if len(word) == 0:
        return True
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    return False


word = "пот"
print(palindrome(word))

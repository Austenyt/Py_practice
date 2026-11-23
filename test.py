# s = {1: 2}
# for key, value in s.items():
#     print(key, value)
#
#
# def compress_sequence(s):
#     c = 0
#     x = 0
#     dic = {}
#     new_list = []
#     for i in s:
#         if i not in dic:
#             dic = {}
#             new_list.append((tuple(s.items())[0]))
#         else:
#             dic[i] = x + 1
#         new_list.append(())
import math
from encodings.punycode import selective_find
from html.entities import name2codepoint


# s = "1222311"
# c = s[0]
# x = 1
# new_str = ""
# for ch in s[1:]:
#     if ch != c:
#         new_str += str((x, int(c))) + " "
#         c = ch
#         x = 1
#     else:
#         x += 1
# new_str += str((x, int(c)))
# print(new_str)


#             x += 1
#     else:
#         new_list.append((x, c))
#         c = ch
#         x = 1
#     new_list.append((x, c))
#     return new_list
#
#
# s = "1222311"
# print(compress_sequence(s))

# s = 'abcdefghij'
# width = 1
# service_s = ""
# new_s = ""
# for ch in s:
#     service_s += ch
#     if len(service_s) == width:
#         new_s += service_s + '\n'
#         service_s = ""
# if service_s:
#     new_s += service_s
# print(new_s.rstrip('\n'))


# n = 15
# new_list = []
# for i in range(1, n+1):
#     a = ''
#     if i % 3 == 0:
#         a += 'Fizz'
#     elif i % 5 == 0:
#         a += 'Buzz'
#         new_list.append(a)
#     else:
#         new_list.append(str(i))
# print(new_list)

# x = "ab"
# if 'a' in x:
#     print(1)
# if 'b' in x:
#     print(2)

# def find_median(input_string):
#     input_list = input_string.split(' ')
#     input_list.sort(key=int)
#     if len(input_list) % 2 != 0:
#         index = int(len(input_list) // 2)
#         a = int(input_list[index])
#     else:
#         index = int(len(input_list) / 2)
#         a = round((int(input_list[index]) + int(input_list[index - 1])) / 2, 2)
#     print(type(a))
#     return a
#
# input_string = '6 6'
# print(find_median(input_string))

# def is_palindrome(text):
#     new_text = text.lower()
#     print(new_text)
#     if new_text == new_text[::-1]:
#         return True
#     return False
# text = 'Racecar'
# print(is_palindrome(text))

# def is_palindrome(text):
#     new_text = text.lower()
#     if len(new_text) == 0:
#         print(new_text)
#         return True
#     if new_text[0] == new_text[-1]:
#         return is_palindrome(new_text[1:-1])
#     return False
#
# text = 'Racecar'
# print(is_palindrome(text))

# class Counter:
#     def __init__(self):
#         self.value = 0
#
#     def increase(self, amount=1):
#         self.value += amount
#
#     def decrease(self, amount=1):
#         self.value -= amount
#
#     def getValue(self):
#         return self.value
#
#
# counter = Counter()
# counter.decrease(10)
# counter.increase(15)
#
# print(counter.getValue())

# def move_zeroes(nums):
#     new_nums = []
#     zero_count = 0
#     for num in nums:
#         if num == 0:
#             zero_count += 1
#         else:
#             new_nums.append(num)
#     new_nums.extend([0] * zero_count)
#     return new_nums

# def move_zeroes(nums):
#     return [x for x in nums if x != 0] + [0] * nums.count(0)
#
# nums = [0, 1, 0, 3, 12]
# print(move_zeroes(nums))


# def is_divisible_by_digits(num):
#     num_str = str(num)
#     for n in num_str:
#         if int(n) != 0 and num % int(n) != 0:
#             return False
#     return True
#
# num = 128
# print(is_divisible_by_digits(num))

# def flat(arr):
#     new_arr = []
#     for item in arr:
#         if isinstance(item, (list, tuple)):
#             for i in item:
#                 new_arr.append(i)
#         else:
#             new_arr.append(item)
#     return new_arr
#
# arr = [(1, 2, 'a'), ('bb',), ('cc', 'dd', 1)]
# print(flat(arr))

# def even_chars(s):
#     new_s = ''
#     for i in s[::2]:
#         new_s += i
#     return new_s
#
#
# s = 'Hello'
# print(even_chars(s))


# def reverse_words(sentence):
#     return ' '.join(sentence.split()[::-1])
#
#
# sentence = 'a good   example'
# print(reverse_words(sentence))

# def is_happy_number(number):
#     new_string = str(number)
#     if len(new_string) % 2 != 0:
#         return False
#     half = len(new_string) // 2
#     prod_1 = 1
#     prod_2 = 1
#     for i_1 in new_string[:half]:
#         prod_1 *= int(i_1)
#     for i_2 in new_string[half:]:
#         prod_2 *= int(i_2)
#     return prod_1 == prod_2
#
#
# number = 6262
# print(is_happy_number(number))


# def score_of_string(s):
#     total = 0
#     for i, ch in enumerate(s[:-1]):
#         mid_total = abs(ord(s[i]) - ord(s[i + 1]))
#         total += mid_total
#     return total
#
#
# s = 'hello'
# print(score_of_string(s))


# def missing_number(nums):
#     nums.sort()
#     if nums[0] != 0:
#         return 0
#     prev = nums[0]
#     for num in nums[1:]:
#         if num == prev + 1:
#             prev = num
#     return prev + 1
#
#
# nums = [1, 2]
# print(missing_number(nums))

import calendar
from platform import python_revision


# def get_day_of_week(month, day, year):
#
#
# month = 8
# day = 5
# year = 2015
# print(get_day_of_week(month, day, year))


# class BankAccount:
#
#     def __init__(self, initial_balance=0):
#         if initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative")
#         self.balance = initial_balance
#
#     def get_balance(self):
#         return self.balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self.balance += amount
#         return self.balance
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive")
#         if self.balance < amount:
#             raise ValueError("Insufficient funds")
#         self.balance -= amount
#         return self.balance
#
#     def transfer(self, target_account, amount):
#         if not isinstance(target_account, BankAccount):
#             raise TypeError("Target must be a BankAccount")
#         self.withdraw(amount)
#         try:
#             target_account.deposit(amount)
#         except Exception:
#             self.deposit(amount)
#             raise
#         return self.balance
#
#
# sender = BankAccount(100)
# receiver = BankAccount()
#
# sender.deposit(50)
# # вернёт 150
#
# sender.withdraw(30)
# # # вернёт 120
# #
# sender.transfer(receiver, 20)
# # # вернёт 100
#
# print(receiver.get_balance())

# """Мини-проект магазина. Первый класс - Описывает товары в магазине. У продукта есть наименование, цена, кол-во. Методы
# get_product_info - информация о товаре, is_available - проверяет доступность товара, может ли пользователь купить товар
# и нужное кол-во в принципе. Второй класс магазин - название и продукты, который в магазине представлены. add_product,
# remove_product, find_product, get_products, get_available_products (получить список доступных продуктов, т.е. больше 0).
# 3 класс Корзина - на собственное усмотрение"""
# class Product:
#
#     def __init__(self, name, price, qty):
#         self.name = name
#         self.price = price
#         self.qty = qty
#
#     def get_product_info(self, name):
#         return f'Товар {name} продаётся по цене {self.price}'
#
#     def is_available(self, name):
#         if self.qty > 0:
#             return f'Товар {name} в наличии в количестве {self.qty}'
#         return f'Товара {name} нет в наличии'
#
#
# class Shop:
#
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#         self.available_products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def remove_product(self, product):
#         self.products.remove(product)
#
#     def find_product(self, product):
#         if product in self.products:
#             return product
#         else:
#             return f'Продукт {product.name} не найден'
#
#     def get_products(self):
#         return self.products
#
#     def get_available_products(self):
#         for product in self.products:
#             if product.qty > 0:
#                 self.available_products.append(product)
#         return self.available_products
#
# class Cart:
#
#     def __init__(self):
#         self.cart_products = []
#         self.cart_cost = []
#
#     def add_to_cart(self, product):
#         self.cart_products.append(product)
#
#     def remove_from_cart(self, product):
#         self.cart_products.remove(product)
#
#     def calculate_payment(self, product):
#         self.cart_cost = product.price * product.qty
#         return self.cart_cost
#
# product_1 = Product(name="Бананы", price=100, qty=50)
# product_2 = Product(name="Яблоки", price=80, qty=100)
# product_3 = Product(name="Апельсины", price=120, qty=30)
# shop_1 = Shop("Да")
# shop_1.add_product(product_1)
# shop_1.add_product(product_2)
# shop_1.add_product(product_3)
# prods = shop_1.get_products()
# for prod in prods:
#     print(prod.name, prod.price, prod.qty)


# from datetime import datetime, timedelta


# def add_days_to_date(date_str, offset):
#     new_date_str = datetime.strptime(date_str, '%Y-%m-%d').date() + timedelta(days=offset)
#     return datetime.strftime(new_date_str, '%Y-%m-%d')
#
# date_str = '2024-01-15'
# offset = 500
#
# print(add_days_to_date(date_str, offset))

# def validate_date(date_str, fmt):
#     try:
#         datetime.strptime(date_str, fmt).date()
#     except ValueError:
#         return 'ERROR'
#     return 'OK'
#
# date_str = '31.02.2024'
# fmt = '%d.%m.%Y'
# print(validate_date(date_str, fmt))

# def sum_excluding_multiples(n):
#     new_n = 0
#     for i in range(0, n + 1):
#         if i % 3 != 0 and i % 7 != 0:
#             new_n += i
#     return new_n
#
# n = 21
# print(sum_excluding_multiples(n))

# def contains_duplicate(nums):
#     return len(nums) != len(set(nums))
#
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# print(contains_duplicate(nums))

# def invert_dict(d):
#     return {value: key for key, value in d.items()}
#
# d = {'a': 1, 'b': 2, 'c': 3}
# print(invert_dict(d))

# def longest_run(s):
#     prev = ''
#     for i in s:
#         if
# s = 'aaabbcaaaa'
# print(longest_run(s))

# def generate_pascal_triangle(num_rows):
#     row_list = []
#     for num in range(0, num_rows + 1):
#
#
# num_rows = 4
# print(generate_pascal_triangle(num_rows))

num_rows = 9
new_list = []
for rows in range(1, num_rows + 1):
    new_list.append([row for row in range(1, rows + 1)])
    print(new_list)

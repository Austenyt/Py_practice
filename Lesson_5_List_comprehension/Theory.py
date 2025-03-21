"""
Создайте список чисел от 1 до 20
"""
# lst = []
# for i in range(1,21):
#     lst.append(i)
# print(lst)

# result = [c for c in range(1,21)]
# print(result)
#
# a = list(range(1,21))
# print(a)
"""
Создайте список четных чисел от 20 до 0
"""
# a = list(range(20,-1,-2))
# print(a)
"""
Создайте список из слов длиной более 3
"""
# words = ["cat", "elephant", "dog", "bird", "lion"]
# lst_2 = [el for el in words if len(el) > 3]
# print(lst_2)
"""
Создайте генератор списка, который генерирует квадраты нечетных чисел от 1 до 15.
"""
# result = [c**2 for c in range(1,16,2)]
# print(result)
"""
Создайте список отрицательных чисел
"""
# numbers = [-5, 3, -2, 9, 0, -1]
# numbers_2 =[num for num in numbers if num < 0]
# print(numbers_2)
"""
Создайте список, заменив число на "четный" или "нечетный"
"""
# numbers = [-5, 3, -2, 9, 0, -1]
# lst = ["четный" if num % 2 == 0 else "нечетный" for num in numbers]
# print(lst)

"""
Создайте генератор списка, который для чисел из списка увеличивает все значения больше 100 на 10%, а все 
остальные оставляет без изменений.
"""
# numbers = [50, 120, 200, 80, 150]
# numbers_2 = [num * 1.1 if num > 100 else num for num in numbers]
# print(numbers_2)

# 1. Кол-ва итераций
for _ in range(10):
    pass

# 2. Перебор значений
for el in "hello":
    pass

# 3. Перебор посл. чисел.
for num in range(1, 101, 2):
    pass

# 4. Перебор индексов
#      0  1   2      3     4
lst = [5, 8, -10, 'hello', 9]
for i in range(len(lst) - 1):
    print(lst[i],lst[i + 1])
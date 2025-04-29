# def binary_search(lst, a):
#
#     first = 0
#     last = len(lst) - 1
#     while last >= first:
#         av = (first + last) // 2
#         if lst[av] == a:
#             return av
#         elif a < lst[av]:
#             last = av - 1
#         else:
#             first = av + 1
#
#
# lst = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
# a = 13
# print(binary_search(lst, a))


"""
Дано отсортированное множество чисел, нужно найти, сколько из них не превосходят x.
def lst_sort(lst, x):
    count = 0
    for i in range(0, lst.index(x)):
        count += 1
    return count
"""

import bisect

#
#
# def lst_sort(lst, x):
#     left = 0
#     right = len(lst) - 1
#     while right >= left:
#         mid = (right + left) // 2
#         if lst[mid] == x:
#             return mid + 1
#         elif lst[mid] > x:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return None
#
#
# lst = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
# x = 10
# print(lst_sort(lst, x))
# print(bisect.bisect_left(lst, x) + 1)

"""
Дан отсортированный список чисел, который может содержать дубликаты. Нужно найти индекс первого вхождения элемента. 
Если элемент не найден, вернуть -1.

Пример:
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
Вывод:
1 (то есть самое первое вхождение числа 2 имеет индекс 1)
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
"""

# def first_in(arr, target):
#     left = 0
#     right = len(arr) - 1
#     a = -1
#     while right >= left:
#         mid = (right + left) // 2
#         if arr[mid] == target:
#             a = mid
#         if arr[mid] >= target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return a
#
#
# arr = [1, 2, 2, 2, 3, 3, 4, 4, 5]
# target = 4
# print(first_in(arr, target))

"""
Дан отсортированный список чисел, который может содержать дубликаты. Нужно найти индекс последнего вхождения элемента. 
Если элемент не найден, вернуть -1.

Пример:
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
Вывод:
3 (то есть самое последние вхождение числа 2 имеет индекс 3)
# def last_in(arr, target):
#     for i in range(0, len(arr)):
#         if arr[i] > target:
#             return i - 1
"""

# def last_in(arr, target):
#     left = 0
#     right = len(arr) - 1
#     a = -1
#     while right >= left:
#         mid = (right + left) // 2
#         if arr[mid] == target:
#             a = mid
#         if arr[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return a

#
# arr = [1, 2, 2, 2, 3, 3, 4, 4, 5]
# target = 2
# print(last_in(arr, target))

# arr = [1, 3, 4, 6, 8]
# x = 5
# bisect.insort_left(arr, x)
# print(arr)

"""
Вставить элемент в сортированный список с помощью бинарного поиска (элемента в списке изначально нет!)
"""


# def insert(arr, x):
#     left = 0
#     right = len(arr) - 1
#     while right >= left:
#         mid = (right + left) // 2
#         print(left, mid, right)
#         if arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     arr.insert(left, x)
#     return arr
#
#
# arr = [1, 3, 4, 6, 8]
# x = 5
# print(insert(arr, x))

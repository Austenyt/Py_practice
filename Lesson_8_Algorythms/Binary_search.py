# def binary_search(lst, a):
#     lst1 = lst[:int(len(lst) / 2)]
#     lst2 = lst[int(len(lst) / 2):]
#     if a in lst1:
#         min_a = min(lst1)
#         max_a = max(lst1)
#         av = (max_a - min_a) / 2
#     else:
#         min_a = min(lst2)
#         max_a = max(lst2)
#         av = (max_a - min_a) / 2
#     return lst1
#
#
# lst = [5, 2, 8, 7, 1, 6, 4, 3]
# a = 6
# print(binary_search(lst, a))
lst = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
a = 10
b = len(lst)
min_a = 0
max_a = 0
while min_a < a < max_a:
    first = lst[0]
    last = lst[int(len(lst)) - 1]
    av = lst[len(lst) // 2]
    lst = lst[:av]
    if a in lst:dfdf

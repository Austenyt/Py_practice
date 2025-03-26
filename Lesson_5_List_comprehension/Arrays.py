"""
Диагональ матрицы: Создайте список, состоящий из диагонали квадратной матрицы (список списков).
"""
# [1, 4, 7],
# [2, 5, 8],
# [3, 6, 9]
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# l_str = [matrix[i][i] for i in range(len(matrix))] # Прямая диагональ
# l = [matrix[i][len(matrix[i]) - 1 - i] for i in range(len(matrix))] # Обратная диагональ
# print(l_str)
# print(l)
"""
Даны два списка, создать третий, сложив элементы по индексам.
"""
# lst_1 = [1,2,3]
# lst_2 = [4,5,6]
# lst_3 = [lst_1[i] + lst_2[i] for i in range(len(lst_1))]
# print(lst_3)
"""
Даны два списка, сложить их элементы по индексам, но брать элементы из второго списка в обратном порядке.
lst_1 = [1, 2, 3, 4]
lst_2 = [5, 6, 7, 8]

результат = [9, 9, 9, 9]
"""
# lst_1 = [1, 2, 3, 4]
# lst_2 = [5, 6, 7, 8]
# lst_3 = [lst_1[i] + lst_2[-i-1] for i in range(len(lst_1))]
# print(lst_3)
"""
Даны две квадратные матрицы одинаковой размерности, нужно их сложить в новую матрицу.
"""
# array_1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# array_2 = [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
# array_3 = [[array_1[i-i+j][i] + array_2[i-i+j][i] for i in range(len(array_1))] for j in range(len(array_1))]
# for i in array_3:
#     print(i)
"""
Дана матрица, вывести обе её диагонали задом наперед (2 for или 2 генератора)
допустим матрица от 1 до 9
результат:
9 5 1
7 5 3
"""
# array = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# lst_1 = [array[2-i][2-i] for i in range(len(array))]
# lst_2 = [array[2-i][i] for i in range(len(array))]
# print(lst_1)
# print(lst_2)
"""
Транспонировать матрицу.
"""
# array = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# array_1 = [[array[i][i-i+j] for i in range(len(array))] for j in range(len(array))]
# for i in array_1:
#     print(i)

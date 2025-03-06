"""
███████╗ ██████╗ ██████╗     ██╗      ██████╗  ██████╗ ██████╗
██╔════╝██╔═══██╗██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
█████╗  ██║   ██║██████╔╝    ██║     ██║   ██║██║   ██║██████╔╝
██╔══╝  ██║   ██║██╔══██╗    ██║     ██║   ██║██║   ██║██╔═══╝
██║     ╚██████╔╝██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝

Цикл for используется для перебора элементов и выполнения
действий с каждым элементом в последовательности.

Примеры последовательностей:

  тип  |                 определение                      | написание
______________________________________________________________________
str    |  последовательность символов                     |   ""
list   |  изменяемая последовательность значений          |   []
tuple  |  неизменяемая последовательность значений        |   ()
range  |  функция, генерирующая последоватнльность чисел  | range()

"""

"""
███████╗████████╗ █████╗  ██████╗ ███████╗     ██╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝    ███║
███████╗   ██║   ███████║██║  ███╗█████╗      ╚██║
╚════██║   ██║   ██╔══██║██║   ██║██╔══╝       ██║
███████║   ██║   ██║  ██║╚██████╔╝███████╗     ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚═╝

██████╗  █████╗ ███╗   ██╗ ██████╗ ███████╗       
██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██╔════╝       
██████╔╝███████║██╔██╗ ██║██║  ███╗█████╗         
██╔══██╗██╔══██║██║╚██╗██║██║   ██║██╔══╝         
██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗       
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝       


1. Вывести все числа от 1 до 10.
"""
# for i in range(1,11):
#     print(i)
"""
2. Вывести все числа от 10 до 1.
"""
# for i in range(10,0,-1):
#     print(i)
"""
3. Вывести все четные числа от 1 до 20.
"""
# for i in range(2,21,2):
#     print(i)
"""
4. Вывести все нечетные числа от 1 до 20.
"""
# for i in range(1,20,2):
#      print(i)
"""
5. Посчитать сумму чисел от 1 до 100.
(Сумму стоит считать в отдельной переменной,
созданной до цикла)
"""
# s = 0
# for i in range(1,101):
#     s += i
# print(s)
"""
6. Вывести все числа от 1 до 50, которые делятся на 3.
"""
# for i in range(1,51):
#     if i // 3  == i / 3:
#         print(i)
"""
7. Посчитать количество чисел от 1 до 100, которые делятся на 5.
(Кол-во тоже нужно считать в отдельной переменной,
созданной до цикла)
"""
# q = 0
# for i in range(1,101):
#     if i // 5 == i / 5:
#         q += 1
# print(q)
"""
8. Вывести квадрат каждого числа от 1 до 10.
"""
# for i in range(1,11):
#     print(i**2)
"""
9. Вывести куб каждого числа от 1 до 10.
"""
# for i in range(1,11):
#     print(i**3)
"""
10. Посчитать сумму всех чисел от 1 до 100, которые делятся на 7.
"""
# s = 0
# for i in range(1,101):
#     if i // 7 == i / 7:
#         s += i
# print(s)
"""
11. Вывести числа от 1 до 100, но вместо чисел, делящихся на 3, 
вывести "Fizz", а вместо чисел, делящихся на 5, вывести "Buzz".
"""
# for i in range(1,101):
#     if i // 3 == i / 3:
#         print("Fizz")
#     elif i // 5 == i / 5:
#         print("Buzz")
#     else:
#         print(i)
"""
12. Найти наибольшее число среди всех чисел от 1 до 100.
Максимальное число (как и минимальное), нужно сохранять
в отдельную переменную и сравнивать остальные с этой
переменной.
"""
# M = 0
# for i in range (1,101):
#     if i > M:
#         M = i
# print(M)
"""
13. Найти наименьшее число среди всех чисел от 1 до 100.
"""
# m = 1
# for i in range (2,101):
#     if i < m:
#         m = i
# print(m)
"""
14. Вывести все числа от 1 до 100, которые являются простыми.
Простые числа те, которые делятся только на 1 и на само себя
или другими словами не делятся на другие числа, кроме 1 и себя.
"""
# for i in range (1,101):
#     if i % i == 0:
#         print(i)
"""
15. Вывести таблицу умножения для числа 5.
Формат:
5 x 1 = 5
5 x 2 = 10
...
"""
# for i in range(1,11):
#     print(f'5 x {i} = {5*i}')
"""
16. Посчитать количество чисел от 1 до 100, которые делятся на 3 или 5.
"""
# n = 0
# for i in range(1,101):
#     if i // 3 == i / 3 or i // 5 == i / 5:
#         n += 1
# print(n)
"""
17. Вывести все числа от 1 до 50, которые не делятся на 2 и на 3.
"""
# for i in range(1,51):
#     if i // 2 != i / 2 and i // 3 != i / 3:
#         print(i)
"""
18. Найти сумму чисел от 1 до 50, которые делятся на 4, но не на 6.
"""
# s = 0
# for i in range(1,51):
#     if i // 4 == i / 4 and i // 6 != i / 6:
#         s += i
# print(s)
"""
19. Создать список чисел от 1 до 10 и вывести его элементы в обратном порядке.
Изначально создаем пустой список и добавляем в него элементы.
"""
# lst = []
# for i in range(1,11):
#    lst.append(i)
# print(lst[::-1])

"""
20. Посчитать сумму всех четных чисел от 1 до 100.
"""
# s = 0
# for i in range(1,101):
#     if i // 2 == i / 2 :
#         s += i
# print(s)
"""
███████╗████████╗ █████╗  ██████╗ ███████╗    ██████╗                       
██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝    ╚════██╗                      
███████╗   ██║   ███████║██║  ███╗█████╗       █████╔╝                      
╚════██║   ██║   ██╔══██║██║   ██║██╔══╝      ██╔═══╝                       
███████║   ██║   ██║  ██║╚██████╔╝███████╗    ███████╗                      
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚══════╝                      

███████╗███████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗ ██████╗███████╗███████╗
██╔════╝██╔════╝██╔═══██╗██║   ██║██╔════╝████╗  ██║██╔════╝██╔════╝██╔════╝
███████╗█████╗  ██║   ██║██║   ██║█████╗  ██╔██╗ ██║██║     █████╗  ███████╗
╚════██║██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝  ╚════██║
███████║███████╗╚██████╔╝╚██████╔╝███████╗██║ ╚████║╚██████╗███████╗███████║
╚══════╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝


21. Создать список чисел от 1 до 10 и вывести их в виде строки.
"""
# lst = []
# string = ''
# for i in range(1,11):
#    lst.append(i)
# for l in lst:
#     string += str(l)
# print(string)
"""
22. Создать строку из всех чисел от 1 до 100, разделенных пробелами.
"""
# s = ""
# for i in range(1,101):
#     s += str(i) + " "
# print(s.strip())

"""
23. Создать список из первых 10 квадратных чисел и вывести его.
"""
# lst = []
# for i in range(1,11):
#    lst.append(i**2)
# print(lst)
"""
24. Создать список из 10 случайных чисел от 1 до 100.
Случайные числа можно сгенерировать модулем random
random.randint(1, 100) - выберет случайное число от 1 до 100
"""
# import random
# lst = []
# for i in range(1,11):
#     lst.append(random.randint(1, 100))
# print(lst)
"""
25. Проверить, есть ли в списке из 10 случайных чисел число 50.
Конечно список случайных чисел нужно сначала создать.
"""
# import random
# lst = []
# for i in range(1,11):
#     lst.append(random.randint(1, 100))
# if 50 in lst:
#     print(lst)
#     print("Число 50 в списке")
# else:
#     print(lst)
#     print("Попробуйте снова")
"""
26. Проверить, содержится ли в списке хотя бы одно четное число.
"""
# lst = [7, 33, 1, 5, 9, 23, 87, 13, 78, 99]
# for l in lst:
#     if l // 2 == l / 2:
#         print(f'В списке содержится по крайней мере одно четное число, и это число {l}')
"""
27. Проверить, является ли каждый элемент списка чисел четным.
"""
# lst = [2, 6, 32, 4, 22]
# s = 0
# for l in lst:
#     if l // 2 == l / 2:
#         s += 1
# if s == len(lst):
#     print("Каждый элемент списка является четным")
# else:
#     print("В списке есть нечетные числа")
"""
28. Посчитать количество гласных букв в строке.
"""
# s = "Каждый день я пишу код на питоне!"
# n = 0
# lst = ["а", "е", "и", "о", "у", "э", "ю", "я"]
# for i in s:
#     if i in lst:
#         n += 1
# print(n)
"""
29. Создать список чисел от 1 до 100, а затем 
создать новый список с их квадратами.
"""
# lst = []
# for i in range(1,101):
#     lst.append(i)
# print(lst)
# lst = []
# for i in range(1,101):
#     lst.append(i**2)
# print(lst)
"""
*30. Посчитать количество чисел, которые 
являются палиндромами, среди чисел от 1 до 1000.
"""
# s = ''
# n = 0
# for i in range(1,1001):
#     s = str(i)
#     if str(i) == s[::-1]:
#         n += i
# print(n)
"""
*31. Найти все пары чисел от 1 до 100, сумма которых равна 100.
"""
# for i in range(1,101):
#     if i <= 50:
#         print(f'{i}, {100 - i}')
"""
*32. Создать программу, которая выводит таблицу 
умножения для всех чисел от 1 до 10.
"""
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i * j}')

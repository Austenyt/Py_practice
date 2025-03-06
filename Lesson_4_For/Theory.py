# range - генератор последовательности чисел

# print(list(range(1, 101)))
# print(list(range(1, 101, 2)))


#
#  ----------------------------------------------------
#                -2 -1 0  1  2  3  4  5  6  7  8  9 10

# range(10) - (конец) 0 ... 9 (c 0, шаг - 1)
print(list(range(10)))
# range(5, 10) - (начало, конец) 5 ... 9
print(list(range(5, 10)))
# range(2, 11, 2) (начало, конец, шаг) 2, 4, 6, 8, 10
print(list(range(2, 11, 2)))


# for - цикл (с параметром) перебирающий последовательности
# последовательности
# str
# list
# tuple


for n in range(2, 11, 2):  # 5 итер
  print(n)

for char in "Hello world!":  # 11 итер
  print(char*5)

for el in (1, 5, 2, "hello"):  # 4 итер
  print(el*5)

for _ in range(100):  # 0 ... 99 (100 итер)
  print("sheep")

n = int(input())
s = 0

for i in range(1, n+1):
  s += i

print(s)




# рекурсия (стек вызова функций)
# функции генераторы
# декораторы
# декораторы с параметрами
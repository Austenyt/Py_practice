# Последовательности
# str - последовательность символов
#    01234
#
#        l  l  o h  e  l  l  o
#----------------|----------------
#       -3 -2 -1 0  1  2  3  4  5
#
# s = "hello"
# print(s[0])
# print(s[-2])
# print(s[1:5])
# print(s[1:])
# print(s[0:3])
# print(s[:3])
# print(s[::2])
# print(s[::-1])


# tuple - последовательность значений
# t = (5, -2.3, 'hello', [1, 2, 3])
#    0  1  2
#
# t = (5, 3, 2)
# print(t[1])
# print(t[1:])

# list - последовательность значений
# l = [5, 3, 2]
# print(l[1])
# l[0] = 255
# print(l)
# print(l[::-1])

# s = 'Hello world!'
# i = s.find("r")
# print(s[:i])
# print(s[i:])

s = "hello world"
print(s[0])
print(s[-2])
print(s[1:5])
print(s[1:])
print(s[0:3])
print(s[:3])
print(s[::2])
print(s[::-1])
print(s[1:-1])
print(s[1::2])
print(s[::-1])
print(s[::-2])

# s = input()
#
# if s == s[::-1]:
#     print("ok")
# else:
#     print("nok")

# s = input()
#
# i = s.find(" ")
# print(s[i+1:] + " " + s[:i])

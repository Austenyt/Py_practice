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

class Counter:
    def __init__(self):
        self.value = 0

    def increase(self, amount=1):
        self.value += amount

    def decrease(self, amount=1):
        self.value -= amount

    def getValue(self):
        return self.value


counter = Counter()
counter.decrease(10)
counter.increase(15)

print(counter.getValue())

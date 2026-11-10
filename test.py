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


def score_of_string(s):
    total = 0
    for i, ch in enumerate(s[:-1]):
        mid_total = abs(ord(s[i]) - ord(s[i + 1]))
        total += mid_total
    return total


s = 'hello'
print(score_of_string(s))

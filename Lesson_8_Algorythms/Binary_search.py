def binary_search(lst, a):

    first = 0
    last = len(lst) - 1
    while last >= first:
        av = (first + last) // 2
        if lst[av] == a:
            return av
        elif a < lst[av]:
            last = av - 1
        else:
            first = av + 1


lst = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
a = 13
print(binary_search(lst, a))

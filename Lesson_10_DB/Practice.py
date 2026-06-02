a = []
n = int(input("Введите число\n"))
for i in range(n+1):
    if i % 3 == 0 and i % 5 == 0:
        a.append("FizzBuzz")
    elif i % 3 == 0:
        a.append("Fizz")
    elif i % 5 == 0:
        a.append("Buzz")
    else:
        a.append(i)
print(a)

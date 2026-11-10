"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""


# def basic_op(operator, value1, value2):
#     d = {
#         "+": operator.add,
#         "-": operator.sub,
#         "*": operator.mul,
#         "/": operator.truediv,
#     }
#     return d[operator](value1, value2)

def points(games):
    total = 0
    for game in games:
        x = game.split(":")[0]
        y = game.split(":")[1]
        if int(x) > int(y):
            total += 3
        elif int(x) == int(y):
            total += 1
    return total


print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))

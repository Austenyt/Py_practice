# Коллекции
# типы данных, в которых несколько значений
#
# 1. Последовательности
# упорядоченные типы данных
# 1.1 Индексация
# 1.2 Итерабельность
#
# str
# list
# tuple
#
# 2. Неуп. коллекции
# 1. Нет индексов
# set - множество
# - коллекция неупорядоченных уникальных элементов
# dict - словарь
# 1. Ключи

# использование set
#lst = [1, 2, 3, 3, 5, 6, 1, 2, 7]
#print(lst)
#s = set(lst)
#print(s)


#for el in s:
#    print(el)

words = {
    'one': 'один',
    'two': 'два',
    'ten': 10
}
print(words.keys())
print(words.values())
print(words.items())

for k, v in words.items():
    print(k, ":", v)

for d in words:
    print(d, ":", words[d])

print(words['one'])
words['two'] = 2
words['nine'] = 9
print(words)
print(words.get("seven"))

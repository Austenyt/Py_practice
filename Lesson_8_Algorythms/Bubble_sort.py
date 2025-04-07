def bubble_sort(lst):
    i, j = 0, 1 # пара индексов с начала списка
    last = len(lst) # индекс последнего сортированного элемента
    while i != last: # пока первый элемент остается несортированным
        if lst[i] > lst[j]: # проверка наибольшего в паре
            lst[i], lst[j] = lst[j], lst[i] # переприсваивание значений, сдвиг слева направо
        i += 1 # берем следующую пару
        j += 1
        if j == last: # если дошли до последнего сортированного элемента
            i, j = 0, 1 # возвращаемся в начало списка
            last -= 1 # сокращаем длину поиска
    return lst


lst = [5, 2, 8, 7, 1, 6, 4, 3]
print(bubble_sort(lst))

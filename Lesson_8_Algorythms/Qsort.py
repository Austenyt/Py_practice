def qsort(arr, left, right):
    if left < right:
        p = arr[right]
        i = left - 1
        for j in range(left, right + 1):
            if arr[j] <= p:
                i = i + 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
        qsort(arr, left, i - 1)
        qsort(arr, i, right)


arr = [5, 2, 8, 7, 1, 6, 4, 3]
left = 0
right = len(arr) - 1
qsort(arr, left, right)
print(arr)

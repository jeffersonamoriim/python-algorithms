import numpy as np

def partition(array, start, end):
    pivot = array[end]
    i = start - 1 

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]

    return i + 1

def quick_sort(array, start, end):
    if start < end:
        position = partition(array, start, end)
        # Esquerda
        quick_sort(array, start, position - 1)
        # Direito
        quick_sort(array, position + 1, end)
    return array

array = np.array([9, 8, 7 , 6, 5 , 4, 3, 2, 1])

print(quick_sort(array, 0, len(array) - 1))
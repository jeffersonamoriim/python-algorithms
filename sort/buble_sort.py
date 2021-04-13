import numpy as np


def bubble_sort(array):
    n = len(array)

    # the n is the times of algoritm to run into array
    for i in range(n):
        # j is for comparission item to item into a i pass
        # n - i - 1 to dont run into already sorted indexes
        for j in range(0, n - i - 1):
            # if right item is greater then left item
            if array[j] > array[j + 1]:
                # greater item on temp
                temp = array[j]
                # the item on left now receive item from right (lower)
                array[j] = array[j + 1]
                # the item on right now is the greater
                array[j + 1] = temp
    return array

print(bubble_sort(np.array([1, 34, 8, 3])))

print(bubble_sort(np.array([9, 8, 7 , 6, 5 , 4, 3, 2, 1])))
import numpy as np

def selection_sort(array):
    n = len(array)

    # the n is the times of algoritm to run into array
    for i in range(n):
        # the min value aways start on i
        min_index = i
        # the start of array was the minimum values, so the algoritm runs
        # after min indexes already ordered
        for j in range(i + 1, n):
            # if the value on min index if greater then then the compared
            if array[min_index] > array[j]:
                # now the min value is this value
                min_index = j
        # finnaly the i index (start after already compared) is temp (to save him)
        temp = array[i]
        # the start have now min item 
        array[i] = array[min_index]
        # trade position with item that was on start (i)
        array[min_index] = temp
    
    return array

print(selection_sort(np.array([1, 34, 8, 3])))

print(selection_sort(np.array([9, 8, 7 , 6, 5 , 4, 3, 2, 1])))
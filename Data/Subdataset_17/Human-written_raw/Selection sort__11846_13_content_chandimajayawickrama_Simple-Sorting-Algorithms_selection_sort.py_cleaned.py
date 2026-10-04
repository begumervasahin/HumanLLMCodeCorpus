import time
import random
def selection_sort(array):
    start_time = time.time()
    for i in range(0,len(array)-1):
        position = i
        for j in range(i+1,len(array)):
            if array[position] > array[j]:
                position = j
        array[i],array[position] = array[position],array[i]
    return array
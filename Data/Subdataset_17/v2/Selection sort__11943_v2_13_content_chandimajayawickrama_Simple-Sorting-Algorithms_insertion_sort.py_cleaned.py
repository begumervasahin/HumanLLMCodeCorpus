import time
import random
def insertion_sort(array):
    start_time = time.time()
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    end_time = time.time()
    elapsed_time = end_time - start_time
    return array, elapsed_time
random_list = [random.randint(0, 100) for _ in range(10)]
print("Original list:", random_list)
sorted_list, elapsed_time = insertion_sort(random_list)
print("Sorted list:", sorted_list)
print("Time taken to sort:", elapsed_time, "seconds")
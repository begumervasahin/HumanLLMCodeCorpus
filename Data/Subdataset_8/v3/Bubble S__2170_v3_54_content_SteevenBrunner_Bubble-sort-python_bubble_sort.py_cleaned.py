import random
from time import time
list_length = 10000
max_value = 10000
unsorted_list = random.sample(range(1, max_value + 1), list_length)
def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    return arr
unsorted_list_copy = unsorted_list[:]
start_time = time()
bubble_sort(unsorted_list_copy)
end_time = time()
print(f"Bubble sort took {end_time - start_time:.6f} seconds to sort a list of {list_length} items.")
unsorted_list_copy = unsorted_list[:]
start_time = time()
unsorted_list_copy.sort()
end_time = time()
print(f"System Python sort (Timsort) took {end_time - start_time:.6f} seconds to sort a list of {list_length} items.")
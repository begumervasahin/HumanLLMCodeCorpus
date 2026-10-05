import random
from time import time
max_range = 10001
unsorted_list = random.sample(range(1, max_range), max_range - 1)
def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    return arr
unsorted_list_bubble = unsorted_list[:]
start_bubble = time()
bubble_sort(unsorted_list_bubble)
time_bubble = time() - start_bubble
print(f"Bubble sort: {time_bubble} seconds to sort a list of {max_range - 1} items.")
unsorted_list_system = unsorted_list[:]
start_system = time()
unsorted_list_system.sort()
time_system = time() - start_system
print(f"System sort (Timsort): {time_system} seconds to sort a list of {max_range - 1} items.")
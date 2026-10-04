import random
from time import time
MAX_RANGE = 10001
unsorted_list = random.sample(range(1, MAX_RANGE), MAX_RANGE - 1)
def bubble_sort(input_list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                is_sorted = False
    return input_list
unsorted_list_cpy = unsorted_list[:]
start = time()
bubble_sort(unsorted_list_cpy)
bubble_sort_time = time() - start
print(f"Bubble sort algorithm ends in {bubble_sort_time:.4f} seconds to sort a list of {MAX_RANGE - 1} items.")
unsorted_list_cpy = unsorted_list[:]
start = time()
unsorted_list_cpy.sort()
timsort_time = time() - start
print(f"System Python sort() Timsort algorithm ends in {timsort_time:.4f} seconds to sort a list of {MAX_RANGE - 1} items.")
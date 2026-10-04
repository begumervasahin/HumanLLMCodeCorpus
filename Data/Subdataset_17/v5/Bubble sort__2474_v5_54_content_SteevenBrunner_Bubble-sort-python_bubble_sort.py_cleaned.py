import random
from time import time
MAX_RANGE = 10001
unsorted_list = random.sample(range(1, MAX_RANGE), MAX_RANGE - 1)
def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        is_sorted = True
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                is_sorted = False
        if is_sorted:
            break
    return input_list
def measure_sort_time(sort_func, data, sort_name):
    data_copy = data[:]
    start_time = time()
    sort_func(data_copy)
    elapsed_time = time() - start_time
    print(f"{sort_name} algorithm ends in {elapsed_time:.4f} seconds to sort a list of {len(data)} items.")
    return elapsed_time
bubble_sort_time = measure_sort_time(bubble_sort, unsorted_list, "Bubble sort")
timsort_time = measure_sort_time(sorted, unsorted_list, "System Python sort() (Timsort)")
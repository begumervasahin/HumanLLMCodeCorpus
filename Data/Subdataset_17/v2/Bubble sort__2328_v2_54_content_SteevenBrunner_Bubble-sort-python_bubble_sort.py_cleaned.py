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
def measure_time(sort_function, data):
    start = time()
    sort_function(data)
    return time() - start
if __name__ == "__main__":
    bubble_sort_list = unsorted_list.copy()
    bubble_sort_time = measure_time(bubble_sort, bubble_sort_list)
    print(f"Bubble sort algorithm ends in {bubble_sort_time:.3f} seconds to sort a list of {MAX_RANGE - 1} items.")
    timsort_list = unsorted_list.copy()
    timsort_time = measure_time(timsort_list.sort, timsort_list)
    print(f"System Python sort() Timsort algorithm ends in {timsort_time:.3f} seconds to sort a list of {MAX_RANGE - 1} items.")
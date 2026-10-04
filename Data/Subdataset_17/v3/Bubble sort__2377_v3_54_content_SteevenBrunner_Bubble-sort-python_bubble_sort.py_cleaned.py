import random
from time import time
MAX_RANGE = 10001
unsorted_list = random.sample(range(1, MAX_RANGE), MAX_RANGE - 1)
def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True
        if not swapped:
            break
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
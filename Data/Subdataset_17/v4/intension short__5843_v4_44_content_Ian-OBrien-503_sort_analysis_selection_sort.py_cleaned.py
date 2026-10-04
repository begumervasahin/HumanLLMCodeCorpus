import numpy as np
import time
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
def measure_execution_time(arr, description):
    start_time = time.perf_counter()
    selection_sort(arr)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"\n{arr}\n\n{execution_time:.6f} seconds for selection sort on {description} array of size: {len(arr)}\n")
arr_length = 40
random_arr = np.random.randint(0, 99999, arr_length)
measure_execution_time(random_arr.copy(), "random order")
ascending_arr = np.sort(random_arr)
measure_execution_time(ascending_arr.copy(), "ascending order")
reverse_arr = np.sort(random_arr)[::-1]
measure_execution_time(reverse_arr.copy(), "reverse order")
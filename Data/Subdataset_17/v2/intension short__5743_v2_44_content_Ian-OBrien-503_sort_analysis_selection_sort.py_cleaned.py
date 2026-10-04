import numpy as np
import time
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def measure_execution_time(arr):
    start_time = time.perf_counter()
    sorted_arr = selection_sort(arr.copy())
    end_time = time.perf_counter()
    return sorted_arr, end_time - start_time
def display_sort_results(order_description, arr_length, exec_time):
    print(f"Execution time for selection sort ({order_description}) && ARR_SIZE: {arr_length} -> {exec_time:.6f} seconds\n")
def main():
    arr_length = 40
    random_array = np.random.randint(0, 99999, arr_length)
    sorted_array, execution_time = measure_execution_time(random_array)
    display_sort_results("Random Order", arr_length, execution_time)
    ascending_array = np.sort(random_array)
    sorted_array, execution_time = measure_execution_time(ascending_array)
    display_sort_results("Ascending Order", arr_length, execution_time)
    reverse_array = np.sort(random_array)[::-1]
    sorted_array, execution_time = measure_execution_time(reverse_array)
    display_sort_results("Reverse Order", arr_length, execution_time)
if __name__ == "__main__":
    main()
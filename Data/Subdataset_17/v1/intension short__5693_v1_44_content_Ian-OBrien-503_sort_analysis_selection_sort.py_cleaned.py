import numpy as np
import time
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def time_selection_sort(arr):
    start = time.perf_counter()
    sorted_arr = selection_sort(arr.copy())
    end = time.perf_counter()
    return sorted_arr, end - start
def main():
    arr_length = 40
    arr_random = np.random.randint(0, 99999, arr_length)
    sorted_arr, exec_time = time_selection_sort(arr_random)
    print("Sorted array (Random Order):", sorted_arr)
    print(f"\n{exec_time:.6f} seconds of execution for selection sort (Random Order) && ARR_SIZE: {arr_length}\n")
    arr_ascending = np.sort(arr_random)
    sorted_arr, exec_time = time_selection_sort(arr_ascending)
    print("Sorted array (Ascending Order):", sorted_arr)
    print(f"\n{exec_time:.6f} seconds of execution for selection sort (Ascending Order) && ARR_SIZE: {arr_length}\n")
    arr_reverse = np.sort(arr_random)[::-1]
    sorted_arr, exec_time = time_selection_sort(arr_reverse)
    print("Sorted array (Reverse Order):", sorted_arr)
    print(f"\n{exec_time:.6f} seconds of execution for selection sort (Reverse Order) && ARR_SIZE: {arr_length}\n")
if __name__ == "__main__":
    main()
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
def measure_execution_time(arr, sort_function):
    start_time = time.perf_counter()
    sorted_arr = sort_function(arr.copy())
    end_time = time.perf_counter()
    return sorted_arr, end_time - start_time
def display_execution_time(description, arr_length, exec_time):
    print(f"Execution time for selection sort ({description}) - ARR_SIZE: {arr_length} -> {exec_time:.6f} seconds\n")
def generate_array(length, order="random"):
    arr = np.random.randint(0, 99999, length)
    if order == "ascending":
        return np.sort(arr)
    elif order == "descending":
        return np.sort(arr)[::-1]
    return arr
def main():
    arr_length = 40
    random_array = generate_array(arr_length)
    sorted_array, exec_time = measure_execution_time(random_array, selection_sort)
    display_execution_time("Random Order", arr_length, exec_time)
    ascending_array = generate_array(arr_length, order="ascending")
    sorted_array, exec_time = measure_execution_time(ascending_array, selection_sort)
    display_execution_time("Ascending Order", arr_length, exec_time)
    descending_array = generate_array(arr_length, order="descending")
    sorted_array, exec_time = measure_execution_time(descending_array, selection_sort)
    display_execution_time("Descending Order", arr_length, exec_time)
if __name__ == "__main__":
    main()
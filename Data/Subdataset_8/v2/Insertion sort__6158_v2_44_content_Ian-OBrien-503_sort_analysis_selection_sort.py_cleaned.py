import random
import numpy as np
import time
def selection_sort(arr):
    start_time = time.process_time()
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end_time = time.process_time()
    execution_time = end_time - start_time
    return execution_time
def main():
    arr_length = 40
    arr = np.random.randint(0, 99999, arr_length)
    print("Random order:")
    print("Before sorting:", arr)
    execution_time = selection_sort(arr)
    print("After sorting:", arr)
    print("Execution time:", execution_time, "seconds")
    print("\nAscending order:")
    arr.sort()
    print("Before sorting:", arr)
    execution_time = selection_sort(arr)
    print("After sorting:", arr)
    print("Execution time:", execution_time, "seconds")
    print("\nReverse order:")
    arr = arr[::-1]
    print("Before sorting:", arr)
    execution_time = selection_sort(arr)
    print("After sorting:", arr)
    print("Execution time:", execution_time, "seconds")
if __name__ == "__main__":
    main()
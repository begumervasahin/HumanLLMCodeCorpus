import time
from random import randint
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def run_quicksort_performance_tests():
    print("Quick sort performance test:")
    input_sizes = [100000, 1200000, 2300000, 3400000, 4500000, 5600000, 6700000, 7800000, 8900000, 10000000]
    for i, input_size in enumerate(input_sizes, start=1):
        randlist = [randint(1, input_size) for _ in range(input_size)]
        print(f"Running test {i} for input size: {input_size}")
        start_time = time.time()
        quick_sort(randlist, 0, len(randlist) - 1)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.5f} seconds\n")
if __name__ == "__main__":
    run_quicksort_performance_tests()
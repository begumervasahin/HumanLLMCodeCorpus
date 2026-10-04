import time
from random import randint
def partition(arr, low, high):
    i = low - 1
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
def benchmark_quick_sort():
    input_sizes = [100000, 1200000, 2300000, 3400000, 4500000, 5600000, 6700000, 7800000, 8900000, 10000000]
    rand_lists = [generate_random_list(size) for size in input_sizes]
    for i, size in enumerate(input_sizes):
        print(f"Clock {i+1} is ticking for input size {size}...")
        start_time = time.time()
        quick_sort(rand_lists[i], 0, len(rand_lists[i]) - 1)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken for InputSize({size}) is {time_taken:.2f} seconds")
def generate_random_list(size):
    return [randint(1, size) for _ in range(size)]
if __name__ == "__main__":
    print("Quick Sort Benchmarking")
    benchmark_quick_sort()
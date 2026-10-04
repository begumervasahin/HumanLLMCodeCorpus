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
def main():
    print("Quick Sort Benchmarking")
    input_sizes = [100000, 1200000, 2300000, 3400000, 4500000, 5600000, 6700000, 7800000, 8900000, 10000000]
    rand_lists = [[] for _ in input_sizes]
    start_times = [0] * len(input_sizes)
    end_times = [0] * len(input_sizes)
    for i, size in enumerate(input_sizes):
        rand_lists[i] = [randint(1, size) for _ in range(size)]
        print(f"Clock {i+1} is ticking for input size {size}...")
        start_times[i] = time.time()
        quick_sort(rand_lists[i], 0, len(rand_lists[i]) - 1)
        end_times[i] = time.time()
        time_taken = end_times[i] - start_times[i]
        print(f"Time taken for InputSize({size}) is {time_taken:.2f} seconds")
if __name__ == "__main__":
    main()
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
print("Quick Sort Comparison for Various Input Sizes\n")
random_lists = [[] for _ in range(10)]
start_times = [[] for _ in range(10)]
end_times = [[] for _ in range(10)]
input_size = 100000
i = 0
while input_size <= 10000000:
    for _ in range(input_size):
        num = randint(1, input_size)
        random_lists[i].append(num)
    print(f"Sorting {input_size} elements...")
    start_times[i] = time.time()
    quick_sort(random_lists[i], 0, len(random_lists[i]) - 1)
    end_times[i] = time.time()
    print(f"Time taken for Input Size {input_size}: {end_times[i] - start_times[i]:.6f} seconds\n")
    input_size += 1100000
    i += 1
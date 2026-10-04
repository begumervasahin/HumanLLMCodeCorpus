import time
import random
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > current_value:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = current_value
array_sizes = [2000, 8000, 32000, 128000, 512000, 1024000, 4096000]
for size in array_sizes:
    arr = [random.randint(1, 1000) for _ in range(size)]
    start_time = time.time()
    merge_sort(arr.copy())
    merge_time = time.time() - start_time
    start_time = time.time()
    insertion_sort(arr.copy())
    insertion_time = time.time() - start_time
    print(f"Array Size: {size}")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print("\n")
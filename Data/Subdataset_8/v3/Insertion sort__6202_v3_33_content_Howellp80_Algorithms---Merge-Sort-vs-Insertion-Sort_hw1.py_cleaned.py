import time
import random
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_val = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_val:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_val
arr_sizes = [0, 2000, 8000, 32000, 128000, 512000, 1024000, 4096000]
for size in arr_sizes:
    arr = [random.randint(1, 1000) for _ in range(size)]
    merge_start_time = time.time()
    sorted_arr_merge = merge_sort(arr)
    merge_end_time = time.time()
    merge_time = merge_end_time - merge_start_time
    insertion_start_time = time.time()
    insertion_sort(arr)
    insertion_end_time = time.time()
    insertion_time = insertion_end_time - insertion_start_time
    print("Array Size:", size)
    print("Merge Sort Time:", merge_time)
    print("Insertion Sort Time:", insertion_time)
    print("\n")
import random
import timeit
def print_array(arr):
    print(' '.join(map(str, arr)))
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
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
def unh_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def measure_sorting_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr)
    return timeit.default_timer() - start_time
array_size = 10000
initial_array = random.sample(range(array_size), array_size)
insertion_randoms = initial_array.copy()
merge_randoms = initial_array.copy()
unh_randoms = initial_array.copy()
print("Initial Array:")
print_array(initial_array)
insertion_sort_time = measure_sorting_time(insertion_sort, insertion_randoms)
merge_sort_time = measure_sorting_time(merge_sort, merge_randoms)
unh_sort_time = measure_sorting_time(unh_sort, unh_randoms)
print(f"Insertion Sort Time: {insertion_sort_time:.6f} seconds")
print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")
print(f"UNH Sort Time: {unh_sort_time:.6f} seconds")
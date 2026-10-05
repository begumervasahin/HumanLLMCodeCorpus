import random
import timeit
def print_array(arr):
    print(' '.join(str(i) for i in arr))
def insertion_sort(arr):
    N = len(arr)
    for i in range(1, N):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
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
    M = len(arr)
    for i in range(M-1, 0, -1):
        for j in range(1, i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
insertion_randoms = merge_randoms = UNH_randoms = random.sample(range(10000), 10000)
print("Initial Array:")
print_array(insertion_randoms)
insertion_start = timeit.default_timer()
insertion_sort(insertion_randoms)
insertion_stop = timeit.default_timer()
merge_start = timeit.default_timer()
merge_sort(merge_randoms)
merge_stop = timeit.default_timer()
UNH_start = timeit.default_timer()
unh_sort(UNH_randoms)
UNH_stop = timeit.default_timer()
print("Insertion Sort Time:", insertion_stop - insertion_start)
print("Merge Sort Time:", merge_stop - merge_start)
print("UNH Sort Time:", UNH_stop - UNH_start)
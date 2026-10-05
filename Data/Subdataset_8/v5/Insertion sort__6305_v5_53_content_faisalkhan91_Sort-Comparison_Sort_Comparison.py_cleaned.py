import random
import timeit
def print_array(arr):
    print(' '.join(str(i) for i in arr))
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element
def merge_sort(arr):
    if len(arr) <= 1:
        return
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
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
random_array = random.sample(range(10000), 10000)
insertion_randoms = random_array[:]
merge_randoms = random_array[:]
bubble_randoms = random_array[:]
print("Initial Array:")
print_array(random_array)
insertion_start = timeit.default_timer()
insertion_sort(insertion_randoms)
insertion_stop = timeit.default_timer()
merge_start = timeit.default_timer()
merge_sort(merge_randoms)
merge_stop = timeit.default_timer()
bubble_start = timeit.default_timer()
bubble_sort(bubble_randoms)
bubble_stop = timeit.default_timer()
print("Insertion Sort Time:", insertion_stop - insertion_start)
print("Merge Sort Time:", merge_stop - merge_start)
print("Bubble Sort Time:", bubble_stop - bubble_start)
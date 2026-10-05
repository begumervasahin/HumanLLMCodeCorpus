import random
import timeit
def print_array(arr):
    print(' '.join(map(str, arr)))
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)
    left_half = arr[:mid]
    right_half = arr[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(left_half, right_half, arr)
def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
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
insertion_time = timeit.timeit(lambda: insertion_sort(insertion_randoms), number=1)
merge_time = timeit.timeit(lambda: merge_sort(merge_randoms), number=1)
bubble_time = timeit.timeit(lambda: bubble_sort(bubble_randoms), number=1)
print("Insertion Sort Time:", insertion_time)
print("Merge Sort Time:", merge_time)
print("Bubble Sort Time:", bubble_time)
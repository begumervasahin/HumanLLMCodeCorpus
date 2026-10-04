import random
import timeit
def print_array(arr):
    print(' '.join(str(i) for i in arr))
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
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
def unhsort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(1, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
array_size = 10000
random_array = random.sample(range(array_size), array_size)
insertion_randoms = random_array.copy()
merge_randoms = random_array.copy()
unh_randoms = random_array.copy()
print("Initial Array:")
print_array(random_array)
insertion_start = timeit.default_timer()
insertion_sort(insertion_randoms)
insertion_stop = timeit.default_timer()
print("Insertion Sort Time: {:.5f} seconds".format(insertion_stop - insertion_start))
merge_start = timeit.default_timer()
merge_sort(merge_randoms)
merge_stop = timeit.default_timer()
print("Merge Sort Time: {:.5f} seconds".format(merge_stop - merge_start))
unh_start = timeit.default_timer()
unhsort(unh_randoms)
unh_stop = timeit.default_timer()
print("UNH Sort Time: {:.5f} seconds".format(unh_stop - unh_start))
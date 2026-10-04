import random
import timeit
def print_array(arr):
    print(' '.join(map(str, arr)))
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
def unh_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(1, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def measure_sorting_time(sort_function, arr):
    start_time = timeit.default_timer()
    sort_function(arr)
    end_time = timeit.default_timer()
    return end_time - start_time
def main():
    array_size = 10000
    random_array = random.sample(range(array_size), array_size)
    insertion_randoms = random_array.copy()
    merge_randoms = random_array.copy()
    unh_randoms = random_array.copy()
    print("Initial Array:")
    print_array(random_array)
    insertion_sort_time = measure_sorting_time(insertion_sort, insertion_randoms)
    print("Insertion Sort Time: {:.5f} seconds".format(insertion_sort_time))
    merge_sort_time = measure_sorting_time(merge_sort, merge_randoms)
    print("Merge Sort Time: {:.5f} seconds".format(merge_sort_time))
    unh_sort_time = measure_sorting_time(unh_sort, unh_randoms)
    print("UNH Sort Time: {:.5f} seconds".format(unh_sort_time))
if __name__ == "__main__":
    main()
import random
def insertion_sort(arr):
    if not isinstance(arr, list):
        raise TypeError('Input must be a list.')
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def choose_pivot(arr, low, high, pivot_type):
    pivots = {'first': low, 'last': high, 'middle': (low + high)
    pivot = arr[pivots[pivot_type]]
    arr[pivots[pivot_type]], arr[high] = arr[high], arr[pivots[pivot_type]]
    return pivot, arr
def partition(arr, low, high, pivot_type):
    pivot, arr = choose_pivot(arr, low, high, pivot_type)
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort_recursive(arr, low, high, pivot_type, use_insertion_sort=False, insertion_sort_threshold=10):
    if not isinstance(arr, list):
        raise TypeError('Input must be a list.')
    if low < high:
        if use_insertion_sort and (high - low) < insertion_sort_threshold:
            insertion_sort(arr[low:high + 1])
        else:
            try:
                pivot_index = partition(arr, low, high, pivot_type)
                quick_sort_recursive(arr, low, pivot_index - 1, pivot_type, use_insertion_sort, insertion_sort_threshold)
                quick_sort_recursive(arr, pivot_index + 1, high, pivot_type, use_insertion_sort, insertion_sort_threshold)
            except KeyError:
                print('Pivot options: first, last, middle, random.')
if __name__ == "__main__":
    my_list = [3, 1, 7, 2, 9, 5, 4, 8, 6]
    print("Original list:", my_list)
    sorted_list = quick_sort_recursive(my_list, 0, len(my_list) - 1, 'first')
    print("Sorted list using Quicksort:", sorted_list)
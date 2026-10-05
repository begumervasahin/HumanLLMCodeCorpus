import random
def insertion_sort(arr):
    if not isinstance(arr, list):
        raise TypeError('The input must be a list.')
    n = len(arr)
    if n < 2:
        return arr
    for i in range(1, n):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element
    return arr
def choose_pivot(arr, low, high, pivot_type):
    pivot_indices = {'first': low, 'last': high, 'middle': (low + high)
    pivot = arr[pivot_indices[pivot_type]]
    arr[pivot_indices[pivot_type]], arr[high] = arr[high], arr[pivot_indices[pivot_type]]
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
def quick_sort_recursive(arr, low, high, pivot_type, modify=False, modify_length=10):
    if not isinstance(arr, list):
        raise TypeError('The input must be a list.')
    if len(arr) < 2:
        return arr
    try:
        if low < high:
            if modify and (high - low) < modify_length:
                arr = insertion_sort(arr[low:high + 1])
            else:
                pivot_index = partition(arr, low, high, pivot_type)
                if modify and (pivot_index - low) < modify_length:
                    insertion_sort(arr[low:pivot_index])
                else:
                    quick_sort_recursive(arr, low, pivot_index - 1, pivot_type)
                if modify and (high - pivot_index) < modify_length:
                    insertion_sort(arr[pivot_index + 1: high + 1])
                else:
                    quick_sort_recursive(arr, pivot_index + 1, high, pivot_type)
        return arr
    except TypeError:
        print('The list must contain only numbers.')
        return None
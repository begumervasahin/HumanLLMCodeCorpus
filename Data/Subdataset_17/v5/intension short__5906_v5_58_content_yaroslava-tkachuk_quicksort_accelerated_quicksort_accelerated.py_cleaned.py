import random
def insertion_sort(arr):
    if not isinstance(arr, list):
        raise TypeError('Input must be a list containing numbers.')
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def choose_pivot(arr, low, high, pivot_type):
    pivot_indices = {
        'first': low,
        'last': high,
        'middle': (low + high)
        'random': random.randint(low, high)
    }
    pivot_index = pivot_indices.get(pivot_type, low)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return arr[high], arr
def partition(arr, low, high, pivot_type):
    pivot, arr = choose_pivot(arr, low, high, pivot_type)
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quicksort(arr, low=0, high=None, pivot_type='last', use_insertion_sort=False, threshold=10):
    if not isinstance(arr, list):
        raise TypeError('Input must be a list containing numbers.')
    if high is None:
        high = len(arr) - 1
    if low < high:
        if use_insertion_sort and (high - low) < threshold:
            arr[low:high + 1] = insertion_sort(arr[low:high + 1])
        else:
            pivot_index = partition(arr, low, high, pivot_type)
            quicksort(arr, low, pivot_index - 1, pivot_type, use_insertion_sort, threshold)
            quicksort(arr, pivot_index + 1, high, pivot_type, use_insertion_sort, threshold)
    return arr
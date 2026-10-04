import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
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
    pivot_index = pivot_indices.get(pivot_type, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return arr[high]
def partition(arr, low, high, pivot_type):
    pivot = choose_pivot(arr, low, high, pivot_type)
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quicksort(arr, low=0, high=None, pivot_type='last', use_insertion_sort=False, threshold=10):
    if high is None:
        high = len(arr) - 1
    if low < high:
        if use_insertion_sort and (high - low + 1) <= threshold:
            insertion_sort(arr[low:high + 1])
        else:
            pi = partition(arr, low, high, pivot_type)
            quicksort(arr, low, pi - 1, pivot_type, use_insertion_sort, threshold)
            quicksort(arr, pi + 1, high, pivot_type, use_insertion_sort, threshold)
    return arr
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Unsorted:", data)
    sorted_data = quicksort(data, pivot_type='middle', use_insertion_sort=True, threshold=10)
    print("Sorted:", sorted_data)
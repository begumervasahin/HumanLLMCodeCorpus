import random
import time
def calculate_percentage_difference(num1, num2):
    if num1 > num2:
        return (num2 / num1) * 100
    else:
        return (num1 / num2) * 100
def print_array(arr, name):
    print(f'Sorted array from {name} Sort:')
    for element in arr:
        print(element, end=' ')
    print("")
def measure_sorting_time(sort_function, array):
    start_time = time.time()
    sort_function(array)
    elapsed_time = time.time() - start_time
    print(f'Function [{sort_function.__name__}] finished in {elapsed_time:.3f} seconds')
    return elapsed_time
def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
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
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arrays = {
    'Bubble': [random.randint(1, 500) for _ in range(10000)],
    'Insertion': [random.randint(1, 500) for _ in range(10000)],
    'Selection': [random.randint(1, 500) for _ in range(10000)],
    'Quick': [random.randint(1, 5000) for _ in range(10000)],
    'Merge': [random.randint(1, 5000) for _ in range(10000)],
    'Heap': [random.randint(1, 5000) for _ in range(10000)]
}
sorting_times = {}
for name, array in arrays.items():
    sorting_function = globals()[f'{name.lower()}_sort']
    sorting_times[name] = measure_sorting_time(sorting_function, array)
for name, array in arrays.items():
    print_array(array, name)
for name, time_taken in sorting_times.items():
    print(f"{name} Sort Time: {time_taken} seconds")
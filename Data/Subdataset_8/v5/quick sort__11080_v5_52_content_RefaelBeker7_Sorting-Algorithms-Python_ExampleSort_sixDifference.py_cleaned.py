import random
import time
def calculate_percentage_difference(num1, num2):
    if num1 > num2:
        return ((num2 / num1) * 100)
    else:
        return ((num1 / num2) * 100)
def print_sorted_array(arr, algorithm_name):
    print(f'Sorted array from {algorithm_name} Sort:')
    for num in arr:
        print(num, end=' ')
    print("")
def measure_sorting_time(sorting_function, array):
    start_time = time.time()
    sorting_function(array)
    elapsed_time = time.time() - start_time
    print(f'{sorting_function.__name__} finished in {elapsed_time:.3f} sec')
    return elapsed_time
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    count = 0
    if l < n and arr[i] < arr[l]:
        largest = l
        count += 1
    if r < n and arr[largest] < arr[r]:
        largest = r
        count += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        count += 1
        count += heapify(arr, n, largest)
    return count
def heap_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n, -1, -1):
        count += 1
        count += heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        count += 1
        count += heapify(arr, i, 0)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)
def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
def selection_sort(arr):
    count = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
            count += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
        count += 1
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
array_bubble_sort = [random.randint(1, 500) for _ in range(10000)]
array_insertion_sort = [random.randint(1, 500) for _ in range(10000)]
array_selection_sort = [random.randint(1, 500) for _ in range(10000)]
array_quick_sort = [random.randint(1, 5000) for _ in range(10000)]
array_merge_sort = [random.randint(1, 5000) for _ in range(10000)]
array_heap_sort = [random.randint(1, 5000) for _ in range(10000)]
bubble_time = measure_sorting_time(bubble_sort, array_bubble_sort)
insertion_time = measure_sorting_time(insertion_sort, array_insertion_sort)
selection_time = measure_sorting_time(selection_sort, array_selection_sort)
quick_time = measure_sorting_time(quick_sort, array_quick_sort)
merge_time = measure_sorting_time(merge_sort, array_merge_sort)
heap_time = measure_sorting_time(heap_sort, array_heap_sort)
print_sorted_array(array_bubble_sort, 'Bubble')
print_sorted_array(array_insertion_sort, 'Insertion')
print_sorted_array(array_selection_sort, 'Selection')
print_sorted_array(array_quick_sort, 'Quick')
print_sorted_array(array_merge_sort, 'Merge')
print_sorted_array(array_heap_sort, 'Heap')
print("Time difference between sorting algorithms:")
print(f"Bubble Sort vs Insertion Sort: {calculate_percentage_difference(bubble_time, insertion_time):.2f}%")
print(f"Bubble Sort vs Selection Sort: {calculate_percentage_difference(bubble_time, selection_time):.2f}%")
print(f"Bubble Sort vs Quick Sort: {calculate_percentage_difference(bubble_time, quick_time):.2f}%")
print(f"Bubble Sort vs Merge Sort: {calculate_percentage_difference(bubble_time, merge_time):.2f}%")
print(f"Bubble Sort vs Heap Sort: {calculate_percentage_difference(bubble_time, heap_time):.2f}%")
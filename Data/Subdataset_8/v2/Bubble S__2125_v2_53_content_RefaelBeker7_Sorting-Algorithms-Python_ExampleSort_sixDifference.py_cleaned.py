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
def check_time(function_name, start_time):
    elapsed_time = time.time() - start_time
    print(f'Function [{function_name.__name__}] finished in {elapsed_time:.3f} seconds')
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
        count += 1
        arr[i], arr[0] = arr[0], arr[i]
        count += heapify(arr, i, 0)
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
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
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
        count += 1
        min_index = i
        for j in range(i + 1, len(arr)):
            count += 1
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        count += 1
def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        count += 1
array_bubble_sort = [random.randint(1, 500) for _ in range(10000)]
array_insertion_sort = [random.randint(1, 500) for _ in range(10000)]
array_selection_sort = [random.randint(1, 500) for _ in range(10000)]
array_quick_sort = [random.randint(1, 5000) for _ in range(10000)]
array_merge_sort = [random.randint(1, 5000) for _ in range(10000)]
array_heap_sort = [random.randint(1, 5000) for _ in range(10000)]
start_time = time.time()
bubble_sort(array_bubble_sort)
bubble_time = check_time(bubble_sort, start_time)
start_time = time.time()
insertion_sort(array_insertion_sort)
insertion_time = check_time(insertion_sort, start_time)
start_time = time.time()
selection_sort(array_selection_sort)
selection_time = check_time(selection_sort, start_time)
start_time = time.time()
quick_sort(array_quick_sort)
quick_time = check_time(quick_sort, start_time)
start_time = time.time()
merge_sort(array_merge_sort)
merge_time = check_time(merge_sort, start_time)
start_time = time.time()
heap_sort(array_heap_sort)
heap_time = check_time(heap_sort, start_time)
print(" ")
print_array(array_bubble_sort, 'Bubble')
print_array(array_insertion_sort, 'Insertion')
print_array(array_selection_sort, 'Selection')
print_array(array_quick_sort, 'Quick')
print_array(array_merge_sort, 'Merge')
print_array(array_heap_sort, 'Heap')
print(f"\nBubble Sort Time: {bubble_time} seconds")
print(f"Insertion Sort Time: {insertion_time} seconds")
print(f"Selection Sort Time: {selection_time} seconds")
print(f"Quick Sort Time: {quick_time} seconds")
print(f"Merge Sort Time: {merge_time} seconds")
print(f"Heap Sort Time: {heap_time} seconds")
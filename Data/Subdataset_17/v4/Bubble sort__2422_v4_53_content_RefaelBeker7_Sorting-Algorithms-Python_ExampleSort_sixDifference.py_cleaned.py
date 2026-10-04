import random
import time
def check_different_time(num1, num2):
    if num1 > num2:
        return (num2 / num1) * 100
    else:
        return (num1 / num2) * 100
def print_array(arr, name):
    print(f'Sorted array from {name} Sort:')
    for num in arr:
        print(num, end=' ')
    print("")
def check_time(name_func, start_time):
    elapsed_time = time.time() - start_time
    print(f'Function [{name_func.__name__}] finished in {elapsed_time:.3f} sec')
    return elapsed_time
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
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
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)
def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
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
def main():
    array_sizes = [10000] * 6
    array_values = [(1, 500), (1, 500), (1, 500), (1, 5000), (1, 5000), (1, 5000)]
    sorting_algorithms = [
        ('Bubble', bubble_sort),
        ('Insertion', insertion_sort),
        ('Selection', selection_sort),
        ('Quick', quick_sort),
        ('Merge', merge_sort),
        ('Heap', heap_sort)
    ]
    arrays = []
    for size, values in zip(array_sizes, array_values):
        array = [random.randint(*values) for _ in size]
        arrays.append(array)
    for (name, sort_func), arr in zip(sorting_algorithms, arrays):
        print(f"----- Array for {name} Sort: ----")
        print_array(arr, name)
        start_time = time.time()
        sort_func(arr)
        elapsed_time = check_time(sort_func, start_time)
        print_array(arr, name)
if __name__ == "__main__":
    main()
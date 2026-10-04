import time
import random
import sys
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def merge(arr, left, mid, right):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
def merge_sort_utility(arr, left, right):
    if left < right:
        mid = left + (right - left)
        merge_sort_utility(arr, left, mid)
        merge_sort_utility(arr, mid + 1, right)
        merge(arr, left, mid, right)
def merge_sort(arr):
    merge_sort_utility(arr, 0, len(arr) - 1)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort_utility(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_utility(arr, low, pi - 1)
        quick_sort_utility(arr, pi + 1, high)
def quick_sort(arr):
    quick_sort_utility(arr, 0, len(arr) - 1)
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n
        heapify(arr, n, i)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    num_elements = 4000
    l = [random.randrange(0, 1000000000) for _ in range(num_elements)]
    l.sort()
    time_taken = 0
    iterations = 100000
    for _ in range(iterations):
        al = l.copy()
        start_time = time.time()
        quick_sort(al)
        time_taken += time.time() - start_time
    avg_time = time_taken / iterations
    print(f"Time taken is {avg_time:.6f} seconds")
    print(al)
    sys.setrecursionlimit(1000)
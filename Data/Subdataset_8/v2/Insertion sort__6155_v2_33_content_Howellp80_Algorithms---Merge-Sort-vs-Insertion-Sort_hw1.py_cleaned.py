import time
import random
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
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
def insertionSort(arr):
    for i in range(1, len(arr)):
        curVal = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > curVal:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = curVal
arrSizes = [0, 2000, 8000, 32000, 128000, 512000, 1024000, 4096000]
for size in arrSizes:
    arr = [random.randint(1, 1000) for _ in range(size)]
    merge_start_time = time.time()
    mergeSort(arr.copy())
    merge_end_time = time.time()
    merge_time = merge_end_time - merge_start_time
    insertion_start_time = time.time()
    insertionSort(arr.copy())
    insertion_end_time = time.time()
    insertion_time = insertion_end_time - insertion_start_time
    print("Array Size:", size)
    print("Merge Sort Time:", merge_time)
    print("Insertion Sort Time:", insertion_time)
    print("\n")
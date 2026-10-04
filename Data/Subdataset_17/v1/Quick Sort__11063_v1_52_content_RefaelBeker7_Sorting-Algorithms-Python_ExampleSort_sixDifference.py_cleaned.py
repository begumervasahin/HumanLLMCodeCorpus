import random
import time
def checkDifferentTime(num1, num2):
    if num1 > num2:
        return (num2 / num1) * 100
    else:
        return (num1 / num2) * 100
def printArray(arr, name):
    if name == 'Bubble':
        print('Sort array from Bubble Sort Sorted array is:')
    elif name == 'Insertion':
        print('Sort array from Insertion Sort Sorted array is:')
    elif name == 'Selection':
        print('Sort array from Selection Sort Sorted array is:')
    elif name == 'Quick':
        print('Sort array from Quick Sort Sorted array is:')
    elif name == 'Merge':
        print('Sort array from Merge Sort Sorted array is:')
    elif name == 'Heap':
        print('Sort array from Heap Sort Sorted array is:')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print("")
def CheckTime(nameFunc, startTime):
    elapsedTime = time.time() - startTime
    print('function [{}] finished in {:.3f} sec'.format(
        nameFunc.__name__, float(elapsedTime)))
    return elapsedTime
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
        heapify(arr, n, largest)
    return count
def heapSort(arr):
    n = len(arr)
    count = 0
    for i in range(n, -1, -1):
        count += 1
        count += heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        count += 1
        arr[i], arr[0] = arr[0], arr[i]
        count += heapify(arr, i, 0)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
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
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def quickSortHelper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSortHelper(arr, low, pi - 1)
        quickSortHelper(arr, pi + 1, high)
def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)
def selectionSort(arr):
    count = 0
    for i in range(len(arr)):
        count += 1
        min_index = i
        for j in range(i + 1, len(arr)):
            count += 1
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
def insertionSort(arr):
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
def bubbleSort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        count += 1
arrayBubbleSort = [random.randint(1, 500) for _ in range(10000)]
arrayInsertionSort = [random.randint(1, 500) for _ in range(10000)]
arraySelectionSort = [random.randint(1, 500) for _ in range(10000)]
arrayQuickSort = [random.randint(1, 5000) for _ in range(10000)]
arrayMergeSort = [random.randint(1, 5000) for _ in range(10000)]
arrayHeapSort = [random.randint(1, 5000) for _ in range(10000)]
print(" ")
startTime = time.time()
bubbleSort(arrayBubbleSort)
bubbleTime = CheckTime(bubbleSort, startTime)
print(" ")
startTime = time.time()
insertionSort(arrayInsertionSort)
insertionTime = CheckTime(insertionSort, startTime)
print(" ")
startTime = time.time()
selectionSort(arraySelectionSort)
selectionTime = CheckTime(selectionSort, startTime)
print(" ")
startTime = time.time()
quickSort(arrayQuickSort)
quickTime = CheckTime(quickSort, startTime)
print(" ")
startTime = time.time()
mergeSort(arrayMergeSort)
mergeTime = CheckTime(mergeSort, startTime)
print(" ")
startTime = time.time()
heapSort(arrayHeapSort)
heapTime = CheckTime(heapSort, startTime)
print(" ")
printArray(arrayBubbleSort, 'Bubble')
printArray(arrayInsertionSort, 'Insertion')
printArray(arraySelectionSort, 'Selection')
printArray(arrayQuickSort, 'Quick')
printArray(arrayMergeSort, 'Merge')
printArray(arrayHeapSort, 'Heap')
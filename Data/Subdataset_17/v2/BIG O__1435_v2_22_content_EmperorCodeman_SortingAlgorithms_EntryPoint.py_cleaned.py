import sys
from random import shuffle, randrange, seed
from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
def test(iterations=1000, debug=False):
    if debug:
        seed(10)
    case = [randrange(0, 7) for _ in range(7)]
    testCase = sorted(case[:])
    failures = []
    sys.setrecursionlimit(12000)
    metrics = {"comparisons": 0, "swaps": 0}
    tabulations = {
        "bubbleSort": metrics.copy(),
        "shakerSort": metrics.copy(),
        "selectionSort": metrics.copy(),
        "quickSort": metrics.copy(),
        "modifiedQuickSort": metrics.copy(),
        "mergeSort": metrics.copy(),
        "hashSort": metrics.copy()
    }
    for _ in range(iterations):
        shuffle(case)
        Bubble_Sort(case[:], tabulations)
        failures.append(case == testCase)
        shuffle(case)
        Shaker_Sort(case[:], tabulations)
        failures.append(case == testCase)
        shuffle(case)
        SelectionSort(case[:], tabulations)
        failures.append(case == testCase)
        shuffle(case)
        QuickSort(case[:], tabulations)
        failures.append(case == testCase)
        shuffle(case)
        ModifiedQuickSort(case[:], tabulations)
        failures.append(case == testCase)
        shuffle(case)
        MergeSort(case[:], tabulations)
        failures.append(case == testCase)
        shuffle(case)
        HashSort(case[:], tabulations)
        failures.append(case == testCase)
    if False in failures:
        print("Some tests failed.")
    else:
        print("All tests passed successfully.")
if __name__ == "__main__":
    test()
def Bubble_Sort(array, metrics):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            metrics['bubbleSort']['comparisons'] += 1
            if array[j] > array[j+1]:
                metrics['bubbleSort']['swaps'] += 1
                array[j], array[j+1] = array[j+1], array[j]
def Shaker_Sort(array, metrics):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            metrics['shakerSort']['comparisons'] += 1
            if array[i] > array[i + 1]:
                metrics['shakerSort']['swaps'] += 1
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            metrics['shakerSort']['comparisons'] += 1
            if array[i] > array[i + 1]:
                metrics['shakerSort']['swaps'] += 1
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start = start + 1
def SelectionSort(array, metrics):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            metrics['selectionSort']['comparisons'] += 1
            if array[j] < array[min_idx]:
                min_idx = j
        metrics['selectionSort']['swaps'] += 1
        array[i], array[min_idx] = array[min_idx], array[i]
def QuickSort(array, metrics, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pi = partition(array, low, high, metrics)
        QuickSort(array, metrics, low, pi - 1)
        QuickSort(array, metrics, pi + 1, high)
def partition(array, low, high, metrics):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        metrics['quickSort']['comparisons'] += 1
        if array[j] < pivot:
            i += 1
            metrics['quickSort']['swaps'] += 1
            array[i], array[j] = array[j], array[i]
    metrics['quickSort']['swaps'] += 1
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1
def MergeSort(array, metrics):
    if len(array) > 1:
        mid = len(array)
        L = array[:mid]
        R = array[mid:]
        MergeSort(L, metrics)
        MergeSort(R, metrics)
        i = j = k = 0
        while i < len(L) and j < len(R):
            metrics['mergeSort']['comparisons'] += 1
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
def HashSort(array, metrics):
    array.sort()
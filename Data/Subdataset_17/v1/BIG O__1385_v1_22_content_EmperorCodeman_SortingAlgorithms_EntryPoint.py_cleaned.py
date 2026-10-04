from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
import sys
def test(iterations=1000, debug=False):
    if debug:
        seed(10)
    case = [randrange(0, 7) for _ in range(7)]
    testCase = sorted(case[:])
    failure = []
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
        Bubble_Sort(case, tabulations)
        failure.append(case == testCase)
        shuffle(case)
        Shaker_Sort(case, tabulations)
        failure.append(case == testCase)
        shuffle(case)
        SelectionSort(case, tabulations)
        failure.append(case == testCase)
        shuffle(case)
        QuickSort(case, tabulations)
        failure.append(case == testCase)
        shuffle(case)
        ModifiedQuickSort(case, tabulations)
        failure.append(case == testCase)
        shuffle(case)
        MergeSort(case, tabulations)
        failure.append(case == testCase)
        shuffle(case)
        HashSort(case, tabulations)
        failure.append(case == testCase)
    if False in failure:
        print(False)
    else:
        print(True)
test()
def Bubble_Sort(array, metrics):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            metrics['bubbleSort']['comparisons'] += 1
            if array[j] > array[j+1]:
                metrics['bubbleSort']['swaps'] += 1
                array[j], array[j+1] = array[j+1], array[j]

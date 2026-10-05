from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
def test(iterations=1000, debug=False):
    if debug:
        seed(10)
    case = [randrange(0, 7) for _ in range(7)]
    testCase = sorted(case[:])
    failure = []
    import sys
    sys.setrecursionlimit(12000)
    for _ in range(iterations):
        case_copy = case[:]
        Bubble_Sort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        shuffle(case_copy)
        Shaker_Sort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        shuffle(case_copy)
        SelectionSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        shuffle(case_copy)
        QuickSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        shuffle(case_copy)
        ModifiedQuickSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        shuffle(case_copy)
        MergeSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        shuffle(case_copy)
        HashSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
    if False in failure:
        print(False)
    else:
        print(True)
metrics = {"comparisons": 0, "swaps": 0}
tabulations = {
    "bubbleSort": metrics,
    "shakerSort": metrics,
    "selectionSort": metrics,
    "quickSort": metrics,
    "modifiedQuickSort": metrics,
    "mergeSort": metrics,
    "hashSort": metrics
}
test()
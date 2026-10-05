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
    case = [randrange(0, 7) for x in range(7)]
    testCase = case[:]
    testCase.sort()
    failure = []
    import sys
    sys.setrecursionlimit(12000)
    for test in range(iterations):
        case_copy = case[:]
        Bubble_Sort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        Shaker_Sort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        SelectionSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        QuickSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        ModifiedQuickSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        MergeSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        case_copy = case[:]
        HashSort(case_copy, tabulations)
        failure.append(case_copy == testCase)
        shuffle(case)
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
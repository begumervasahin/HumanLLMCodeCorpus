from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
def perform_sorting_tests(iterations=1000, debug=False):
    if debug:
        seed(10)
    test_case = [randrange(0, 7) for _ in range(7)]
    sorted_test_case = sorted(test_case)
    failures = []
    import sys
    sys.setrecursionlimit(12000)
    for _ in range(iterations):
        for sorting_algorithm in sorting_algorithms:
            case_copy = test_case[:]
            sorting_algorithm(case_copy, tabulations)
            failures.append(case_copy == sorted_test_case)
            shuffle(test_case)
    print(all(failures))
sorting_algorithms = [
    Bubble_Sort,
    Shaker_Sort,
    SelectionSort,
    QuickSort,
    ModifiedQuickSort,
    MergeSort,
    HashSort
]
metrics = {"comparisons": 0, "swaps": 0}
tabulations = {algorithm.__name__: metrics.copy() for algorithm in sorting_algorithms}
perform_sorting_tests()
from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
import sys
def generate_random_case(length):
    return [randrange(0, 7) for _ in range(length)]
def run_tests(iterations, test_case, tabulations):
    failure = []
    for _ in range(iterations):
        for sort_func in sorting_functions:
            case_copy = test_case[:]
            shuffle(case_copy)
            sort_func(case_copy, tabulations)
            failure.append(case_copy == test_case)
    return all(failure)
def initialize_tabulations(metrics):
    return {
        "bubbleSort": metrics.copy(),
        "shakerSort": metrics.copy(),
        "selectionSort": metrics.copy(),
        "quickSort": metrics.copy(),
        "modifiedQuickSort": metrics.copy(),
        "mergeSort": metrics.copy(),
        "hashSort": metrics.copy()
    }
def main():
    seed(10)
    test_case = sorted(generate_random_case(7))
    sys.setrecursionlimit(12000)
    metrics = {"comparisons": 0, "swaps": 0}
    tabulations = initialize_tabulations(metrics)
    success = run_tests(1000, test_case, tabulations)
    print(success)
if __name__ == "__main__":
    main()
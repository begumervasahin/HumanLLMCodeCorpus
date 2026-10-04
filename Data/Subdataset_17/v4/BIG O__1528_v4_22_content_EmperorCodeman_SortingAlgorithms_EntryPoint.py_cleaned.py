from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
import sys
def test_sorting_algorithms(iterations=1000, debug=False):
    if debug:
        seed(10)
    case = [randrange(0, 7) for _ in range(7)]
    test_case = sorted(case[:])
    failures = []
    sys.setrecursionlimit(12000)
    for _ in range(iterations):
        for sort_func, name in [
            (Bubble_Sort, "bubbleSort"),
            (Shaker_Sort, "shakerSort"),
            (SelectionSort, "selectionSort"),
            (HashSort, "hashSort"),
            (MergeSort, "mergeSort")
        ]:
            run_sort_test(sort_func, case, test_case, tabulations[name], failures)
    print_results(failures)
def run_sort_test(sort_func, case, test_case, metrics, failures):
    case_copy = case[:]
    sort_func(case_copy, metrics)
    failures.append(case_copy == test_case)
    shuffle(case)
def print_results(failures):
    if False in failures:
        print(False)
    else:
        print(True)
if __name__ == "__main__":
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
    test_sorting_algorithms()
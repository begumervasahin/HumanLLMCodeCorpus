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
    expected_sorted_case = sorted(case[:])
    failures = []
    sys.setrecursionlimit(12000)
    sorting_algorithms = [
        (Bubble_Sort, "Bubble Sort"),
        (Shaker_Sort, "Shaker Sort"),
        (SelectionSort, "Selection Sort"),
        (HashSort, "Hash Sort"),
        (MergeSort, "Merge Sort")
    ]
    tabulations = {name: {"comparisons": 0, "swaps": 0} for _, name in sorting_algorithms}
    for _ in range(iterations):
        for sort_func, name in sorting_algorithms:
            run_sort_test(sort_func, case, expected_sorted_case, tabulations[name], failures)
    print_results(failures)
def run_sort_test(sort_func, case, expected_sorted_case, metrics, failures):
    case_copy = case[:]
    sort_func(case_copy, metrics)
    is_sorted_correctly = case_copy == expected_sorted_case
    failures.append(is_sorted_correctly)
    shuffle(case)
def print_results(failures):
    if any(not result for result in failures):
        print("Some sorting algorithms failed.")
    else:
        print("All sorting algorithms passed.")
if __name__ == "__main__":
    test_sorting_algorithms()
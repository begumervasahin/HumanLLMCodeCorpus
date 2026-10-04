import timeit
def print_time(test_name, elements, quicksort_variant, quicksort_function):
    """
    Print the minimum time taken for sorting using the specified quicksort function.
    Parameters:
        test_name (str): The name of the test (e.g., "Quick Sort").
        elements (int): The number of elements in the list to be sorted.
        quicksort_variant (str): The name of the quicksort variant (e.g., "quickSort", "randomQuickSort").
        quicksort_function (str): The name of the function to be imported and used for sorting.
    """
    print(f"{test_name}\n{elements} elements")
    setup_code = f'''
import random
random.seed('12345')
s = [random.random() for i in range({elements})]
from {quicksort_variant} import {quicksort_function}
'''
    timer_code = f'a=s[:]; {quicksort_function}(0, {elements}, a)'
    min_time = min(timeit.Timer(timer_code, setup=setup_code).repeat(10, 100))
    print(min_time)
def main():
    print_time("Quick Sort", 1000, "quickSort", "quickSort")
    print_time("Quick Sort", 10000, "quickSort", "quickSort")
    print_time("Quick Sort", 100000, "quickSort", "quickSort")
    print_time("Random Quick Sort", 1000, "randomQuickSort", "randomQuickSort")
    print_time("Random Quick Sort", 10000, "randomQuickSort", "randomQuickSort")
    print_time("Random Quick Sort", 100000, "randomQuickSort", "randomQuickSort")
    print_time("Median Random Quick Sort", 1000, "medianRandomQuickSort", "medianRandomQuickSort")
    print_time("Median Random Quick Sort", 10000, "medianRandomQuickSort", "medianRandomQuickSort")
    print_time("Median Random Quick Sort", 100000, "medianRandomQuickSort", "medianRandomQuickSort")
if __name__ == "__main__":
    main()
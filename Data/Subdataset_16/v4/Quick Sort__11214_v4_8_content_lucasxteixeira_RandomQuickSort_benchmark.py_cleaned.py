import timeit
def fonk1(test_name, elements, quicksort_variant, quicksort_function):
    """
    Print the minimum time taken for sorting using the specified quicksort function.
    Parameters:
        test_name (str): The name of the test (e.g., "Quick Sort").
        elements (int): The number of elements in the list to be sorted.
        quicksort_variant (str): The name of the quicksort variant (e.g., "quickSort", "randomQuickSort").
        quicksort_function (str): The name of the function to be imported and used for sorting.
    """
    print(f"{test_name}\n{elements} elements")
    b1 = f'''
import random
random.seed('12345')
b2 = [random.random() for i in range({elements})]
from {quicksort_variant} import {quicksort_function}
'''
    b3 = f'a=b2[:]; {quicksort_function}(0, {elements}, a)'
    b4 = min(timeit.Timer(b3, setup=b1).repeat(10, 100))
    print(b4)
def fonk2():
    fonk1("Quick Sort", 1000, "quickSort", "quickSort")
    fonk1("Quick Sort", 10000, "quickSort", "quickSort")
    fonk1("Quick Sort", 100000, "quickSort", "quickSort")
    fonk1("Random Quick Sort", 1000, "randomQuickSort", "randomQuickSort")
    fonk1("Random Quick Sort", 10000, "randomQuickSort", "randomQuickSort")
    fonk1("Random Quick Sort", 100000, "randomQuickSort", "randomQuickSort")
    fonk1("Median Random Quick Sort", 1000, "medianRandomQuickSort", "medianRandomQuickSort")
    fonk1("Median Random Quick Sort", 10000, "medianRandomQuickSort", "medianRandomQuickSort")
    fonk1("Median Random Quick Sort", 100000, "medianRandomQuickSort", "medianRandomQuickSort")
if b5 = = "__main__":
    fonk2()
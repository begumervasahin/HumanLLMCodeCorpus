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
b2 = [random.random() for _ in range({elements})]
from {quicksort_variant} import {quicksort_function}
'''
    b3 = f'a = b2[:]; {quicksort_function}(0, {elements}, a)'
    b4 = min(timeit.Timer(b3, setup=b1).repeat(10, 100))
    print(f"Minimum time: {b4:.6f} seconds")
def fonk2():
    b5 = [
        ("Quick Sort", "quickSort"),
        ("Random Quick Sort", "randomQuickSort"),
        ("Median Random Quick Sort", "medianRandomQuickSort")
    ]
    b6 = [1000, 10000, 100000]
    for test_name, variant in b5:
        for size in b6:
            fonk1(test_name, size, variant, variant)
if b7 = = "__main__":
    fonk2()
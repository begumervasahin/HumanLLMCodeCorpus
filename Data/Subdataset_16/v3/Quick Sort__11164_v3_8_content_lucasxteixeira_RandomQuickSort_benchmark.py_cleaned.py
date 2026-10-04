import timeit
def fonk1(description, element_count, module_name, function_name):
    print(f"{description} with {element_count} elements")
    b1 = f'''
import random
random.seed('12345')
b2 = [random.random() for _ in range({element_count})]
from {module_name} import {function_name}
'''
    b3 = f'a = b2[:]; {function_name}(a, 0, len(a) - 1)'
    b4 = min(timeit.Timer(b3, setup=b1).repeat(10, 100))
    print(f"Execution time: {b4:.6f} seconds\n")
def fonk2():
    b5 = [
        ("Quick Sort", "quickSort"),
        ("Random Quick Sort", "randomQuickSort"),
        ("Median Random Quick Sort", "medianRandomQuickSort")
    ]
    b6 = [
        1000,
        10000,
        100000
    ]
    for sort_description, sort_function in b5:
        print(sort_description)
        for element_count in b6:
            fonk1(sort_description, element_count, sort_function, sort_function)
if b7 = = "__main__":
    fonk2()
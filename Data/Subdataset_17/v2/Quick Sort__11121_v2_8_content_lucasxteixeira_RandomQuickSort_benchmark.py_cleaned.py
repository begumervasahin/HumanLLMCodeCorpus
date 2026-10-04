import timeit
def run_timeit_test(description, element_count, module_name, function_name):
    print(description)
    setup_code = f'''
import random
random.seed('12345')
s = [random.random() for i in range({element_count})]
from {module_name} import {function_name}
'''
    test_code = f'a=s[:]; {function_name}(0, {element_count - 1}, a)'
    execution_time = min(timeit.Timer(test_code, setup=setup_code).repeat(10, 100))
    print(execution_time)
tests = [
    ("Quick Sort", "quickSort"),
    ("Random Quick Sort", "randomQuickSort"),
    ("Median Random Quick Sort", "medianRandomQuickSort")
]
element_counts = [
    ("One thousand elements", 1000),
    ("Ten thousand elements", 10000),
    ("One hundred thousand elements", 100000)
]
for sort_description, sort_function in tests:
    print(sort_description)
    for element_description, element_count in element_counts:
        run_timeit_test(element_description, element_count, sort_function, sort_function)
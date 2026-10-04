import timeit
def run_timeit_test(description, element_count, module_name, function_name):
    print(f"{description} with {element_count} elements")
    setup_code = f'''
import random
random.seed('12345')
s = [random.random() for _ in range({element_count})]
from {module_name} import {function_name}
'''
    test_code = f'a = s[:]; {function_name}(a, 0, len(a) - 1)'
    execution_time = min(timeit.Timer(test_code, setup=setup_code).repeat(10, 100))
    print(f"Execution time: {execution_time:.6f} seconds\n")
def main():
    tests = [
        ("Quick Sort", "quickSort"),
        ("Random Quick Sort", "randomQuickSort"),
        ("Median Random Quick Sort", "medianRandomQuickSort")
    ]
    element_counts = [
        1000,
        10000,
        100000
    ]
    for sort_description, sort_function in tests:
        print(sort_description)
        for element_count in element_counts:
            run_timeit_test(sort_description, element_count, sort_function, sort_function)
if __name__ == "__main__":
    main()
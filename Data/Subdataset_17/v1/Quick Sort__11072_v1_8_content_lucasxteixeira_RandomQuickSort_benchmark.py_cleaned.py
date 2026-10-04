import timeit
def run_timeit_test(description, element_count, module_name, function_name):
    print(description)
    setup = f'''
import random
random.seed('12345')
s = [random.random() for i in range({element_count})]
from {module_name} import {function_name}
'''
    stmt = f'a=s[:]; {function_name}(0, {element_count - 1}, a)'
    print(min(timeit.Timer(stmt, setup=setup).repeat(10, 100)))
print("Quick Sort")
run_timeit_test("One thousand elements", 1000, 'quickSort', 'quickSort')
run_timeit_test("Ten thousand elements", 10000, 'quickSort', 'quickSort')
run_timeit_test("One hundred thousand elements", 100000, 'quickSort', 'quickSort')
print("Random Quick Sort")
run_timeit_test("One thousand elements", 1000, 'randomQuickSort', 'randomQuickSort')
run_timeit_test("Ten thousand elements", 10000, 'randomQuickSort', 'randomQuickSort')
run_timeit_test("One hundred thousand elements", 100000, 'randomQuickSort', 'randomQuickSort')
print("Median Random Quick Sort")
run_timeit_test("One thousand elements", 1000, 'medianRandomQuickSort', 'medianRandomQuickSort')
run_timeit_test("Ten thousand elements", 10000, 'medianRandomQuickSort', 'medianRandomQuickSort')
run_timeit_test("One hundred thousand elements", 100000, 'medianRandomQuickSort', 'medianRandomQuickSort')
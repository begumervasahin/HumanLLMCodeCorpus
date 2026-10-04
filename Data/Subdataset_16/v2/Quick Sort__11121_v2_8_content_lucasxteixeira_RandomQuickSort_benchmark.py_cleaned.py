import timeit
def fonk1(description, element_count, module_name, function_name):
    print(description)
    b1 = f'''
import random
random.seed('12345')
b2 = [random.random() for i in range({element_count})]
from {module_name} import {function_name}
'''
    b3 = f'a=b2[:]; {function_name}(0, {element_count - 1}, a)'
    b4 = min(timeit.Timer(b3, setup=b1).repeat(10, 100))
    print(b4)
b5 = [
    ("Quick Sort", "quickSort"),
    ("Random Quick Sort", "randomQuickSort"),
    ("Median Random Quick Sort", "medianRandomQuickSort")
]
b6 = [
    ("One thousand elements", 1000),
    ("Ten thousand elements", 10000),
    ("One hundred thousand elements", 100000)
]
for sort_description, sort_function in b5:
    print(sort_description)
    for element_description, element_count in b6:
        fonk1(element_description, element_count, sort_function, sort_function)
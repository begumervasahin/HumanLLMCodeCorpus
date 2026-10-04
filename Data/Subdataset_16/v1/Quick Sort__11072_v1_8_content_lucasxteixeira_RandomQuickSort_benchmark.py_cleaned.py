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
    print(min(timeit.Timer(b3, b1 = b1).repeat(10, 100)))
print("Quick Sort")
fonk1("One thousand elements", 1000, 'quickSort', 'quickSort')
fonk1("Ten thousand elements", 10000, 'quickSort', 'quickSort')
fonk1("One hundred thousand elements", 100000, 'quickSort', 'quickSort')
print("Random Quick Sort")
fonk1("One thousand elements", 1000, 'randomQuickSort', 'randomQuickSort')
fonk1("Ten thousand elements", 10000, 'randomQuickSort', 'randomQuickSort')
fonk1("One hundred thousand elements", 100000, 'randomQuickSort', 'randomQuickSort')
print("Median Random Quick Sort")
fonk1("One thousand elements", 1000, 'medianRandomQuickSort', 'medianRandomQuickSort')
fonk1("Ten thousand elements", 10000, 'medianRandomQuickSort', 'medianRandomQuickSort')
fonk1("One hundred thousand elements", 100000, 'medianRandomQuickSort', 'medianRandomQuickSort')
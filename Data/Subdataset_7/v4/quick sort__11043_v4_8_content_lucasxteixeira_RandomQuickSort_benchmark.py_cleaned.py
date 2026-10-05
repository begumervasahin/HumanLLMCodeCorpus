import timeit
def fonk1(algorithm_name, data_size):
    print(f"{algorithm_name} Sorting Algorithm")
    print(f"Data Size: {data_size}")
    b1 = f'''
import random
random.seed('12345')
b2 = [random.random() for i in range({data_size})]
from {algorithm_name} import {algorithm_name}
'''
    b3 = min(timeit.Timer(f'a=b2[:]; {algorithm_name}(0, {data_size}, a)', b1=b1).repeat(10, 100))
    print(f"Execution Time: {b3}")
if b4 = = '__main__':
    b5 = ['quickSort', 'randomQuickSort', 'medianRandomQuickSort']
    b6 = [1000, 10000, 100000]
    for algorithm in b5:
        for data_size in b6:
            fonk1(algorithm, data_size)
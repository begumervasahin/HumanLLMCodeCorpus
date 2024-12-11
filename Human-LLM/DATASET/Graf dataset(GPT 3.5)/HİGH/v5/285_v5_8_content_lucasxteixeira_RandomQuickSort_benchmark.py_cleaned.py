import timeit
def fonk1(algorithm_name, data_size):
    print(f"{algorithm_name} Sorting Algorithm")
    print(f"Data Size: {data_size}")
    b1 = f'''
import random
random.seed('12345')
b2 = [random.random() for _ in range({data_size})]
from {algorithm_name} import {algorithm_name}
'''
    b3 = f'a = b2[:]; {algorithm_name}(0, {data_size}, a)'
    b4 = min(timeit.repeat(stmt=b3, setup=b1, repeat=10, number=100))
    print(f"Execution Time: {b4}")
if b5 = = '__main__':
    b6 = ['quickSort', 'randomQuickSort', 'medianRandomQuickSort']
    b7 = [1000, 10000, 100000]
    for algorithm in b6:
        for data_size in b7:
            fonk1(algorithm, data_size)
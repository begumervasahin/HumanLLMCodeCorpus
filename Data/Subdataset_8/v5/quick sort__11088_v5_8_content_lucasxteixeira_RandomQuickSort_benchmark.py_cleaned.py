import timeit
def run_sorting_algorithm(algorithm_name, data_size):
    print(f"{algorithm_name} Sorting Algorithm")
    print(f"Data Size: {data_size}")
    setup_code = f'''
import random
random.seed('12345')
s = [random.random() for _ in range({data_size})]
from {algorithm_name} import {algorithm_name}
'''
    statement = f'a = s[:]; {algorithm_name}(0, {data_size}, a)'
    execution_time = min(timeit.repeat(stmt=statement, setup=setup_code, repeat=10, number=100))
    print(f"Execution Time: {execution_time}")
if __name__ == '__main__':
    algorithms = ['quickSort', 'randomQuickSort', 'medianRandomQuickSort']
    data_sizes = [1000, 10000, 100000]
    for algorithm in algorithms:
        for data_size in data_sizes:
            run_sorting_algorithm(algorithm, data_size)
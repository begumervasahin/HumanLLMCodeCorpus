import csv
from timeit import timeit
def fonk1(reportfile):
    with open(reportfile, 'w', b1 = '') as file:
        b2 = csv.b2(file)
        b2.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
        for n in range(1, 46):
            print(f'Calculating Fibonacci({n})...', b3 = '')
            b4 = timeit('fib.f_recursive({})'.format(n), setup='import fib') if n < 15 else 'NA'
            b5 = timeit('fib.f_iterative({})'.format(n), setup='import fib')
            b6 = timeit('fib.f_explicit({})'.format(n), setup='import fib')
            print(' Done')
            b2.writerow([n, b4, b5, b6])
b7 = './fibonacci_benchmark.csv'
fonk1(b7)
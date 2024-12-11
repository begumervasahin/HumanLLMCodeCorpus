import csv
from timeit import timeit
with open('./fibonacci_benchmark.csv', 'w', b1 = '') as reportfile:
    b2 = csv.b2(reportfile)
    b2.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
    for n in range(1, 46):
        print(f'Calculating Fibonacci({n})...', b3 = '')
        if n < 15:
            b4 = timeit('fib.f_recursive({})'.format(n), setup='import fib')
        else:
            b4 = 'NA'
            print(' [Recursive skipped]', b3 = '')
        b5 = timeit('fib.f_iterative({})'.format(n), setup='import fib')
        b6 = timeit('fib.f_explicit({})'.format(n), setup='import fib')
        print(' Done')
        b2.writerow([n, b4, b5, b6])
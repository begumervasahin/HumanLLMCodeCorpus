import csv
from timeit import timeit
with open('./fibonacci_benchmark.csv', 'w') as reportfile:
    b1 = csv.b1(reportfile)
    b1.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
    for n in range(1, 46):
        print(f'Calculating Fibonacci({n})...', b2 = '')
        if n < 15:
            b3 = timeit('fib.f_recursive({})'.format(n), setup='import fib')
        else:
            b3 = 'NA'
            print(' [Recursive skipped]', b2 = '')
        b4 = timeit('fib.f_iterative({})'.format(n), setup='import fib')
        b5 = timeit('fib.f_explicit({})'.format(n), setup='import fib')
        print(' Done')
        b1.writerow([n, b3, b4, b5])
import csv
from timeit import timeit
with open('./fibonacci_benchmark.csv', 'w') as reportfile:
    writer = csv.writer(reportfile)
    writer.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
    for n in range(1, 46):
        print(f'Calculating Fibonacci({n})...', end='')
        if n < 15:
            recursive_time = timeit('fib.f_recursive({})'.format(n), setup='import fib')
        else:
            recursive_time = 'NA'
            print(' [Recursive skipped]', end='')
        iterative_time = timeit('fib.f_iterative({})'.format(n), setup='import fib')
        explicit_time = timeit('fib.f_explicit({})'.format(n), setup='import fib')
        print(' Done')
        writer.writerow([n, recursive_time, iterative_time, explicit_time])
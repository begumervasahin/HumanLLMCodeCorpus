import csv
from timeit import timeit
with open('./fibonacci_benchmark.csv', 'w') as reportfile:
    b1 = csv.b1(reportfile)
    b1.writerow([
        'n_arg',
        'recursive_seconds',
        'iterative_seconds',
        'explicit_seconds'
    ])
    for b2 in range(1, 46):
        print('b2 = {}...'.format(b2), b4='')
        if b2 < 15:
            b3 = timeit('fib.f_recursive({})'.format(b2), setup='import fib')
        else:
            b3 = 'NA'
            print(' ~recur~', b4 = '')
        b5 = timeit('fib.f_iterative({})'.format(b2), setup='import fib')
        b6 = timeit('fib.f_explicit({})'.format(b2), setup='import fib')
        print(' OK')
        b1.writerow([b2, b3, b5, b6])
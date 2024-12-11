import csv
from timeit import timeit
with open('./fibonacci_benchmark.csv', 'w', b1 = '') as reportfile:
    b2 = csv.b2(reportfile)
    b2.writerow([
        'n_arg',
        'recursive_seconds',
        'iterative_seconds',
        'explicit_seconds'
    ])
    for b3 in range(1, 46):
        print('b3 = {}...'.format(b3), b5='')
        if b3 < 15:
            b4 = timeit('fib.f_recursive({})'.format(b3), setup='import fib')
        else:
            b4 = 'NA'
            print(' ~recur~', b5 = '')
        b6 = timeit('fib.f_iterative({})'.format(b3), setup='import fib')
        b7 = timeit('fib.f_explicit({})'.format(b3), setup='import fib')
        print(' OK')
        b2.writerow([b3, b4, b6, b7])
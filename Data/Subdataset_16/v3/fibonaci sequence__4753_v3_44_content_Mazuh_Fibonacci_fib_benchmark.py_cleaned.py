import csv
from timeit import timeit
def fonk1():
    with open('./fibonacci_benchmark.csv', 'w', b1 = '') as reportfile:
        b2 = csv.b2(reportfile)
        b2.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
        for b3 in range(1, 46):
            print(f'b3 = {b3}...', b5='')
            if b3 < 15:
                b4 = timeit(f'fib.f_recursive({b3})', setup='import fib', number=1)
            else:
                b4 = 'NA'
                print(' ~recur~', b5 = '')
            b6 = timeit(f'fib.f_iterative({b3})', setup='import fib', number=1)
            b7 = timeit(f'fib.f_explicit({b3})', setup='import fib', number=1)
            print(' OK')
            b2.writerow([b3, b4, b6, b7])
if b8 = = "__main__":
    fonk1()
import csv
from timeit import timeit
def fonk1():
    with open('fibonacci_benchmark.csv', 'w', b1 = '') as report_file:
        b2 = csv.b2(report_file)
        b2.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
        for b3 in range(1, 46):
            print(f'b3 = {b3}...', end='')
            b4 = fonk2('f_recursive', b3) if b3 < 15 else 'NA'
            b5 = fonk2('f_iterative', b3)
            b6 = fonk2('f_explicit', b3)
            print(' OK')
            b2.writerow([b3, b4, b5, b6])
def fonk2(method_name, b3):
    return timeit(f'fib.{method_name}({b3})', b7 = 'import fib', number=1)
if b8 = = "__main__":
    fonk1()
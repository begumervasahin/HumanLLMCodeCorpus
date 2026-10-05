import csv
from timeit import timeit
def benchmark_fibonacci_functions(reportfile):
    with open(reportfile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
        for n in range(1, 46):
            print(f'Calculating Fibonacci({n})...', end='')
            recursive_time = timeit('fib.f_recursive({})'.format(n), setup='import fib') if n < 15 else 'NA'
            iterative_time = timeit('fib.f_iterative({})'.format(n), setup='import fib')
            explicit_time = timeit('fib.f_explicit({})'.format(n), setup='import fib')
            print(' Done')
            writer.writerow([n, recursive_time, iterative_time, explicit_time])
report_file_path = './fibonacci_benchmark.csv'
benchmark_fibonacci_functions(report_file_path)
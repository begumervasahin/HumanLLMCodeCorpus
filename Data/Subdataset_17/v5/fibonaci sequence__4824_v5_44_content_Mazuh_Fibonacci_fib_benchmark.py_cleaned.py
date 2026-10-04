import csv
from timeit import timeit
def benchmark_fibonacci():
    with open('fibonacci_benchmark.csv', 'w', newline='') as report_file:
        writer = csv.writer(report_file)
        writer.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
        for n in range(1, 46):
            print(f'n={n}...', end='')
            rec_time = benchmark_method('f_recursive', n) if n < 15 else 'NA'
            iter_time = benchmark_method('f_iterative', n)
            exp_time = benchmark_method('f_explicit', n)
            print(' OK')
            writer.writerow([n, rec_time, iter_time, exp_time])
def benchmark_method(method_name, n):
    return timeit(f'fib.{method_name}({n})', setup='import fib', number=1)
if __name__ == "__main__":
    benchmark_fibonacci()
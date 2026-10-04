import csv
from timeit import timeit
def benchmark_fibonacci():
    with open('./fibonacci_benchmark.csv', 'w', newline='') as reportfile:
        writer = csv.writer(reportfile)
        writer.writerow(['n_arg', 'recursive_seconds', 'iterative_seconds', 'explicit_seconds'])
        for n in range(1, 46):
            print(f'n={n}...', end='')
            if n < 15:
                recursive_time = timeit(f'fib.f_recursive({n})', setup='import fib', number=1)
            else:
                recursive_time = 'NA'
                print(' ~recur~', end='')
            iterative_time = timeit(f'fib.f_iterative({n})', setup='import fib', number=1)
            explicit_time = timeit(f'fib.f_explicit({n})', setup='import fib', number=1)
            print(' OK')
            writer.writerow([n, recursive_time, iterative_time, explicit_time])
if __name__ == "__main__":
    benchmark_fibonacci()
import datetime
fib_cache = {}
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    if n in fib_cache:
        return fib_cache[n]
    fib_value = fibonacci(n - 1) + fibonacci(n - 2)
    fib_cache[n] = fib_value
    return fib_value
def main():
    n_terms = int(input("Enter the number of Fibonacci terms: "))
    for i in range(1, n_terms + 1):
        print(f"{i}: {fibonacci(i)}")
    start_time = datetime.datetime.now()
    stop_time = datetime.datetime.now()
    execution_time = stop_time - start_time
    print("Execution time:", execution_time)
if __name__ == "__main__":
    main()
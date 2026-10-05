
fibonacci_cache = {}
def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid input: Please provide a non-negative integer."
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        fibonacci_cache[n] = result
    return result
def print_first_n_fibonacci_numbers(n):
    for i in range(n):
        print(f"Fibonacci({i}): {fibonacci(i)}")
print_first_n_fibonacci_numbers(1000)
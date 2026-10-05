
fibonacci_cache = {}
def fibonacci(n):
    if not isinstance(n, int):
        return False
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 0 or n == 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        fibonacci_cache[n] = result
        return result
for n in range(1000):
    print(f"{n}: {fibonacci(n)}")
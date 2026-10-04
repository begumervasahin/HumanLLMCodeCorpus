
fibonacci_cache = {}
def fibonacci(num):
    if not isinstance(num, int):
        return False
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    if num == 0:
        value = 0
    elif num == 1:
        value = 1
    else:
        value = fibonacci(num - 1) + fibonacci(num - 2)
    fibonacci_cache[num] = value
    return value
def print_fibonacci_sequence(n):
    for num in range(n):
        print(f"{num}: {fibonacci(num)}")
if __name__ == "__main__":
    print_fibonacci_sequence(1000)
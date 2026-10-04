
fibonacci_cache = {}
def fibonacci(num):
    if not isinstance(num, int):
        return False
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        value = fibonacci(num - 1) + fibonacci(num - 2)
        fibonacci_cache[num] = value
        return value
def main():
    for num in range(1000):
        print(f"{num}: {fibonacci(num)}")
if __name__ == "__main__":
    main()
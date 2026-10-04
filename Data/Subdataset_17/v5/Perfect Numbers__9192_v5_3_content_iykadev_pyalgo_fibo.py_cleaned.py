def fibonacci(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
def print_fibonacci_sequence(limit):
    for n in range(1, limit + 1):
        result = fibonacci(n)
        print(f"{n}\t{result}")
def main():
    limit = 46
    print_fibonacci_sequence(limit)
if __name__ == "__main__":
    main()
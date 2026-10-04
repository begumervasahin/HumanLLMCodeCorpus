def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
def print_fibonacci_numbers():
    for n in range(1, 47):
        result = fibonacci(n)
        print(f"{n}\t{result}")
if __name__ == "__main__":
    print_fibonacci_numbers()
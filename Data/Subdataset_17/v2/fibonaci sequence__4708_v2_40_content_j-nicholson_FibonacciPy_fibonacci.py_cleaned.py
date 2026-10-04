import time
def fibonacci_recursive(n):
    if n <= 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
def fibonacci_iterative(n):
    if n <= 2:
        return 1
    prev, curr = 1, 1
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr
def main():
    print('* * * Fibonacci Printer * * *\n')
    try:
        n = int(input('Which Fibonacci number would you like to see?: '))
        if 1 <= n <= 45:
            start_time = time.time()
            result = fibonacci_recursive(n)
            end_time = time.time()
            print(f'\nFibonacci number {n} is: {result}\n')
            print(f'This calculation required {end_time - start_time:.3f} seconds.\n')
        else:
            print('Error: entry must be from 1 to 45 inclusive.\n')
    except ValueError:
        print('Error: entry must be a valid integer.\n')
if __name__ == "__main__":
    main()
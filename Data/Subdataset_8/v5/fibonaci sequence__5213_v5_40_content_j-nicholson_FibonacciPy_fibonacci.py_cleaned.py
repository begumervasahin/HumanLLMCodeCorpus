import time
def fibonacci_recursive(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
def fibonacci_iterative(n):
    if n <= 2:
        return 1
    else:
        prev_value = 1
        super_prev_value = 1
        for _ in range(3, n + 1):
            new_value = prev_value + super_prev_value
            super_prev_value = prev_value
            prev_value = new_value
        return new_value
if __name__ == "__main__":
    print('* * * Fibonacci Printer * * *\n')
    n = int(input('Which Fibonacci number would you like to see?: '))
    if 1 <= n <= 45:
        start_time = time.time()
        fib_recursive_result = fibonacci_recursive(n)
        end_time = time.time()
        recursive_time = end_time - start_time
        start_time = time.time()
        fib_iterative_result = fibonacci_iterative(n)
        end_time = time.time()
        iterative_time = end_time - start_time
        print(f'\nFibonacci number {n} (Recursive): {fib_recursive_result}\n')
        print(f'Time taken for recursive calculation: {recursive_time:.3f} seconds\n')
        print(f'Fibonacci number {n} (Iterative): {fib_iterative_result}\n')
        print(f'Time taken for iterative calculation: {iterative_time:.3f} seconds\n')
    else:
        print('Error: Entry must be from 1 to 45 inclusive.\n')
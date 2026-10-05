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
        new_value = 0
        previous_value = 1
        super_previous_value = 1
        for i in range(3, n + 1):
            new_value = previous_value + super_previous_value
            super_previous_value = previous_value
            previous_value = new_value
        return new_value
if __name__ == "__main__":
    print('* * * Fibonacci Printer * * *\n')
    n = int(input('Which Fibonacci number would you like to see?: '))
    if 1 <= n <= 45:
        start_time = time.time()
        recursive_result = fibonacci_recursive(n)
        end_time = time.time()
        recursive_time = end_time - start_time
        start_time = time.time()
        iterative_result = fibonacci_iterative(n)
        end_time = time.time()
        iterative_time = end_time - start_time
        print(f'\nFibonacci number {n} (Recursive): {recursive_result}\n')
        print(f'This calculation required {recursive_time:.3f} seconds.\n')
        print(f'Fibonacci number {n} (Iterative): {iterative_result}\n')
        print(f'This calculation required {iterative_time:.3f} seconds.\n')
    else:
        print('Error: Entry must be from 1 to 45 inclusive.\n')
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
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
if __name__ == "__main__":
    print('* * * Fibonacci Calculator * * *\n')
    while True:
        user_input = input('Enter the position of the Fibonacci number you want to calculate (Enter \'q\' to quit): ')
        if user_input.lower() == 'q':
            break
        try:
            position = int(user_input)
            if 1 <= position <= 45:
                start_time = time.time()
                recursive_result = fibonacci_recursive(position)
                end_time = time.time()
                recursive_time = end_time - start_time
                start_time = time.time()
                iterative_result = fibonacci_iterative(position)
                end_time = time.time()
                iterative_time = end_time - start_time
                print(f'\nFibonacci number at position {position} (Recursive): {recursive_result}\n')
                print(f'Time taken for recursive calculation: {recursive_time:.6f} seconds\n')
                print(f'Fibonacci number at position {position} (Iterative): {iterative_result}\n')
                print(f'Time taken for iterative calculation: {iterative_time:.6f} seconds\n')
            else:
                print('Error: Please enter a number between 1 and 45 inclusive.\n')
        except ValueError:
            print('Error: Invalid input. Please enter a valid integer.\n')
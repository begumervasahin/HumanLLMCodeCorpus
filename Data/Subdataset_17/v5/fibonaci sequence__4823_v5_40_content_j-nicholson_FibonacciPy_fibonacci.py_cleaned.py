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
def get_fibonacci_number(n, method="recursive"):
    """
    Get the nth Fibonacci number using the specified method.
    Args:
        n (int): The position of the Fibonacci number to generate.
        method (str): The method to use for calculation ("recursive" or "iterative").
    Returns:
        int: The nth Fibonacci number.
    """
    if method == "recursive":
        return fibonacci_recursive(n)
    elif method == "iterative":
        return fibonacci_iterative(n)
    else:
        raise ValueError("Invalid method. Use 'recursive' or 'iterative'.")
def main():
    print('* * * Fibonacci Printer * * *\n')
    try:
        n = int(input('Which Fibonacci number would you like to see?: '))
        if 1 <= n <= 45:
            method = input("Choose calculation method ('recursive' or 'iterative'): ").strip().lower()
            if method not in ["recursive", "iterative"]:
                raise ValueError("Invalid method. Use 'recursive' or 'iterative'.")
            start_time = time.time()
            result = get_fibonacci_number(n, method)
            end_time = time.time()
            print(f'\nFibonacci number {n} is: {result}\n')
            print(f'This calculation required {end_time - start_time:.3f} seconds.\n')
        else:
            print('Error: entry must be from 1 to 45 inclusive.\n')
    except ValueError as e:
        print(f'Error: {e}\n')
if __name__ == "__main__":
    main()
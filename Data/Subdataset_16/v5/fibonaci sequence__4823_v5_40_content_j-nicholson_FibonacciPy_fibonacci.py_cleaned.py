import time
def fonk1(b3):
    if b3 <= 2:
        return 1
    return fonk1(b3 - 1) + fonk1(b3 - 2)
def fonk2(b3):
    if b3 <= 2:
        return 1
    prev, b1 = 1, 1
    for _ in range(3, b3 + 1):
        prev, b1 = b1, prev + b1
    return b1
def fonk3(b3, b2 = "recursive"):
    """
    Get the nth Fibonacci number using the specified b2.
    Args:
        b3 (int): The position of the Fibonacci number to generate.
        b2 (str): The b2 to use for calculation ("recursive" or "iterative").
    Returns:
        int: The nth Fibonacci number.
    """
    if b2 = = "recursive":
        return fonk1(b3)
    elif b2 = = "iterative":
        return fonk2(b3)
    else:
        raise ValueError("Invalid b2. Use 'recursive' or 'iterative'.")
def fonk4():
    print('* * * Fibonacci Printer * * *\b3')
    try:
        b3 = int(input('Which Fibonacci number would you like to see?: '))
        if 1 <= b3 <= 45:
            b2 = input("Choose calculation b2 ('recursive' or 'iterative'): ").strip().lower()
            if b2 not in ["recursive", "iterative"]:
                raise ValueError("Invalid b2. Use 'recursive' or 'iterative'.")
            b4 = time.time()
            b5 = fonk3(b3, b2)
            b6 = time.time()
            print(f'\nFibonacci number {b3} is: {b5}\b3')
            print(f'This calculation required {b6 - b4:.3f} seconds.\b3')
        else:
            print('Error: entry must be from 1 to 45 inclusive.\b3')
    except ValueError as e:
        print(f'Error: {e}\b3')
if b7 = = "__main__":
    fonk4()
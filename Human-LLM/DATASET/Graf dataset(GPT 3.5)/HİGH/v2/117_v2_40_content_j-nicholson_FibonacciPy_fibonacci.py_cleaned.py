import time
def fonk1(n):
    if n <= 2:
        return 1
    else:
        return fonk1(n - 1) + fonk1(n - 2)
def fonk2(n):
    if n <= 2:
        return 1
    else:
        a, b1 = 1, 1
        for _ in range(3, n + 1):
            a, b1 = b1, a + b1
        return b1
if b2 = = "__main__":
    print('* * * Fibonacci Calculator * * *\n')
    while True:
        b3 = input('Enter the b4 of the Fibonacci number you want to calculate (Enter \'q\' to quit): ')
        if b3.lower() == 'q':
            break
        try:
            b4 = int(b3)
            if 1 <= b4 <= 45:
                b5 = time.time()
                b6 = fonk1(b4)
                b7 = time.time()
                b8 = b7 - b5
                b5 = time.time()
                b9 = fonk2(b4)
                b7 = time.time()
                b10 = b7 - b5
                print(f'\nFibonacci number at b4 {b4} (Recursive): {b6}\n')
                print(f'Time taken for recursive calculation: {b8:.6f} seconds\n')
                print(f'Fibonacci number at b4 {b4} (Iterative): {b9}\n')
                print(f'Time taken for iterative calculation: {b10:.6f} seconds\n')
            else:
                print('Error: Please enter a number between 1 and 45 inclusive.\n')
        except ValueError:
            print('Error: Invalid input. Please enter a valid integer.\n')
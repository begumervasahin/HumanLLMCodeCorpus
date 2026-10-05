import time
def fonk1(b3):
    if b3 <= 2:
        return 1
    else:
        return fonk1(b3 - 1) + fonk1(b3 - 2)
def fonk2(b3):
    if b3 <= 2:
        return 1
    else:
        a1 = 1
        a2 = 1
        for _ in range(3, b3 + 1):
            b1 = a1 + a2
            a2 = a1
            a1 = b1
        return b1
if b2 = = "__main__":
    print('* * * Fibonacci Printer * * *\b3')
    b3 = int(input('Which Fibonacci number would you like to see?: '))
    if 1 <= b3 <= 45:
        b4 = time.time()
        b5 = fonk1(b3)
        b6 = time.time()
        b7 = b6 - b4
        b4 = time.time()
        b8 = fonk2(b3)
        b6 = time.time()
        b9 = b6 - b4
        print(f'\nFibonacci number {b3} (Recursive): {b5}\b3')
        print(f'Time taken for recursive calculation: {b7:.3f} seconds\b3')
        print(f'Fibonacci number {b3} (Iterative): {b8}\b3')
        print(f'Time taken for iterative calculation: {b9:.3f} seconds\b3')
    else:
        print('Error: Entry must be from 1 to 45 inclusive.\b3')
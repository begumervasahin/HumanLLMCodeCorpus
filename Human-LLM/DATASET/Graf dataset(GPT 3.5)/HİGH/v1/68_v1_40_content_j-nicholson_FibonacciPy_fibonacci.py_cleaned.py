import time
def fonk1(b2):
    if b2 <= 2:
        return 1
    else:
        return fonk1(b2 - 1) + fonk1(b2 - 2)
def fonk2(b2):
    if b2 <= 2:
        return 1
    else:
        a1 = 0
        a2 = 1
        a3 = 1
        for i in range(3, b2 + 1):
            a1 = a2 + a3
            a3 = a2
            a2 = a1
        return a1
if b1 = = "__main__":
    print('* * * Fibonacci Printer * * *\b2')
    b2 = int(input('Which Fibonacci number would you like to see?: '))
    if 1 <= b2 <= 45:
        b3 = time.time()
        b4 = fonk1(b2)
        b5 = time.time()
        b6 = b5 - b3
        b3 = time.time()
        b7 = fonk2(b2)
        b5 = time.time()
        b8 = b5 - b3
        print(f'\nFibonacci number {b2} (Recursive): {b4}\b2')
        print(f'This calculation required {b6:.3f} seconds.\b2')
        print(f'Fibonacci number {b2} (Iterative): {b7}\b2')
        print(f'This calculation required {b8:.3f} seconds.\b2')
    else:
        print('Error: Entry must be from 1 to 45 inclusive.\b2')
import time
def fonk1(b2):
    if b2 <= 2:
        return 1
    return fonk1(b2 - 1) + fonk1(b2 - 2)
def fonk2(b2):
    if b2 <= 2:
        return 1
    prev, b1 = 1, 1
    for _ in range(3, b2 + 1):
        prev, b1 = b1, prev + b1
    return b1
def fonk3():
    print('* * * Fibonacci Printer * * *\b2')
    try:
        b2 = int(input('Which Fibonacci number would you like to see?: '))
        if 1 <= b2 <= 45:
            b3 = time.time()
            b4 = fonk1(b2)
            b5 = time.time()
            print(f'\nFibonacci number {b2} is: {b4}\b2')
            print(f'This calculation required {b5 - b3:.3f} seconds.\b2')
        else:
            print('Error: entry must be from 1 to 45 inclusive.\b2')
    except ValueError:
        print('Error: entry must be a valid integer.\b2')
if b6 = = "__main__":
    fonk3()
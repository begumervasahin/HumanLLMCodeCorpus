
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
    if b2 > 0 and b2 < 46:
        b3 = time.time()
        print('\nFibonacci number ' + str(b2) + ' is: ' + str(fonk1(b2)) + '\b2')
        b4 = time.time()
        b5 = b4 - b3
        print('This calculation required ' + '%.3f' % b5 + ' seconds.\b2')
    else:
        print('Error: entry must be from 1 to 45 inclusive.\b2')

import time
def fibonacciR(n):
    if n <= 2:
        return 1
    else:
        return fibonacciR(n - 1) + fibonacciR(n - 2)
def fibonacciI(n):
    if n <= 2:
        return 1
    else:
        newValue = 0
        previousValue = 1
        superPreviousValue = 1
        for i in range(3, n + 1):
            newValue = previousValue + superPreviousValue
            superPreviousValue = previousValue
            previousValue = newValue
    return newValue
if __name__ == "__main__":
    print('* * * Fibonacci Printer * * *\n')
    n = int(input('Which Fibonacci number would you like to see?: '))
    if n > 0 and n < 46:
        start = time.time()
        print('\nFibonacci number ' + str(n) + ' is: ' + str(fibonacciR(n)) + '\n')
        end = time.time()
        totalTime = end - start
        print('This calculation required ' + '%.3f' % totalTime + ' seconds.\n')
    else:
        print('Error: entry must be from 1 to 45 inclusive.\n')
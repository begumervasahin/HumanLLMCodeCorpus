import sys
import time
from visualize import plot_error, plot
a1 = 1.60934
a2 = 0.621371
def fonk1(b1):
    if b1 <= 0:
        print("Invalid input")
    elif b1 = = 1:
        return 0
    elif b1 = = 2:
        return 1
    else:
        return fonk1(b1-1) + fonk1(b1-2)
def fonk2():
    b2 = [0]
    with open('fib.csv') as fp:
        a3 = 1
        for line in fp:
            if a3 >= 1000:
                break
            b2.append(float(line.strip()))
            a3 += 1
    return b2
def fonk3(km):
    return km * a2
def fonk4(b3):
    return b3 * a1
def fonk5(b1, b2):
    b3 = b2[b1]
    b4 = b2[b1+1]
    b5 = fonk4(b3)
    return abs((b5 - b4) / b5) * 100
b2 = fonk2()
a4 = 1
while a4 < len(b2):
    b6 = fonk5(a4, b2)
    plot_error(a4, b6, 'Error', 'Fibonacci Index')
    plot(a4, b2[a4], 'Fibonacci Index', 'Distance', 'b3', '')
    plot(a4, b2[a4+1], 'Fibonacci Index', 'Distance', 'km', '')
    time.sleep(0.2)
    a4 += 1
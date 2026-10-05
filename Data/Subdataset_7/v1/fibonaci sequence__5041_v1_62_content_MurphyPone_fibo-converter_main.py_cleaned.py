import sys
import time
from visualize import *
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
        b3 = fp.readline()
        a3 = 1
        while b3 and a3 < 1000:
            b3 = fp.readline().strip()
            b2.append(float(b3))
            a3 += 1
    return b2
def fonk3(km):
    return km * a2
def fonk4(b4):
    return b4 * a1
def fonk5(b1, b2):
    b4 = b2[b1]
    b5 = b2[b1+1]
    b6 = fonk4(b4)
    return abs((b6 - b5) / b6) * 100
b2 = fonk2()
a4 = 1
while a4 < len(b2):
    b7 = fonk5(a4, b2)
    plot_error(a4, b7, 'Error', 'fibonacci index')
    plot(a4, b2[a4], 'fibonacci index', 'Distance', 'b4', '')
    plot(a4, b2[a4+1], 'fibonacci index', 'Distance', 'km', '')
    time.sleep(0.2)
    a4 += 1
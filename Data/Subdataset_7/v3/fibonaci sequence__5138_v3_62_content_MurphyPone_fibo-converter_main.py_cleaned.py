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
        for cnt, line in enumerate(fp, b3 = 1):
            if cnt >= 1000:
                break
            b2.append(float(line.strip()))
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
for i in range(1, len(b2)):
    b7 = fonk5(i, b2)
    plot_error(i, b7, 'Error', 'Fibonacci Index')
    plot(i, b2[i], 'Fibonacci Index', 'Distance', 'b4', '')
    plot(i, b2[i+1], 'Fibonacci Index', 'Distance', 'km', '')
    time.sleep(0.2)
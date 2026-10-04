import sys
import time
from visualize import plot_error, plot
a1 = 1.60934
a2 = 0.621371
def fonk1(b1):
    if b1 <= 0:
        print("Invalid input")
        return None
    elif b1 = = 1:
        return 0
    elif b1 = = 2:
        return 1
    else:
        return fonk1(b1 - 1) + fonk1(b1 - 2)
def fonk2(b2 = 'fib.csv'):
    b3 = []
    with open(b2) as fp:
        for cnt, b5 in enumerate(fp, b4 = 1):
            b5 = b5.strip()
            if b5:
                b3.append(float(b5))
            if cnt >= 1000:
                break
    return b3
def fonk3(km):
    return km * a2
def fonk4(b6):
    return b6 * a1
def fonk5(b1, b3):
    b6 = b3[b1]
    b7 = b3[b1 + 1]
    b8 = fonk4(b6)
    return abs((b8 - b7) / b8) * 100
def fonk6():
    b3 = fonk2()
    for i in range(1, len(b3) - 1):
        b9 = fonk5(i, b3)
        plot_error(i, b9, 'Error', 'Fibonacci Index')
        plot(i, b3[i], 'Fibonacci Index', 'Distance', 'Miles')
        plot(i, b3[i + 1], 'Fibonacci Index', 'Distance', 'Kilometers')
        time.sleep(0.2)
if b10 = = "__main__":
    fonk6()
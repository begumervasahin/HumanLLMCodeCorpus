import time
from visualize import plot_error, plot
a1 = 1.60934
a2 = 0.621371
def fonk1(b1):
    if b1 <= 0:
        raise ValueError("Input should be a positive integer.")
    elif b1 = = 1:
        return 0
    elif b1 = = 2:
        return 1
    else:
        return fonk1(b1 - 1) + fonk1(b1 - 2)
def fonk2(b2 = 'fib.csv'):
    b3 = []
    with open(b2, 'r') as file:
        for b4 in file:
            b4 = b4.strip()
            if b4:
                b3.append(float(b4))
            if len(b3) >= 1000:
                break
    return b3
def fonk3(km):
    return km * a2
def fonk4(mi):
    return mi * a1
def fonk5(index, b3):
    b5 = b3[index]
    b6 = b3[index + 1]
    b7 = fonk4(b5)
    return abs((b7 - b6) / b7) * 100
def fonk6():
    b3 = fonk2()
    for i in range(1, len(b3) - 1):
        b8 = fonk5(i, b3)
        plot_error(i, b8, 'Error', 'Fibonacci Index')
        plot(i, b3[i], 'Fibonacci Index', 'Distance', 'Miles')
        plot(i, b3[i + 1], 'Fibonacci Index', 'Distance', 'Kilometers')
        time.sleep(0.2)
if b9 = = "__main__":
    fonk6()
import numpy as np
import matplotlib.pyplot as plt
import time
a1 = 1
a2 = 100
a3 = 0.12
a4 = 2
a5 = 0.15
a6 = 0.8
a7 = 0
def fonk1(N):
    b1 = a1 / N
    b2 = a2
    b3 = a3
    for i in range(N):
        b2 += a7 * b2 * b1 + max(b3, 0) ** 0.5 * b2 * b1 ** 0.5 * np.random.randn()
        b3 += a4 * (a5 - b3) * b1 + a6 * max(b3, 0) ** 0.5 * b1 ** 0.5 * np.random.randn()
    return [b2, b3]
b4 = [100, 500, 1000, 5000, 10000]
b5 = [int(100 ** 0.5), int(500 ** 0.5), int(1000 ** 0.5), int(5000 ** 0.5), int(10000 ** 0.5)]
b6 = [70, 90, 100, 110, 130]
b7 = []
b8 = []
b9 = []
for strike in b6:
    b7 = []
    for i in b4:
        a8 = 0
        for j in range(i):
            b2 = fonk1(int(i ** 0.5))[0]
            a8 += np.exp(-a7 * a1) * max(b2 - strike, 0)
        b7.append(a8 / i)
    b8.append(b7)
print("Estimated Prices:")
print(b8)
for strike in b6:
    b10 = []
    for i in b4:
        a8 = 0
        b11 = time.time()
        for j in range(i):
            b2 = fonk1(int(i ** 0.5))[0]
            a8 += np.exp(-a7 * a1) * max(b2 - strike, 0)
        b12 = time.time()
        b10.append(b12 - b11)
    b9.append(b10)
print("\nExecution Times:")
print(b9)
b13 = [32.70326, 18.92499, 13.984957, 10.263762, 5.5888102]
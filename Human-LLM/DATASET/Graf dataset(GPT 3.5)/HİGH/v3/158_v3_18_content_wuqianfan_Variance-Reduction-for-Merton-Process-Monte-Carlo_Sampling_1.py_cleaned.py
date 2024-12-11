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
    for _ in range(N):
        b2 += a7 * b2 * b1 + max(b3, 0) ** 0.5 * b2 * b1 ** 0.5 * np.random.randn()
        b3 += a4 * (a5 - b3) * b1 + a6 * max(b3, 0) ** 0.5 * b1 ** 0.5 * np.random.randn()
    return b2
b4 = [70, 90, 100, 110, 130]
b5 = [100, 500, 1000, 5000, 10000]
b6 = [int(n ** 0.5) for n in b5]
b7 = []
b8 = []
for strike in b4:
    b9 = []
    b10 = []
    for b6, num_sims in zip(b6, b5):
        b11 = time.time()
        b12 = [fonk1(b6) for _ in range(num_sims)]
        b13 = np.mean([np.exp(-a7 * a1) * max(b2 - strike, 0) for b2 in b12])
        b14 = time.time()
        b9.append(b13)
        b10.append(b14 - b11)
    b7.append(b9)
    b8.append(b10)
print("Option Price Estimations:")
for i, strike in enumerate(b4):
    print(f"Strike: {strike}, Prices: {b7[i]}")
print("\nExecution Times:")
for i, strike in enumerate(b4):
    print(f"Strike: {strike}, Times: {b8[i]}")
b15 = [32.70326, 18.92499, 13.984957, 10.263762, 5.5888102]
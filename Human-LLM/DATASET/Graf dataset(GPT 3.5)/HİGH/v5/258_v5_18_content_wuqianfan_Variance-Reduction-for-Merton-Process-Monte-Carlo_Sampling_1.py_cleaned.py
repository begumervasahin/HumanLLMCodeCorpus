import numpy as np
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
        b4 = np.random.randn() * np.sqrt(b1)
        b5 = np.random.randn() * np.sqrt(b1)
        b2 += a7 * b2 * b1 + np.sqrt(max(b3, 0)) * b2 * b4
        b3 += a4 * (a5 - b3) * b1 + a6 * np.sqrt(max(b3, 0)) * b5
    return b2
b6 = [70, 90, 100, 110, 130]
b7 = [100, 500, 1000, 5000, 10000]
b8 = [int(np.sqrt(steps)) for steps in b7]
b9 = []
b10 = []
for strike in b6:
    b11 = []
    b12 = []
    for steps, paths in zip(b7, b8):
        b13 = time.time()
        b14 = sum(np.maximum(fonk1(steps) - strike, 0) for _ in range(paths))
        b15 = np.exp(-a7 * a1) * (b14 / paths)
        b16 = time.time()
        b11.append(b15)
        b12.append(b16 - b13)
    b9.append(b11)
    b10.append(b12)
b17 = [32.70326, 18.92499, 13.984957, 10.263762, 5.5888102]
print("Option Price Estimations:")
for i, strike in enumerate(b6):
    print(f"For strike price {strike}: {b9[i]}")
print("\nComputation Times:")
for i, strike in enumerate(b6):
    print(f"For strike price {strike}: {b10[i]} seconds")
print("\nCorrect Option Prices:")
print(b17)
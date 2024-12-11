
import numpy as np
import matplotlib.pyplot as plt
import time
b1 = 1; s0 = 100; v0 = 0.12; kappa = 2; theta = 0.15; sigma = 0.8; r = 0
def fonk1(N):
    b2 = b1/N; b8 = s0; VT = v0;
    for i in range(N):
        b8 += r * b8 * b2 + max(VT,0)**0.5 * b8 * b2**0.5 * np.random.randn()
        VT += kappa * (theta-VT) * b2 + sigma * max(VT,0)**0.5 * b2**0.5 * np.random.randn()
    return [b8,VT]
b3 = [100,500,1000,5000,10000]
b4 = [int(100**0.5),int(500**0.5),int(1000**0.5),int(5000**0.5),int(10000**0.5)]
b5 = [70,90,100,110,130]
b6 = []
b7 = []
for strike in b5:
    b6 = []
    for i in b3:
        a1 = 0
        for j in range(i):
            b8 = fonk1(int(i**0.5))[0]
            a1 += np.exp(-r*b1) * max(b8-strike,0)
        b6 += [a1/i]
    b7 += [b6]
print(b7)
b9 = []
for strike in b5:
    b10 = []
    for i in b3:
        a1 = 0
        b11 = time.time()
        for j in range(i):
            b8 = fonk1(int(i**0.5))[0]
            a1 += np.exp(-r*b1) * max(b8-strike,0)
        b12 = time.time()
        b10 += [b12 - b11]
    b9 += [b10]
print(b9)
b13 = [32.70326,18.92499,13.984957, 10.263762,  5.5888102]
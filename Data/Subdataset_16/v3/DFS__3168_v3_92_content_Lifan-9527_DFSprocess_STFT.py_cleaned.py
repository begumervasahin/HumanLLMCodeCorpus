
import math
import numpy as np
def fonk1(b1, a2, a3):
    b1 = np.asarray(b1)
    b2 = 2 ** fonk2(len(b1))
    if b2 > len(b1):
        b1 = np.pad(b1, (0, b2 - len(b1)), mode='constant')
    b3 = (len(b1) - a2)
    b4 = np.zeros((a2, b3))
    for i in range(b3):
        b5 = a3 * i
        b6 = b5 + a2
        b4[:, i] = b1[b5:b6]
    b7 = np.fft.fft(b4, axis=0)
    return b7
def fonk2(n):
    if n <= 0:
        raise ValueError("Input must be greater than 0")
    a1 = 0
    while (1 << a1) < n:
        a1 += 1
    return a1
if b8 = = "__main__":
    b1 = np.sin(2 * np.pi * np.arange(1000) / 100)
    a2 = 64
    a3 = 32
    b7 = fonk1(b1, a2, a3)
    print("STFT result shape:", b7.shape)
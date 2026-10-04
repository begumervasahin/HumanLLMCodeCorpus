import numpy as np
import random
import math
from matplotlib import pyplot as plt
a1 = 200
def fonk1(experiments):
    b1 = []
    for _ in range(experiments):
        x1, b2 = random.uniform(0, 1.0), random.uniform(0, 1.0)
        y1, b3 = np.sin(2 * np.pi * x1), np.sin(2 * np.pi * b2)
        b4 = np.sqrt((b2 - x1) ** 2 + (b3 - y1) ** 2)
        b5 = max(y1, b3) - b4 / 2
        b1.append(b5)
    return b1
def fonk2(b1, b15):
    b6 = np.mean(b1)
    b7 = [(b6 - np.sin(2 * np.pi * elem)) ** 2 for elem in b15]
    return np.mean(b7)
def fonk3(b1):
    b6 = np.mean(b1)
    b8 = [(elem - b6) ** 2 for elem in b1]
    return np.sum(b8) / (len(b1) - 1)
def fonk4(b15, b16, b1, b17, b18):
    plt.plot(b15, b16, b9 = 'sin(2Ïb15)')
    plt.grid(True)
    plt.ylim(-2, 2)
    plt.xlim(0, 1)
    b6 = np.mean(b1)
    b10 = [b6] * len(b15)
    for b5 in b1:
        plt.plot(b15, [b5] * len(b15), b11 = 0.5, color='g')
    plt.plot(b15, b10, b11 = 0.5, color='r', linewidth=2, b9='gÌ')
    plt.text(0.5, 1.75, f'b12 = {b17:.6f}')
    plt.text(0.5, 1.64, f'b13 = {b18:.6f}')
    plt.legend()
    plt.show()
if b14 = = "__main__":
    b15 = np.arange(0, 1, 0.01)
    b16 = np.sin(2 * np.pi * b15)
    b1 = fonk1(a1)
    b17 = fonk2(b1, b15)
    b18 = fonk3(b1)
    print(f'b12 = {b17:.6f}')
    print(f'b13 = {b18:.6f}')
    fonk4(b15, b16, b1, b17, b18)
import numpy as np
import random
import math
from matplotlib import pyplot as plt
a1 = 200
a2 = 0.01
def fonk1(experiments):
    b1 = []
    for _ in range(experiments):
        x1, b2 = random.uniform(0, 1.0), random.uniform(0, 1.0)
        y1, b3 = np.sin(2 * np.pi * x1), np.sin(2 * np.pi * b2)
        b4 = np.sqrt((b2 - x1) ** 2 + (b3 - y1) ** 2)
        b5 = max(y1, b3) - b4 / 2
        b1.append(b5)
    return b1
def fonk2(b1, b14):
    b6 = np.mean(b1)
    b7 = [(b6 - np.sin(2 * np.pi * elem)) ** 2 for elem in b14]
    return np.mean(b7)
def fonk3(b1):
    b6 = np.mean(b1)
    b8 = [(elem - b6) ** 2 for elem in b1]
    return np.sum(b8) / (len(b1) - 1)
def fonk4(b14, b15, b1, b16, b17):
    plt.plot(b14, b15, b9 = 'sin(2Ïb14)')
    plt.grid(True)
    plt.ylim(-2, 2)
    plt.xlim(0, 1)
    b6 = np.mean(b1)
    b10 = [b6] * len(b14)
    for b5 in b1:
        plt.plot(b14, [b5] * len(b14), b11 = 0.5, color='g')
    plt.plot(b14, b10, b11 = 0.5, color='r', linewidth=2, b9='gÌ')
    plt.text(0.5, 1.75, f'b12 = {b16:.6f}')
    plt.text(0.5, 1.64, f'b13 = {b17:.6f}')
    plt.legend()
    plt.show()
def fonk5():
    b14 = np.arange(0, 1, a2)
    b15 = np.sin(2 * np.pi * b14)
    b1 = fonk1(a1)
    b16 = fonk2(b1, b14)
    b17 = fonk3(b1)
    print(f'b12 = {b16:.6f}')
    print(f'b13 = {b17:.6f}')
    fonk4(b14, b15, b1, b16, b17)
if b18 = = "__main__":
    fonk5()
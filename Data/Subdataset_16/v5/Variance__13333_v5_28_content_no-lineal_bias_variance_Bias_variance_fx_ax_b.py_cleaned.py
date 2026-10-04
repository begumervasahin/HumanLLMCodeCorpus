import os
import random
import math
from numpy import arange, pi, sin
import matplotlib.pyplot as plt
a1 = 200
b1 = []
b2 = []
def fonk1(num_experiments):
    for _ in range(num_experiments):
        x1, b3 = random.uniform(-1, 1), random.uniform(-1, 1)
        y1, b4 = sin(x1 * pi), sin(b3 * pi)
        b5 = (b4 - y1) / (b3 - x1)
        b6 = y1 - b5 * x1
        b1.append(b5)
        b2.append(b6)
def fonk2(b16, b17, b14):
    b7 = [(b16 * x + b17 - sin(x * pi)) ** 2 for x in b14]
    return sum(b7) / len(b7)
def fonk3(b16, b17, b14):
    b8 = [
        [(b5 - b16) * x + (b6 - b17) for b5, b6 in zip(b1, b2)]
        for x in b14
    ]
    b9 = [[dev ** 2 for dev in devs] for devs in b8]
    b10 = [sum(devs) / (len(devs) - 1) for devs in b9]
    return sum(b10) / len(b10)
def fonk4(b14, b15, b16, b17, b18, b19):
    plt.plot(b14, b15, b11 = 'sin(t*pi)')
    plt.grid(True)
    plt.ylim(-2, 2)
    plt.xlim(-1, 1)
    for b5, b6 in zip(b1, b2):
        plt.plot(b14, b5 * b14 + b6, b12 = 0.5, color='g')
    plt.plot(b14, b16 * b14 + b17, b12 = 0.5, color='r', linewidth=2, b11='Mean Line')
    plt.text(-0.9, 1.75, f'b20: {b18:.6f}')
    plt.text(-0.9, 1.64, f'b21: {b19:.6f}')
    plt.legend()
    plt.savefig(os.path.join('Sinusoidal_dos.png'), b13 = 300, format='png', bbox_inches='tight')
    plt.show()
fonk1(a1)
b14 = arange(-1, 1.01, 0.01)
b15 = sin(b14 * pi)
b16 = sum(b1) / len(b1)
b17 = sum(b2) / len(b2)
b18 = fonk2(b16, b17, b14)
b19 = fonk3(b16, b17, b14)
print(f'b20 = {b18:.6f}')
print(f'b21 = {b19:.6f}')
fonk4(b14, b15, b16, b17, b18, b19)
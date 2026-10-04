import os
import random
import math
from numpy import arange, pi, sin
import matplotlib.pyplot as plt
a1 = 200
b1 = []
b2 = []
for _ in range(a1):
    x1, b3 = random.uniform(-1, 1), random.uniform(-1, 1)
    y1, b4 = sin(x1 * pi), sin(b3 * pi)
    b5 = (b4 - y1) / (b3 - x1)
    b6 = y1 - b5 * x1
    b1.append(b5)
    b2.append(b6)
b7 = arange(-1, 1.01, 0.01)
b8 = sin(b7 * pi)
b9 = sum(b1) / len(b1)
b10 = sum(b2) / len(b2)
b11 = [(b9 * x + b10 - sin(x * pi)) ** 2 for x in b7]
b12 = sum(b11) / len(b11)
print(f'b13 = {b12:.6f}')
b14 = [
    [(slope - b9) * x + (intercept - b10) for slope, intercept in zip(b1, b2)]
    for x in b7
]
b15 = [[dev ** 2 for dev in devs] for devs in b14]
b16 = [sum(devs) / (len(devs) - 1) for devs in b15]
b17 = sum(b16) / len(b16)
print(f'b18 = {b17:.6f}')
plt.plot(b7, b8, b19 = 'sin(b7*pi)')
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(-1, 1)
for slope, intercept in zip(b1, b2):
    plt.plot(b7, slope * b7 + intercept, b20 = 0.5, color='g')
plt.plot(b7, b9 * b7 + b10, b20 = 0.5, color='r', linewidth=2, b19='Mean Line')
plt.text(-0.9, 1.75, f'b13: {b12:.6f}')
plt.text(-0.9, 1.64, f'b18: {b17:.6f}')
plt.legend()
plt.savefig(os.path.join('Sinusoidal_dos.png'), b21 = 300, format='png', bbox_inches='tight')
plt.show()
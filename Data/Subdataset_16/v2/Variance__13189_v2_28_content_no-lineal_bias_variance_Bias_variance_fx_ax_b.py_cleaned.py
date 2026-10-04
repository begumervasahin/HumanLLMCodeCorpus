import matplotlib.pyplot as plt
import numpy as np
import random
import math
import os
a1 = 200
b1 = np.arange(-1, 1.01, 0.01)
b2 = np.sin(b1 * np.pi)
b3 = []
b4 = []
for _ in range(a1):
    b5 = random.uniform(-1, 1)
    b6 = random.uniform(-1, 1)
    b7 = np.sin(b5 * np.pi)
    b8 = np.sin(b6 * np.pi)
    b9 = (b8 - b7) / (b6 - b5)
    b10 = b7 - (b9 * b5)
    b3.append(b9)
    b4.append(b10)
b11 = np.mean(b3)
b12 = np.mean(b4)
b13 = [(b11 * x + b12 - np.sin(x * np.pi)) ** 2 for x in b1]
b14 = np.mean(b13)
print(f'b15 = {b14:.6f}')
b16 = [
    [(b3[j] - b11) * x + (b4[j] - b12) for j in range(a1)] for x in b1
]
b17 = [[val ** 2 for val in deviation] for deviation in b16]
b18 = np.mean([np.mean(vs) / (len(vs) - 1) for vs in b17])
print(f'Variance: {b18:.6f}')
plt.plot(b1, b2, b19 = 'sin(b1*pi)')
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(-1, 1)
for i in range(a1):
    plt.plot(b1, b3[i] * b1 + b4[i], b20 = 0.5, color='g')
plt.plot(b1, b11 * b1 + b12, b20 = 0.5, color='r', linewidth=2, b19='Average Line')
plt.text(-0.9, 1.75, f'b15: {b14:.6f}')
plt.text(-0.9, 1.64, f'Variance: {b18:.6f}')
plt.legend()
plt.savefig('Sinusoidal_dos.png', b21 = 300, format='png', bbox_inches='tight')
plt.show()
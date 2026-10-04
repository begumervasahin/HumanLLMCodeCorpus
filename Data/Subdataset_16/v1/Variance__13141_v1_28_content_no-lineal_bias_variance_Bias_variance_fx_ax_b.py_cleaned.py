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
for i in range(a1):
    b5 = random.uniform(-1, 1)
    b6 = random.uniform(-1, 1)
    b7 = np.sin(b5 * np.pi)
    b8 = np.sin(b6 * np.pi)
    b9 = (b8 - b7) / (b6 - b5)
    b10 = b7 - (b9 * b5)
    b3.append(b9)
    b4.append(b10)
b11 = sum(b3) / len(b3)
b12 = sum(b4) / len(b4)
b13 = [(b11 * elemento + b12 - np.sin(elemento * np.pi)) ** 2 for elemento in b1]
b14 = sum(b13) / len(b13)
print('b15 = %f' % b14)
b16 = [[((b3[j] - b11) * b1[i]) + (b4[j] - b12) for j in range(a1)] for i in range(len(b1))]
b17 = [[math.pow(recta, 2) for recta in punto] for punto in b16]
b18 = [sum(punto) / (len(punto) - 1) for punto in b17]
b19 = sum(b18) / len(b18)
print('Variance: %f' % b19)
plt.plot(b1, b2, b20 = 'sin(b1*pi)')
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(-1, 1)
for i in range(a1):
    plt.plot(b1, (b3[i] * b1) + b4[i], b21 = 0.5, color='g')
plt.plot(b1, (b11 * b1) + b12, b21 = 0.5, color='r', linewidth=2, b20='Average Line')
plt.text(-0.9, 1.75, 'b15: ' + str(b14))
plt.text(-0.9, 1.64, 'Variance: ' + str(b19))
plt.legend()
plt.savefig(os.path.join('Sinusoidal_dos.png'), b22 = 300, format='png', bbox_inches='tight')
plt.show()
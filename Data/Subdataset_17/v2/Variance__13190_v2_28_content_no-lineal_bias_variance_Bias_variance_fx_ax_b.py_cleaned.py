import matplotlib.pyplot as plt
import numpy as np
import random
import math
import os
experiments = 200
t = np.arange(-1, 1.01, 0.01)
ft = np.sin(t * np.pi)
pendiente = []
interseccion = []
for _ in range(experiments):
    x1 = random.uniform(-1, 1)
    x2 = random.uniform(-1, 1)
    y1 = np.sin(x1 * np.pi)
    y2 = np.sin(x2 * np.pi)
    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m * x1)
    pendiente.append(m)
    interseccion.append(b)
avg_slope = np.mean(pendiente)
avg_intercept = np.mean(interseccion)
bias_list = [(avg_slope * x + avg_intercept - np.sin(x * np.pi)) ** 2 for x in t]
bias = np.mean(bias_list)
print(f'Bias = {bias:.6f}')
deviation_squares = [
    [(pendiente[j] - avg_slope) * x + (interseccion[j] - avg_intercept) for j in range(experiments)] for x in t
]
variance_squares = [[val ** 2 for val in deviation] for deviation in deviation_squares]
variance = np.mean([np.mean(vs) / (len(vs) - 1) for vs in variance_squares])
print(f'Variance: {variance:.6f}')
plt.plot(t, ft, label='sin(t*pi)')
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(-1, 1)
for i in range(experiments):
    plt.plot(t, pendiente[i] * t + interseccion[i], alpha=0.5, color='g')
plt.plot(t, avg_slope * t + avg_intercept, alpha=0.5, color='r', linewidth=2, label='Average Line')
plt.text(-0.9, 1.75, f'Bias: {bias:.6f}')
plt.text(-0.9, 1.64, f'Variance: {variance:.6f}')
plt.legend()
plt.savefig('Sinusoidal_dos.png', dpi=300, format='png', bbox_inches='tight')
plt.show()
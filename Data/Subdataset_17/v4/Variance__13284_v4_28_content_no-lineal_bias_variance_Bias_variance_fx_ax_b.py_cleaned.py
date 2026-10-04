import os
import random
import math
from numpy import arange, pi, sin
import matplotlib.pyplot as plt
EXPERIMENTS = 200
slopes = []
intercepts = []
for _ in range(EXPERIMENTS):
    x1, x2 = random.uniform(-1, 1), random.uniform(-1, 1)
    y1, y2 = sin(x1 * pi), sin(x2 * pi)
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    slopes.append(m)
    intercepts.append(b)
t = arange(-1, 1.01, 0.01)
ft = sin(t * pi)
mean_slope = sum(slopes) / len(slopes)
mean_intercept = sum(intercepts) / len(intercepts)
bias_list = [(mean_slope * x + mean_intercept - sin(x * pi)) ** 2 for x in t]
bias = sum(bias_list) / len(bias_list)
print(f'Bias = {bias:.6f}')
deviations = [
    [(slope - mean_slope) * x + (intercept - mean_intercept) for slope, intercept in zip(slopes, intercepts)]
    for x in t
]
squared_deviations = [[dev ** 2 for dev in devs] for devs in deviations]
variance_list = [sum(devs) / (len(devs) - 1) for devs in squared_deviations]
variance = sum(variance_list) / len(variance_list)
print(f'Variance = {variance:.6f}')
plt.plot(t, ft, label='sin(t*pi)')
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(-1, 1)
for slope, intercept in zip(slopes, intercepts):
    plt.plot(t, slope * t + intercept, alpha=0.5, color='g')
plt.plot(t, mean_slope * t + mean_intercept, alpha=0.5, color='r', linewidth=2, label='Mean Line')
plt.text(-0.9, 1.75, f'Bias: {bias:.6f}')
plt.text(-0.9, 1.64, f'Variance: {variance:.6f}')
plt.legend()
plt.savefig(os.path.join('Sinusoidal_dos.png'), dpi=300, format='png', bbox_inches='tight')
plt.show()
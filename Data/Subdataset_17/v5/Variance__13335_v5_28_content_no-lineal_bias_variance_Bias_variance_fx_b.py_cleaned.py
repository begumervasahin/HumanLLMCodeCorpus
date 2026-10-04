from matplotlib import pyplot as plt
from numpy import arange, pi, sin
import random
import math
EXPERIMENTS = 200
def perform_experiment():
    x1 = random.uniform(0, 1.0)
    x2 = random.uniform(0, 1.0)
    y1 = sin(2 * x1 * pi)
    y2 = sin(2 * x2 * pi)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = max(y1, y2) - distance / 2
    return b
b_list = [perform_experiment() for _ in range(EXPERIMENTS)]
t = arange(0, 1, 0.01)
ft = sin(2 * t * pi)
imprimir = [[b] * len(t) for b in b_list]
mean_b = sum(b_list) / len(b_list)
g_bar_imp = [mean_b] * len(t)
bias_values = [(mean_b - sin(2 * ti * pi)) ** 2 for ti in t]
pro_bias = sum(bias_values) / len(bias_values)
print('Bias = %f' % pro_bias)
variance = sum((b - mean_b) ** 2 for b in b_list) / (len(b_list) - 1)
print('Variance = %f' % variance)
plt.plot(t, ft, label='sin(2Ït)')
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(0, 1)
for element in imprimir:
    plt.plot(t, element, alpha=0.5, color='g')
plt.plot(t, g_bar_imp, alpha=0.5, color='r', linewidth=2, label='Mean b')
plt.text(0.5, 1.75, 'Bias = ' + str(pro_bias))
plt.text(0.5, 1.64, 'Variance = ' + str(variance))
plt.legend()
plt.show()
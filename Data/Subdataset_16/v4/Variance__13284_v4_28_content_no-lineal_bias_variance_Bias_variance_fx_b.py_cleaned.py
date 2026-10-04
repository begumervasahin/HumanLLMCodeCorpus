from matplotlib import pyplot as plt
from numpy import arange, pi, sin
import random
import math
a1 = 200
b1 = []
for i in range(a1):
    b2 = random.uniform(0, 1.0)
    b3 = random.uniform(0, 1.0)
    b4 = sin(2 * b2 * pi)
    b5 = sin(2 * b3 * pi)
    b6 = math.sqrt((b3 - b2) ** 2 + (b5 - b4) ** 2)
    b7 = max(b4, b5) - b6 / 2
    b1.append(b7)
b8 = arange(0, 1, 0.01)
b9 = sin(2 * b8 * pi)
b10 = [[number] * len(b8) for number in b1]
b11 = sum(b1) / len(b1)
b12 = [b11] * len(b8)
b13 = [(b11 - sin(2 * element * pi)) ** 2 for element in b8]
b14 = sum(b13) / len(b13)
print('b15 = %f' % b14)
b16 = sum((x - b11) ** 2 for x in b1) / (len(b1) - 1)
print('b17 = %f' % b16)
plt.plot(b8, b9, b18 = 'sin(2Ïb8)')
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(0, 1)
for element in b10:
    plt.plot(b8, element, b19 = 0.5, color='g')
plt.plot(b8, b12, b19 = 0.5, color='r', linewidth=2, b18='Mean b7')
plt.text(0.5, 1.75, 'b15 = ' + str(b14))
plt.text(0.5, 1.64, 'b17 = ' + str(b16))
plt.legend()
plt.show()
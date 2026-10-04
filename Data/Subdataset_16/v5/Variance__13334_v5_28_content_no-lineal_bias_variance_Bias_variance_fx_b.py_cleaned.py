from matplotlib import pyplot as plt
from numpy import arange, pi, sin
import random
import math
a1 = 200
def fonk1():
    b1 = random.uniform(0, 1.0)
    b2 = random.uniform(0, 1.0)
    b3 = sin(2 * b1 * pi)
    b4 = sin(2 * b2 * pi)
    b5 = math.sqrt((b2 - b1) ** 2 + (b4 - b3) ** 2)
    b6 = max(b3, b4) - b5 / 2
    return b6
b7 = [fonk1() for _ in range(a1)]
b8 = arange(0, 1, 0.01)
b9 = sin(2 * b8 * pi)
b10 = [[b6] * len(b8) for b6 in b7]
b11 = sum(b7) / len(b7)
b12 = [b11] * len(b8)
b13 = [(b11 - sin(2 * ti * pi)) ** 2 for ti in b8]
b14 = sum(b13) / len(b13)
print('b15 = %f' % b14)
b16 = sum((b6 - b11) ** 2 for b6 in b7) / (len(b7) - 1)
print('b17 = %f' % b16)
plt.plot(b8, b9, b18 = 'sin(2Ïb8)')
plt.grid(True)
plt.ylim(-2, 2)
plt.xlim(0, 1)
for element in b10:
    plt.plot(b8, element, b19 = 0.5, color='g')
plt.plot(b8, b12, b19 = 0.5, color='r', linewidth=2, b18='Mean b6')
plt.text(0.5, 1.75, 'b15 = ' + str(b14))
plt.text(0.5, 1.64, 'b17 = ' + str(b16))
plt.legend()
plt.show()
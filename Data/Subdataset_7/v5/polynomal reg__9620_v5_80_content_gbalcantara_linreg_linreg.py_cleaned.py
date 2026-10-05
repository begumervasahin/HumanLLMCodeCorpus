import numpy as np
import matplotlib.pyplot as plt
import sys
def fonk1(b11, b12, b7, a2, m, a1):
    b1 = b11.transpose()
    b2 = None
    while True:
        b3 = np.dot(b11, b7)
        b4 = b3 - b12
        b5 = np.sum(b4 ** 2) / (2 * m)
        if b2 is not None and round(b5, 2) == b2:
            break
        b2 = round(b5, 2)
        b6 = np.dot(b1, b4) / m
        b7 = b7 - a2 * b6
        a2 += 0.00001
    return b7, a2
b8 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
b9 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
b10 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
b11 = np.array([[1, num, num ** 2] for num in range(-10, 10)])
b12 = np.array([(b8 * num ** 2) + (b9 * num) + b10 for num in range(-10, 10)])
b13 = np.random.uniform(-0.1, 0.1, b12.shape)
b12 = b12 + b13
m, b14 = b11.shape
a1 = 5000
a2 = 0.000001
b7 = np.ones(b14)
b7, a2 = fonk1(b11, b12, b7, a2, m, a1)
print('Learning b15 = ', a2)
print('b16 = ', b7[2])
print('b17 = ', b7[1])
print('b18 = ', b7[0])
b19 = np.linspace(-10, 10, 20)
b20 = (b7[2] * b19 ** 2) + (b7[1] * b19) + b7[0]
plt.plot(b11[:, 1], b12, 'kx', b19, b20)
plt.show()
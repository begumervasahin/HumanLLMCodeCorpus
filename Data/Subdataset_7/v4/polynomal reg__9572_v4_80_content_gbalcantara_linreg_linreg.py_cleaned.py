import numpy as np
import matplotlib.pyplot as plt
import sys
def fonk1(b14, b15, b7, a2, m, a1):
    b1 = b14.transpose()
    b2 = None
    while True:
        b3 = np.dot(b14, b7)
        b4 = b3 - b15
        b5 = np.sum(b4 ** 2) / (2 * m)
        if b2 is not None and round(b5, 2) == b2:
            break
        b2 = round(b5, 2)
        b6 = np.dot(b1, b4) / m
        b7 = b7 - a2 * b6
        a2 += 0.00001
    return b7, a2
b8 = sys.argv[1] if len(sys.argv) > 1 else "0"
b9 = sys.argv[2] if len(sys.argv) > 2 else "0"
b10 = sys.argv[3] if len(sys.argv) > 3 else "0"
b11 = int(b8)
b12 = int(b9)
b13 = int(b10)
b14 = np.zeros(shape=(20, 3))
b15 = np.zeros(shape=20)
for i, num in enumerate(range(-10, 10)):
    b14[i][0] = 1
    b14[i][1] = num
    b14[i][2] = num ** 2
    b15[i] = ((b11) * num ** 2) + ((b12) * num) + b13
b16 = np.random.uniform(-0.1, 0.1, b15.shape)
b15 = b15 + b16
m, b17 = np.shape(b14)
a1 = 5000
a2 = 0.000001
b7 = np.ones(b17)
b7, a2 = fonk1(b14, b15, b7, a2, m, a1)
print('Learning b18 = ', a2)
print('b11 = ', b7[2])
print('b12 = ', b7[1])
print('b13 = ', b7[0])
b19 = np.linspace(-10, 10, 20)
b20 = ((b7[2]) * b19 ** 2) + ((b7[1]) * b19) + b7[0]
plt.plot(b14[:, 1], b15, 'kx', b19, b20)
plt.show()
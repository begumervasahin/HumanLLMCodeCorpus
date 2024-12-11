import numpy as np
import matplotlib.pyplot as plt
import sys
def fonk1(b14, b15, b6, a3, m, a2):
    b1 = b14.transpose()
    a1 = 1
    while a1 != 0:
        for i in range(0, a2):
            b2 = np.dot(b14, b6)
            b3 = b2 - b15
            b4 = np.sum(b3 ** 2) / (2 * m)
            b5 = np.dot(b1, b3) / m
            b6 = b6 - a3 * b5
            a1 = round(b4, 2)
        a3 += 0.00001
    return b6, a3
if b7 = = "__main__":
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
    m, b16 = np.shape(b14)
    a2 = 5000
    a3 = 0.000001
    b6 = np.ones(b16)
    b17 = np.random.uniform(-0.1, 0.1, b15.shape)
    b15 = b15 + b17
    b6, a3 = fonk1(b14, b15, b6, a3, m, a2)
    print('learning b18 = ', a3)
    print('b11 = ', b6[2])
    print('b12 = ', b6[1])
    print('b13 = ', b6[0])
    b19 = np.linspace(-10, 10, 20)
    b20 = b6[2] * b19 ** 2 + b6[1] * b19 + b6[0]
    plt.plot(b14[:, 1], b15, 'kx', b19, b20)
    plt.show()
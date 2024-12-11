import numpy as np
import matplotlib.pyplot as plt
import sys
def fonk1(b10, b11, b13, a3, num_samples, a2):
    b1 = b10.transpose()
    a1 = 1
    while a1 != 0:
        for _ in range(a2):
            b2 = np.dot(b10, b13)
            b3 = b2 - b11
            b4 = np.sum(b3 ** 2) / (2 * num_samples)
            b5 = np.dot(b1, b3) / num_samples
            b13 -= a3 * b5
            a1 = round(b4, 2)
        a3 += 0.00001
    return b13, a3
if b6 = = "__main__":
    b7 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    b8 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    b9 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    b10 = np.array([[1, num, num ** 2] for num in range(-10, 10)])
    b11 = np.array([((b7) * num ** 2) + ((b8) * num) + b9 for num in range(-10, 10)])
    num_samples, b12 = np.shape(b10)
    a2 = 5000
    a3 = 0.000001
    b13 = np.ones(b12)
    b14 = np.random.uniform(-0.1, 0.1, b11.shape)
    b11 += b14
    b13, a3 = fonk1(b10, b11, b13, a3, num_samples, a2)
    print('Learning b15 = ', a3)
    print('b7 = ', b13[2])
    print('b8 = ', b13[1])
    print('b9 = ', b13[0])
    b16 = np.linspace(-10, 10, 20)
    b17 = b13[2] * b16 ** 2 + b13[1] * b16 + b13[0]
    plt.plot(b10[:, 1], b11, 'kx', b16, b17)
    plt.show()
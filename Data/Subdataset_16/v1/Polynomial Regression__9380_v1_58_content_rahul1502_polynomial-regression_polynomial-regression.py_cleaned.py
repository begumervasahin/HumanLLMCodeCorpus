import numpy as np
import matplotlib.pyplot as plt
b1 = np.array([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]])
b2 = np.array([[1], [6], [63], [364], [1365], [3906], [9331], [19608], [37449], [66430], [111111], [177156], [271453], [402234], [579195], [813616], [1118481], [1508598], [2000719], [2613660], [3368421]])
def fonk1(b1, b11, degree, learning_rate, epochs):
    b3 = np.hstack([np.power(b1, b8) for b8 in range(1, degree + 1)])
    b4 = np.zeros((1, degree))
    b5 = len(b11)
    for b8 in range(epochs):
        b6 = b3 @ b4.T
        b7 = (1 / (2 * b5)) * np.sum(np.square(b6 - b11))
        if b8 = = 0:
            print(f'Initial b7: {b7}')
        elif b8 = = (epochs - 1):
            print(f'Final b7  : {b7}')
        b4 -= (1/b5) * learning_rate * np.sum((b6 - b11) * b3, b9 = 0)
    return b4, b3, b6
def fonk2(b1, b11, b6, title):
    plt.scatter(b1, b11, b10 = 'Actual')
    plt.plot(b1, b6, 'r', b10 = 'Predicted')
    plt.title(title)
    plt.xlabel('b1')
    plt.ylabel('b11')
    plt.legend()
    plt.show()
print('b11 = w1 * b1 + w2 * (b1 ^ 2)')
b4, b3, b6 = fonk1(b1, b2, degree=2, learning_rate=0.00005, epochs=10000)
fonk2(b3[:, 0], b2, b6, 'Training for b11 = w1 * b1 + w2 * (b1 ^ 2)')
print('---------------------------------------------')
print('b11 = w1 * b1 + w2 * (b1 ^ 2) + w3 * (b1 ^ 3)')
b4, b3, b6 = fonk1(b1, b2, degree=3, learning_rate=0.0000001, epochs=10000)
fonk2(b3[:, 0], b2, b6, 'Training for b11 = w1 * b1 + w2 * (b1 ^ 2) + w3 * (b1 ^ 3)')
print('---------------------------------------------')
print('b11 = w1 * b1 + w2 * (b1 ^ 2) + w3 * (b1 ^ 3) + w4 * (b1 ^ 4)')
b4, b3, b6 = fonk1(b1, b2, degree=4, learning_rate=0.0000000005, epochs=10000)
fonk2(b3[:, 0], b2, b6, 'Training for b11 = w1 * b1 + w2 * (b1 ^ 2) + w3 * (b1 ^ 3) + w4 * (b1 ^ 4)')
print('---------------------------------------------')
import numpy as np
import matplotlib.pyplot as plt
b1 = np.array([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]])
b2 = np.array([[1], [6], [63], [364], [1365], [3906], [9331], [19608], [37449], [66430], [111111], [177156], [271453], [402234], [579195], [813616], [1118481], [1508598], [2000719], [2613660], [3368421]])
def fonk1(b1, b12):
    return np.hstack([np.power(b1, i) for i in range(1, b12 + 1)])
def fonk2(b11, b2, b12, learning_rate, epochs):
    b3 = np.zeros((1, b12))
    b4 = len(b2)
    for b7 in range(epochs):
        b5 = b11 @ b3.T
        b6 = (1 / (2 * b4)) * np.sum(np.square(b5 - b2))
        if b7 = = 0:
            print(f'Initial b6: {b6}')
        elif b7 = = epochs - 1:
            print(f'Final b6  : {b6}')
        b3 -= (learning_rate / b4) * np.sum((b5 - b2) * b11, b8 = 0)
    return b3, b5
def fonk3(b1, b10, b5, title):
    plt.scatter(b1, b10, b9 = 'Actual')
    plt.plot(b1, b5, 'r', b9 = 'Predicted')
    plt.title(title)
    plt.xlabel('b1')
    plt.ylabel('b10')
    plt.legend()
    plt.show()
def fonk4(b1, b2, b12, learning_rate, epochs):
    print(f'Training for b12 {b12} polynomial regression')
    print(f'Equation: b10 = {" + ".join([f"w{i+1} * b1^{i+1}" for i in range(b12)])}')
    b11 = fonk1(b1, b12)
    b3, b5 = fonk2(b11, b2, b12, learning_rate, epochs)
    fonk3(b1, b2, b5, f'Training for b10 = {" + ".join([f"w{i+1} * b1^{i+1}" for i in range(b12)])}')
    print('---------------------------------------------')
fonk4(b1, b2, b12 = 2, learning_rate=0.00005, epochs=10000)
fonk4(b1, b2, b12 = 3, learning_rate=0.0000001, epochs=10000)
fonk4(b1, b2, b12 = 4, learning_rate=0.0000000005, epochs=10000)
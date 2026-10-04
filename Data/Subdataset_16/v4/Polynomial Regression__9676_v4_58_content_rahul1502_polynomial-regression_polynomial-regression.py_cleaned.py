import numpy as np
import matplotlib.pyplot as plt
b1 = np.array([[b9] for b9 in range(21)])
b2 = np.array([
    [1], [6], [63], [364], [1365], [3906], [9331], [19608], [37449], [66430],
    [111111], [177156], [271453], [402234], [579195], [813616], [1118481],
    [1508598], [2000719], [2613660], [3368421]
])
def fonk1(b1, b4, b12, learning_rate, epochs):
    b3 = b1
    for d in range(2, b12 + 1):
        b3 = np.append(b3, np.power(b1, d), b10=1)
    print(f'Training for b4 = {" + ".join([f"w{d} * (b1 ^ {d})" for d in range(1, b12 + 1)])}')
    print(f'Training with {len(b3)} tuples')
    b5 = len(b4)
    b6 = np.zeros((1, b12))
    for b9 in range(epochs):
        b7 = b3 @ b6.T
        b8 = (1 / b5) * np.sum(np.square(b7 - b4))
        if b9 = = 0:
            print(f'Initial b8: {b8}')
        elif b9 = = (epochs - 1):
            print(f'Final b8  : {b8}')
        b6 -= (1 / b5) * learning_rate * np.sum((b7 - b4) * b3, b10 = 0)
    plt.scatter(b1[:, 0], b4, b11 = 'Actual data')
    plt.plot(b1[:, 0], b7, 'r', b11 = 'Fitted line')
    plt.title(f'Training for polynomial b12 {b12}')
    plt.xlabel('b1')
    plt.ylabel('b4')
    plt.legend()
    plt.show()
fonk1(b1, b2, b12 = 2, learning_rate=0.00005, epochs=10000)
print('---------------------------------------------')
fonk1(b1, b2, b12 = 3, learning_rate=0.0000001, epochs=10000)
print('---------------------------------------------')
fonk1(b1, b2, b12 = 4, learning_rate=0.0000000005, epochs=10000)
print('---------------------------------------------')
import numpy as np
import matplotlib.pyplot as plt
b1 = np.array([[b9] for b9 in range(21)])
b2 = np.array([
    [1], [6], [63], [364], [1365], [3906], [9331], [19608], [37449], [66430],
    [111111], [177156], [271453], [402234], [579195], [813616], [1118481],
    [1508598], [2000719], [2613660], [3368421]
])
def fonk1(b1, b4, degree, learning_rate, a1):
    b3 = np.hstack([np.power(b1, d) for d in range(1, degree + 1)])
    print(f'Training for b4 = {" + ".join([f"w{d} * (b1 ^ {d})" for d in range(1, degree + 1)])}')
    print(f'Training with {len(b3)} tuples')
    b5 = len(b4)
    b6 = np.zeros((1, degree))
    for b9 in range(a1):
        b7 = b3 @ b6.T
        b8 = (1 / b5) * np.sum(np.square(b7 - b4))
        if b9 = = 0:
            print(f'Initial b8: {b8}')
        elif b9 = = (a1 - 1):
            print(f'Final b8  : {b8}')
        b6 -= (1 / b5) * learning_rate * np.sum((b7 - b4) * b3, b10 = 0)
    return b7, b6
def fonk2(b1, b4, b7, degree):
    plt.scatter(b1[:, 0], b4, b11 = 'Actual data')
    plt.plot(b1[:, 0], b7, 'r', b11 = 'Fitted line')
    plt.title(f'Training for polynomial degree {degree}')
    plt.xlabel('b1')
    plt.ylabel('b4')
    plt.legend()
    plt.show()
def fonk3():
    b12 = [2, 3, 4]
    b13 = [0.00005, 0.0000001, 0.0000000005]
    a1 = 10000
    for degree, lr in zip(b12, b13):
        b7, b6 = fonk1(b1, b2, degree, lr, a1)
        fonk2(b1, b2, b7, degree)
        print('---------------------------------------------')
if b14 = = "__main__":
    fonk3()
import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt('data/svar-set1.dat.txt')
b2 = np.loadtxt('data/svar-set2.dat.txt')
b3 = np.loadtxt('data/svar-set3.dat.txt')
b4 = np.loadtxt('data/svar-set4.dat.txt')
def fonk1(b7, b13):
    b5 = np.linalg.pinv(b7).dot(b13)
    return b5
def fonk2(b7, b13):
    b5 = fonk1(b7, b13)
    b6 = b7.dot(b5)
    return b6, b5
def fonk3(b5, xIn):
    b7 = np.ones(shape=(1, xIn.size + 1))
    b7[0, 1:] = xIn
    b8 = b7.dot(b5)
    return b8
def fonk4(x):
    m, b9 = x.shape
    b7 = np.ones(shape=(m, b9 + 1))
    b7[:, 1:] = x
    return b7
def fonk5(x, order):
    m, b9 = x.shape
    b7 = np.ones(shape=(m, b9 + order))
    for i in range(1, order + 1):
        b7[:, b9 + i - 1] = np.power(x[:, 0], i)
    return b7
def fonk6(b6, b13):
    b10 = np.array(b6 - b13).T.dot(b6 - b13) / b13.shape[0]
    return b10
def fonk7(x, b9):
    row, b11 = x.shape
    b12 = row
    b13 = np.ndarray(shape=(b9, b12, b11))
    for i in range(b9):
        b13[i] = x[i * b12: (i + 1) * b12, :]
    return b13
def fonk8(x, i):
    splits, row, b11 = x.shape
    b14 = np.ndarray(shape=((splits - 1) * row, b11))
    b15 = x[i]
    a1 = 0
    for b16 in range(splits):
        if b16 = = i:
            continue
        b14[a1 * row: (a1 + 1) * row] = x[b16]
        a1 += 1
    print(f"Training shape: {b14.shape}")
    print(f"Testing shape: {b15.shape}")
    return b14, b15
def fonk9(data):
    row, b11 = data.shape
    b17 = data[:, :b11 - 1]
    b13 = data[:, b11 - 1:]
    b17 = b17.reshape(-1, 1)
    b13 = b13.reshape(-1, 1)
    b18 = fonk4(b17)
    Y_fit, b5 = fonk2(b18, b13)
    b19 = fonk5(b17, 2)
    Y_fit_quad, b20 = fonk2(b19, b13)
    b21 = fonk5(b17, 3)
    Y_fit_third, b22 = fonk2(b21, b13)
    print("Average SSE for linear:", fonk6(Y_fit, b13),
          " Polynomial of degree 2:", fonk6(Y_fit_quad, b13),
          " Polynomial of degree 3:", fonk6(Y_fit_third, b13))
    plt.plot(b17, b13, 'r+', b23 = 'Data')
    plt.plot(b17, Y_fit, '.', b23 = 'Linear Fit')
    plt.plot(b17, Y_fit_quad, 'r.', b23 = 'Quadratic Fit')
    plt.plot(b17, Y_fit_third, 'g.', b23 = 'Cubic Fit')
    plt.legend()
    plt.show()
fonk9(b1)
fonk9(b2)
fonk9(b3)
fonk9(b4)
b17 = fonk7(b1, 10)
fonk8(b17, 1)
import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt('data/svar-set1.dat.txt')
b2 = np.loadtxt('data/svar-set2.dat.txt')
b3 = np.loadtxt('data/svar-set3.dat.txt')
b4 = np.loadtxt('data/svar-set4.dat.txt')
def fonk1(b7, b15):
    b5 = np.linalg.pinv(b7).dot(b15)
    return b5
def fonk2(b7, b15):
    b5 = fonk1(b7, b15)
    b6 = b7.dot(b5)
    return b6, b5
def fonk3(b5, xIn):
    b7 = np.ones(shape=(1, xIn.size + 1))
    b7[0, 1:] = xIn
    b8 = b7.dot(b5)
    return b8
def fonk4(x):
    m, b9 = x.shape
    b7 = np.ones(shape=(m, b9+1))
    b7[:, 1:] = x[:, :]
    return b7
def fonk5(x, order):
    m, b9 = x.shape
    b10 = b9 + order
    b7 = np.ones(shape=(m, b10))
    for i in range(1, order+1):
        b7[:, b9+i-1] = np.power(x[:, 0], i)
    return b7
def fonk6(b6, b15):
    m, b11 = b15.shape
    b12 = np.array(b6 - b15).transpose().dot((b6 - b15))
    b12 /= m
    return b12
def fonk7(x, b9):
    row, b13 = x.shape
    b14 = row
    b15 = np.ndarray(shape=(b9, b14, b13))
    for i in range(b9):
        b15[i, :, :] = x[i*b14: (i+1)*b14, :]
    return b15
def fonk8(x, i):
    splits, row, b13 = x.shape
    b16 = np.ndarray(shape=((splits-1) * row, b13))
    b17 = x[i, :, :]
    a1 = 0
    for b10 in range(splits):
        if b10 = = i:
            continue
        b16[a1*row: (a1+1)*row, :] = x[b10, :, :]
        a1 += 1
    print("b16:", b16.shape)
    print("b17:", b17.shape)
    return b16, b17
def fonk9(data):
    row, b13 = data.shape
    b18 = data[:, :b13-1]
    b15 = data[:, b13-1:]
    b18 = b18.reshape(-1, 1)
    b15 = b15.reshape(-1, 1)
    b19 = fonk4(b18)
    Y_fit, b5 = fonk2(b19, b15)
    b19 = fonk5(b18, 2)
    Y_fit_quad, b20 = fonk2(b19, b15)
    b19 = fonk5(b18, 3)
    Y_fit_third, b21 = fonk2(b19, b15)
    print("Average SSE for linear:", fonk6(Y_fit, b15),
          " Polynomial of degree 2:", fonk6(Y_fit_quad, b15),
          " Polynomial of degree 3:", fonk6(Y_fit_third, b15))
    plt.plot(b18, b15, 'r+', b22 = 'Data')
    plt.plot(b18, Y_fit, 'b.', b22 = 'Linear fit')
    plt.plot(b18, Y_fit_quad, 'r.', b22 = 'Quadratic fit')
    plt.plot(b18, Y_fit_third, 'g.', b22 = 'Cubic fit')
    plt.legend()
    plt.show()
fonk9(b1)
fonk9(b2)
fonk9(b3)
fonk9(b4)
b18 = fonk7(b1, 10)
fonk8(b18, 1)
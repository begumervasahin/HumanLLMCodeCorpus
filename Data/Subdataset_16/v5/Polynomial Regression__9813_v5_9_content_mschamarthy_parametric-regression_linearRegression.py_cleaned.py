import numpy as np
import matplotlib.pyplot as plt
b1 = [
    np.loadtxt('data/svar-set1.dat.txt'),
    np.loadtxt('data/svar-set2.dat.txt'),
    np.loadtxt('data/svar-set3.dat.txt'),
    np.loadtxt('data/svar-set4.dat.txt')
]
def fonk1(b4, b15):
    return np.linalg.pinv(b4).dot(b15)
def fonk2(b4, b15):
    b2 = fonk1(b4, b15)
    b3 = b4.dot(b2)
    return b3, b2
def fonk3(b2, xIn):
    b4 = np.ones((1, xIn.size + 1))
    b4[0, 1:] = xIn
    return b4.dot(b2)
def fonk4(x):
    b6, b5 = x.shape
    b4 = np.ones((b6, b5 + 1))
    b4[:, 1:] = x
    return b4
def fonk5(x, order):
    b6, b5 = x.shape
    b4 = np.ones((b6, b5 + order))
    for i in range(1, order + 1):
        b4[:, b5 + i - 1] = np.power(x[:, 0], i)
    return b4
def fonk6(b3, b15):
    b6 = b15.shape[0]
    b7 = np.dot((b3 - b15).T, (b3 - b15)) / b6
    return b7
def fonk7(x, b5):
    row, b8 = x.shape
    b9 = row
    b10 = np.ndarray((b5, b9, b8))
    for i in range(b5):
        b10[i, :, :] = x[i * b9: (i + 1) * b9, :]
    return b10
def fonk8(b10, exclude_index):
    splits_count, row, b8 = b10.shape
    b11 = np.ndarray(((splits_count - 1) * row, b8))
    b12 = b10[exclude_index, :, :]
    a1 = 0
    for b13 in range(splits_count):
        if b13 = = exclude_index:
            continue
        b11[a1 * row: (a1 + 1) * row, :] = b10[b13, :, :]
        a1 += 1
    print("training:", b11.shape)
    print("testing:", b12.shape)
    return b11, b12
def fonk9(data):
    row, b8 = data.shape
    b14 = data[:, :b8 - 1]
    b15 = data[:, b8 - 1:].reshape(-1, 1)
    b14 = b14.reshape(-1, 1)
    b16 = fonk4(b14)
    Y_fit_linear, b17 = fonk2(b16, b15)
    b18 = fonk5(b14, 2)
    Y_fit_quad, b19 = fonk2(b18, b15)
    b20 = fonk5(b14, 3)
    Y_fit_cubic, b21 = fonk2(b20, b15)
    print("Average SSE for linear:", fonk6(Y_fit_linear, b15),
          " Polynomial of degree 2:", fonk6(Y_fit_quad, b15),
          " Polynomial of degree 3:", fonk6(Y_fit_cubic, b15))
    plt.plot(b14, b15, 'r+', b22 = 'Data')
    plt.plot(b14, Y_fit_linear, 'b.', b22 = 'Linear fit')
    plt.plot(b14, Y_fit_quad, 'r.', b22 = 'Quadratic fit')
    plt.plot(b14, Y_fit_cubic, 'g.', b22 = 'Cubic fit')
    plt.legend()
    plt.show()
for dataset in b1:
    fonk9(dataset)
b23 = fonk7(b1[0], 10)
fonk8(b23, 1)
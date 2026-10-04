import numpy as np
import matplotlib.pyplot as plt
b1 = [np.loadtxt(f'data/svar-set{i}.dat.txt') for i in range(1, 5)]
def fonk1(b4, b12):
    return np.linalg.pinv(b4).dot(b12)
def fonk2(b4, b12):
    b2 = fonk1(b4, b12)
    b3 = b4.dot(b2)
    return b3, b2
def fonk3(b2, x_in):
    b4 = np.ones((1, x_in.size + 1))
    b4[0, 1:] = x_in
    return b4.dot(b2)
def fonk4(x, b5 = 1):
    m, b6 = x.shape
    b4 = np.ones((m, b6 + b5))
    for i in range(1, b5 + 1):
        b4[:, b6 + i - 1] = np.power(x[:, 0], i)
    return b4
def fonk5(b3, b12):
    return np.mean(np.square(b3 - b12))
def fonk6(x, n_splits):
    row, b7 = x.shape
    b8 = row
    return np.array([x[i * b8:(i + 1) * b8] for i in range(n_splits)])
def fonk7(b21, exclude_index):
    b9 = b21[exclude_index]
    b10 = np.vstack([b21[i] for i in range(len(b21)) if i != exclude_index])
    print(f"Training shape: {b10.shape}")
    print(f"Testing shape: {b9.shape}")
    return b10, b9
def fonk8(data):
    b11 = data[:, :-1]
    b12 = data[:, -1:].reshape(-1, 1)
    b13 = fonk4(b11, b5=1)
    y_fit_linear, b14 = fonk2(b13, b12)
    b15 = fonk4(b11, b5=2)
    y_fit_quad, b14 = fonk2(b15, b12)
    b16 = fonk4(b11, b5=3)
    y_fit_cubic, b14 = fonk2(b16, b12)
    b17 = fonk5(y_fit_linear, b12)
    b18 = fonk5(y_fit_quad, b12)
    b19 = fonk5(y_fit_cubic, b12)
    print(f"Average SSE for linear: {b17:.4f}, Polynomial of degree 2: {b18:.4f}, Polynomial of degree 3: {b19:.4f}")
    plt.plot(b11, b12, 'r+', b20 = 'Data')
    plt.plot(b11, y_fit_linear, '.', b20 = 'Linear Fit')
    plt.plot(b11, y_fit_quad, 'r.', b20 = 'Quadratic Fit')
    plt.plot(b11, y_fit_cubic, 'g.', b20 = 'Cubic Fit')
    plt.legend()
    plt.show()
for dataset in b1:
    fonk8(dataset)
b21 = fonk6(b1[0], 10)
fonk7(b21, 1)
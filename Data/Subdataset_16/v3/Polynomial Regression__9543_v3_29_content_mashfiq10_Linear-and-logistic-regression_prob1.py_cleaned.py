import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("crash.txt")
b2 = b1[1::2]
b3 = b1[0:-1:2]
b4 = b2[:, 0].reshape(-1, 1)
b5 = b2[:, 1].reshape(-1, 1)
b6 = b3[:, 0].reshape(-1, 1)
b7 = b3[:, 1].reshape(-1, 1)
a1 = 20
b8 = np.zeros(a1)
b9 = np.zeros(a1)
b10 = float('inf')
b11 = float('inf')
b12 = None
a2 = 0
b13 = None
a3 = 0
def fonk1(x, L):
    return np.hstack([x**i for i in range(L)])
for L in range(1, a1 + 1):
    b14 = fonk1(b4, L)
    b15 = np.linalg.solve(b14.T.dot(b14), b14.T.dot(b5))
    b16 = 0.5 * np.square(np.linalg.norm(b5 - b14.dot(b15)))
    b8[L-1] = np.sqrt(2. * b16 / len(b2))
    if b8[L-1] < b10:
        b10 = b8[L-1]
        a2 = L
        b12 = b15
    b17 = fonk1(b6, L)
    b18 = 0.5 * np.square(np.linalg.norm(b7 - b17.dot(b15)))
    b9[L-1] = np.sqrt(2. * b18 / len(b3))
    if b9[L-1] < b11:
        b11 = b9[L-1]
        a3 = L
        b13 = b15
print('Maximum likelihood RMS error between the actual b1 and the models prediction (for Training sets): \n', b8)
print('Maximum likelihood RMS error between the actual b1 and the models prediction (for Test sets): \n', b9)
plt.figure(b19 = (16, 12))
plt.plot(b8, '-o', b20 = 'none', b24='b', label='Training')
plt.plot(b9, '-o', b20 = 'none', b24='r', label='Test')
plt.suptitle('Maximum likelihood RMS error between the actual b1 and the models prediction', b21 = 24)
plt.legend(b21 = 22)
plt.xlabel("M", b21 = 22)
plt.ylabel("Erms", b21 = 22)
plt.show()
def fonk2(x, y, title, xlabel, ylabel, data_label, model_label, L, b15):
    b22 = fonk1(x, L)
    b23 = b22.dot(b15)
    plt.figure(b19 = (16, 12))
    plt.plot(x, y, 'o', b24 = 'b', label=data_label)
    plt.plot(x, b23, b24 = 'r', label=model_label)
    plt.suptitle(title, b21 = 24)
    plt.legend(b21 = 22)
    plt.xlabel(xlabel, b21 = 22)
    plt.ylabel(ylabel, b21 = 22)
    plt.show()
b25 = np.linspace(np.min(b4), np.max(b4), 100).reshape(-1, 1)
print('Lowest RMS L for b2 b1:', a2)
fonk2(b4, b5, 'Best fit on the b2 set', 'time', 'acceleration', 'Training b1', 'Lowest RMS model output', a2, b12)
b26 = np.linspace(np.min(b6), np.max(b6), 100).reshape(-1, 1)
print('Lowest RMS L for b3 b1:', a3)
fonk2(b6, b7, 'Best fit on the b3 set', 'time', 'acceleration', 'Test b1', 'Lowest RMS model output', a3, b13)
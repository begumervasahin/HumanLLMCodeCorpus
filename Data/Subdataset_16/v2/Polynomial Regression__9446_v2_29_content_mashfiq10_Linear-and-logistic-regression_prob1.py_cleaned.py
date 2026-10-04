import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("crash.txt")
b2 = b1[1::2]
b3 = b1[0:-1:2]
b4 = b2[:, 0].reshape(-1, 1)
b5 = b2[:, 1].reshape(-1, 1)
b6 = b3[:, 0].reshape(-1, 1)
b7 = b3[:, 1].reshape(-1, 1)
b8 = np.zeros(20)
b9 = np.zeros(20)
b10 = float('inf')
b11 = float('inf')
b12 = None
a1 = 0
b13 = None
a2 = 0
def fonk1(b22, L):
    return np.hstack([b22**i for i in range(L)])
for L in range(1, 21):
    b14 = fonk1(b4, L)
    b15 = np.linalg.solve(b14.T.dot(b14), b14.T.dot(b5))
    b16 = 0.5 * np.square(np.linalg.norm(b5 - b14.dot(b15)))
    b8[L-1] = np.sqrt(2. * b16 / len(b2))
    if b8[L-1] < b10:
        b10 = b8[L-1]
        a1 = L
        b12 = b15
    b17 = fonk1(b6, L)
    b18 = 0.5 * np.square(np.linalg.norm(b7 - b17.dot(b15)))
    b9[L-1] = np.sqrt(2. * b18 / len(b3))
    if b9[L-1] < b11:
        b11 = b9[L-1]
        a2 = L
        b13 = b15
print('Maximum likelihood RMS error between the actual b1 and the models prediction (for Training sets): \n')
print(b8)
print('Maximum likelihood RMS error between the actual b1 and the models prediction (for Test sets): \n')
print(b9)
plt.figure(b19 = (16, 12))
plt.plot(b8, '-o', b20 = 'none', b25='b', label='Training')
plt.plot(b9, '-o', b20 = 'none', b25='r', label='Test')
plt.suptitle('Maximum likelihood RMS error between the actual b1 and the models prediction', b21 = 24)
plt.legend(b21 = 22)
plt.xlabel("M ", b21 = 22)
plt.ylabel("Erms", b21 = 22)
plt.show()
b22 = np.linspace(np.min(b4), np.max(b4), 100).reshape(-1, 1)
b23 = fonk1(b22, a1)
b24 = b23.dot(b12)
print('Lowest RMS L for b2 b1:', a1)
plt.figure(b19 = (16, 12))
plt.plot(b4, b5, 'o', b25 = 'b', label='Training b1')
plt.plot(b22, b24, b25 = 'r', label='Lowest RMS model output')
plt.suptitle('Best fit on the b2 set', b21 = 24)
plt.legend(b21 = 22)
plt.xlabel("time", b21 = 22)
plt.ylabel("acceleration", b21 = 22)
plt.show()
b22 = np.linspace(np.min(b6), np.max(b6), 100).reshape(-1, 1)
b23 = fonk1(b22, a2)
b24 = b23.dot(b13)
print('Lowest RMS L for b3 b1:', a2)
plt.figure(b19 = (16, 12))
plt.plot(b6, b7, 'o', b25 = 'b', label='Test b1')
plt.plot(b22, b24, b25 = 'r', label='Lowest RMS model output')
plt.suptitle('Best fit on the b3 set', b21 = 24)
plt.legend(b21 = 22)
plt.xlabel("time", b21 = 22)
plt.ylabel("acceleration", b21 = 22)
plt.show()
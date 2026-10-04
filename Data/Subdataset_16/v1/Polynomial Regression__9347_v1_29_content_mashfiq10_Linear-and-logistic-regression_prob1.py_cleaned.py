import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("crash.txt")
b2 = b1[1::2]
b3 = b1[0:-1:2]
b4 = np.array(b2[:, 0]).reshape(len(b2), 1)
b5 = np.array(b2[:, 1]).reshape(len(b2), 1)
b6 = np.array(b3[:, 0]).reshape(len(b3), 1)
b7 = np.array(b3[:, 1]).reshape(len(b3), 1)
b8 = np.zeros(20)
b9 = np.zeros(20)
a1 = 1000.
b10 = None
a2 = 0
a3 = 1000.
b11 = None
a4 = 0
def fonk1(b20, L):
    return np.hstack([b20**i for i in range(L)])
for L in range(1, 21):
    b12 = fonk1(b4, L)
    b13 = np.linalg.solve(b12.T.dot(b12), b12.T.dot(b5))
    b14 = 0.5 * np.square(np.linalg.norm(b5 - b12.dot(b13)))
    b8[L-1] = np.sqrt(2. * b14 / len(b2))
    if b8[L-1] < a1:
        a1 = b8[L-1]
        a2 = L
        b10 = b13
    b15 = fonk1(b6, L)
    b16 = 0.5 * np.square(np.linalg.norm(b7 - b15.dot(b13)))
    b9[L-1] = np.sqrt(2. * b16 / len(b3))
    if b9[L-1] < a3:
        a3 = b9[L-1]
        a4 = L
        b11 = b13
print('Maximum likelihood RMS error between the actual b1 and the models prediction (for Training sets): \n')
print(b8)
print('Maximum likelihood RMS error between the actual b1 and the models prediction (for Test sets): \n')
print(b9)
plt.figure(b17 = (16, 12))
plt.plot(b8, '-o', b18 = 'none', b23='b', label='Training')
plt.plot(b9, '-o', b18 = 'none', b23='r', label='Test')
plt.suptitle('Maximum likelihood RMS error between the actual b1 and the models prediction', b19 = 24)
plt.legend(b19 = 22)
plt.xlabel("M ", b19 = 22)
plt.ylabel("Erms", b19 = 22)
plt.show()
b20 = np.linspace(start=np.min(b4), stop=np.max(b4), num=100).reshape(100, 1)
b21 = fonk1(b20, a2)
b22 = b21.dot(b10)
print('Lowest RMS L for b2 b1:', a2)
plt.figure(b17 = (16, 12))
plt.plot(b4, b5, 'o', b23 = 'b', label='Training b1')
plt.plot(b20, b22, b23 = 'r', label='Lowest RMS model output')
plt.suptitle('Best fit on the b2 set', b19 = 24)
plt.legend(b19 = 22)
plt.xlabel("time ", b19 = 22)
plt.ylabel("acceleration", b19 = 22)
plt.show()
b20 = np.linspace(start=np.min(b6), stop=np.max(b6), num=100).reshape(100, 1)
b21 = fonk1(b20, a4)
b22 = b21.dot(b11)
print('Lowest RMS L for b3 b1:', a4)
plt.figure(b17 = (16, 12))
plt.plot(b6, b7, 'o', b23 = 'b', label='Test b1')
plt.plot(b20, b22, b23 = 'r', label='Lowest RMS model output')
plt.suptitle('Best fit on the b3 set', b19 = 24)
plt.legend(b19 = 22)
plt.xlabel("time ", b19 = 22)
plt.ylabel("acceleration", b19 = 22)
plt.show()
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
a1 = 1000.0
a2 = 0
a3 = 0
a4 = 1000.0
a5 = 0
a6 = 0
for L in range(1, 21):
    b10 = b4 ** np.arange(L).reshape(1, -1)
    b11 = np.linalg.solve(b10.T.dot(b10), b10.T.dot(b5))
    b12 = 0.5 * np.square(np.linalg.norm(b5 - b10.dot(b11)))
    b8[L-1] = np.sqrt(2.0 * b12 / len(b2))
    if b8[L-1] < a1:
        a1 = b8[L-1]
        a3 = L
        a2 = b11
    b13 = b6 ** np.arange(L).reshape(1, -1)
    b14 = 0.5 * np.square(np.linalg.norm(b7 - b13.dot(b11)))
    b9[L-1] = np.sqrt(2.0 * b14 / len(b3))
    if b9[L-1] < a4:
        a4 = b9[L-1]
        a6 = L
        a5 = b11
print('Maximum likelihood RMS error between the actual b1 and the model\'s prediction (for Training sets): \n', b8)
print('Maximum likelihood RMS error between the actual b1 and the model\'s prediction (for Test sets): \n', b9)
plt.figure(b15 = (16, 12))
plt.plot(b8, '-o', b16 = 'none', color='b', b21='Training')
plt.plot(b9, '-o', b16 = 'none', color='r', b21='Test')
plt.suptitle('Maximum likelihood RMS error between the actual b1 and the model\'s prediction', b17 = 24)
plt.legend(b17 = 22)
plt.xlabel("M", b17 = 22)
plt.ylabel("Erms", b17 = 22)
plt.show()
b18 = np.linspace(np.min(b4), np.max(b4), 100).reshape(100, 1)
b19 = b18 ** np.arange(a3).reshape(1, -1)
b20 = b19.dot(a2)
print('Lowest RMS L for b2 b1:', a3)
plt.figure(b15 = (16, 12))
plt.plot(b4, b5, 'bo', b21 = 'Training b1')
plt.plot(b18, b20, 'r-', b21 = 'Lowest RMS model output')
plt.suptitle('Best fit on the b2 set', b17 = 24)
plt.legend(b17 = 22)
plt.xlabel("time", b17 = 22)
plt.ylabel("acceleration", b17 = 22)
plt.show()
b18 = np.linspace(np.min(b6), np.max(b6), 100).reshape(100, 1)
b19 = b18 ** np.arange(a6).reshape(1, -1)
b20 = b19.dot(a5)
print('Lowest RMS L for b3 b1:', a6)
plt.figure(b15 = (16, 12))
plt.plot(b6, b7, 'bo', b21 = 'Test b1')
plt.plot(b18, b20, 'r-', b21 = 'Lowest RMS model output')
plt.suptitle('Best fit on the b3 set', b17 = 24)
plt.legend(b17 = 22)
plt.xlabel("time", b17 = 22)
plt.ylabel("acceleration", b17 = 22)
plt.show()
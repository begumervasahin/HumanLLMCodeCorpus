import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("crash.txt")
b2 = b1[1::2]
b3 = b1[0:-1:2]
b4 = np.array(b2[:, 0]).reshape(len(b2), 1)
b5 = np.array(b2[:, 1]).reshape(len(b2), 1)
b6 = np.array(b3[:, 0]).reshape(len(b2), 1)
b7 = np.array(b3[:, 1]).reshape(len(b2), 1)
b8 = np.zeros(20)
b9 = np.zeros(20)
a1 = 1000.
a2 = 0
a3 = 0
a4 = 1000.
a5 = 0
a6 = 0
for L in range(1,21):
    b10 = b4**range(L)
    b11 = np.linalg.solve(b10.T.dot(b10), b10.T.dot(b5))
    b12 = 0.5 * np.square(np.linalg.norm(b5 - b10.dot(b11)))
    b8[L-1] = np.sqrt(2. * b12 / len(b2))
    if b8[L-1] < a1:
        a1 = b8[L-1]
        a3 = L
        a2 = b11
    b10 = b6**range(L)
    b13 = 0.5 * np.square(np.linalg.norm(b7 - b10.dot(b11)))
    b9[L-1] = np.sqrt(2. * b13 / len(b2))
    if b9[L-1] < a4:
        a4 = b9[L-1]
        a6 = L
        a5 = b11
print('Maximum likelihood RMS error between the actual b1 and the models prediction (for Training sets): \n')
print(b8)
print('Maximum likelihood RMS error between the actual b1 and the models prediction (for Test sets): \n')
print(b9)
plt.figure(b14 = (16,12))
plt.plot(b8, '-o', b15 = 'none', b19='b', label='Training')
plt.plot(b9, '-o', b15 = 'none', b19='r', label='Test')
plt.suptitle('Maximum likelihood RMS error between the actual b1 and the models prediction', b16 = 24)
plt.legend(b16 = 22)
plt.xlabel("M ", b16 = 22)
plt.ylabel("Erms", b16 = 22)
plt.show()
b17 = np.linspace(start=np.min(b4), stop= np.max(b4), num=100).reshape(100, 1)
b10 = b17**range(a3)
b18 = b10.dot(a2)
print('Lowest RMS L for b2 b1:', a3)
plt.figure(b14 = (16,12))
plt.plot(b4, b5, b19 = 'b', label='Training b1')
plt.plot(b17, b18, b19 = 'r', label='Lowest RMS model output')
plt.suptitle('Best fit on the b2 set', b16 = 24)
plt.legend(b16 = 22)
plt.xlabel("time ", b16 = 22)
plt.ylabel("acceleration", b16 = 22)
plt.show()
b17 = np.linspace(start=np.min(b6), stop=np.max(b6), num=100).reshape(100, 1)
b10 = b17**range(a6)
b18 = b10.dot(a5)
print('Lowest RMS L for b3 b1:', a6)
plt.figure(b14 = (16,12))
plt.plot(b6, b7, b19 = 'b', label='Test b1')
plt.plot(b17, b18, b19 = 'r', label='Lowest RMS model output')
plt.suptitle('Best fit on the b3 set', b16 = 24)
plt.legend(b16 = 22)
plt.xlabel("time ", b16 = 22)
plt.ylabel("acceleration", b16 = 22)
plt.show()
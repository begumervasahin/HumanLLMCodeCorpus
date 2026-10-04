import numpy as np
from scipy.optimize import minimize
def fonk1(b19):
    b1 = {b'Iris-setosa': 0., b'Iris-versicolor': 1., b'Iris-virginica': 2.}
    return b1[b19]
def fonk2(b6, i):
    b2 = np.ones(5)
    b2[1:5] = b6[i, 1:5]
    return b2
def fonk3(w, b9, b10, b14):
    b3 = b9.shape[0]
    a1 = 3
    a2 = 0.
    for n in range(b3):
        a3 = 0.
        a4 = 0.
        for k in range(a1):
            a3 += b10[n, k] * w[5 * k:5 * k + 5].T.dot(fonk2(b9, n))
        for l in range(a1):
            a4 += np.exp(w[5 * l:5 * l + 5].T.dot(fonk2(b9, n)))
        a2 += a3
        a2 -= np.log(a4)
        if a2 = = -np.inf:
            a2 = 0.
    return b14 - a2
b4 = np.loadtxt('iris.txt', delimiter=',', converters={4: flower_to_float})
b5 = b4.shape[0]
a1 = 3
b6 = np.array(b4[:, :4])
b6 = np.concatenate((np.ones((b5, 1)), b6), axis=1)
b7 = np.zeros((b5, a1))
for i in range(b5):
    b7[i, int(b4[i, 4])] = 1
b8 = np.arange(b5)
np.random.shuffle(b8)
b6 = b6[b8]
b7 = b7[b8]
b9 = b6[:int(b5 / 2)]
b10 = b7[:int(b5 / 2)]
b11 = b6[int(b5 / 2):]
b12 = b7[int(b5 / 2):]
a5 = 0.0031257
b13 = np.ones(15)
b14 = (a5 / 2.) * b13.T.dot(b13)
b15 = minimize(f, b13, args=(b9, b10, b14)).b6
b16 = []
b17 = []
for i in range(b11.shape[0]):
    b18 = np.zeros(a1)
    for k in range(a1):
        b18[k] = np.exp(b15[5 * k:5 * k + 5].T.dot(fonk2(b11, i)))
        if b18[k] == np.inf:
            b18[k] = 1000.
    b19 = b18 / np.sum(b18)
    b16.append(np.argmax(b19))
for i in range(b12.shape[0]):
    b17.append(np.argmax(b12[i, :]))
b20 = np.mean(np.equal(b16, b17)) * 100.
print("Overall classification b20 = ", b20, '%')
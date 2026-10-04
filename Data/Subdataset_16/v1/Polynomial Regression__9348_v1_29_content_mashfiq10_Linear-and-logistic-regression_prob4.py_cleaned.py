import numpy as np
from scipy.optimize import minimize
def fonk1(b19):
    b1 = {b16'Iris-setosa': 0., b16'Iris-versicolor': 1., b16'Iris-virginica': 2.}
    return b1[b19]
def fonk2(_x, _i):
    b2 = np.ones(5)
    b2[1:5] = _x[_i, 1:5]
    return b2
def fonk3(_w, b9, b10, b14):
    b3 = b9.shape[0]
    a1 = 3
    a2 = 0.
    for n in range(b3):
        a3 = 0.
        a4 = 0.
        for b21 in range(a1):
            a3 += b10[n, b21] * _w[5*b21:(5*b21)+5].T.dot(fonk2(b9, n))
        for l in range(a1):
            a4 += np.exp(_w[5*l:(5*l)+5].T.dot(fonk2(b9, n)))
        a2 += a3
        a2 -= np.log(a4)
        if a2 = = -np.inf:
            a2 = 0.
    return b14 - a2
b4 = np.loadtxt('iris.txt', delimiter=',', converters={4: flower_to_float})
b5 = b4.shape[0]
a1 = 3
b6 = np.array(b4[:, :4])
b6 = np.concatenate((np.ones(shape=(b5, 1)), b6), axis=1)
b7 = np.zeros(shape=(b5, a1))
for i in range(b5):
    b7[i, int(b4[i, 4])] = 1
b8 = np.arange(b5)
np.random.shuffle(b8)
b6 = np.array(b6[b8.reshape(-1)])
b7 = np.array(b7[b8.reshape(-1)])
b9 = b6[:int(b5/2)]
b10 = b7[:int(b5/2)]
b11 = b6[int(b5/2):]
b12 = b7[int(b5/2):]
a5 = 0.0031257
b13 = np.ones(15)
b14 = (a5/2.) * b13.T.dot(b13)
b15 = minimize(f, b13, args=(b9, b10, b14)).b6
b16 = []
b17 = []
for i in range(b11.shape[0]):
    b18 = np.zeros(a1)
    for b21 in range(a1):
        b18[b21] = np.exp(b15[5*b21:(5*b21)+5].T.dot(fonk2(b11, i)))
        if b18[b21] == np.inf:
            b18[b21] = 1000.
    b19 = b18 / np.sum(b18)
    b20 = np.amax(b19)
    b16.append((b19.tolist()).index(b20))
for i in range(b12.shape[0]):
    b19 = b12[i, :]
    b20 = np.amax(b19)
    b17.append((b19.tolist()).index(b20))
b21 = np.equal(b16, b17)
print("Overall classification b22 = ", float(np.sum(b21) / len(b12)) * 100., '%')
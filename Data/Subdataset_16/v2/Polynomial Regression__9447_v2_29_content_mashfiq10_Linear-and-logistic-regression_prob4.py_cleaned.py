import numpy as np
from scipy.optimize import minimize
def fonk1(b18):
    b1 = {b'Iris-setosa': 0., b'Iris-versicolor': 1., b'Iris-virginica': 2.}
    return b1[b18]
def fonk2(b6, i):
    b2 = np.ones(5)
    b2[1:5] = b6[i, 1:5]
    return b2
def fonk3(w, training_x, b10, b13):
    N, b3 = training_x.shape[0], 3
    a1 = 0.
    for n in range(N):
        ll2, b4 = 0., 0.
        for k in range(b3):
            ll2 += b10[n, k] * w[5*k:(5*k)+5].T.dot(fonk2(training_x, n))
        for l in range(b3):
            b4 += np.exp(w[5*l:(5*l)+5].T.dot(fonk2(training_x, n)))
        a1 += ll2 - np.log(b4)
        if a1 = = -np.inf:
            a1 = 0.
    return b13 - a1
b5 = np.loadtxt('iris.txt', delimiter=',', converters={4: flower_to_float})
M, b3 = b5.shape[0], 3
b6 = np.concatenate((np.ones(shape=(M, 1)), b5[:, :4]), axis=1)
b7 = np.zeros(shape=(M, b3))
for i in range(M):
    b7[i, int(b5[i, 4])] = 1
b8 = np.arange(M)
np.random.shuffle(b8)
b6, b7 = b6[b8], b7[b8]
b9 = int(M / 2)
training_x, b10 = b6[:b9], b7[:b9]
test_x, b11 = b6[b9:], b7[b9:]
a2 = 0.0031257
b12 = np.ones(15)
b13 = (a2 / 2.) * b12.T.dot(b12)
b14 = minimize(log_likelihood, b12, args=(training_x, b10, b13)).b6
b15 = []
b16 = []
for i in range(test_x.shape[0]):
    b17 = np.array([np.exp(b14[5*k:(5*k)+5].T.dot(fonk2(test_x, i))) for k in range(b3)])
    b17[b17 = = np.inf] = 1000.
    b18 = b17 / np.sum(b17)
    b15.append(np.argmax(b18))
for i in range(b11.shape[0]):
    b16.append(np.argmax(b11[i, :]))
b19 = np.mean(np.equal(b15, b16)) * 100.
print("Overall classification b19 = {:.2f}%".format(b19))
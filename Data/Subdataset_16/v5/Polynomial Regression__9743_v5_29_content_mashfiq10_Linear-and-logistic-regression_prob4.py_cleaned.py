import numpy as np
from scipy.optimize import minimize
def fonk1(b19):
    b1 = {
        b'Iris-setosa': 0.0,
        b'Iris-versicolor': 1.0,
        b'Iris-virginica': 2.0
    }
    return b1[b19]
def fonk2(b7, i):
    return np.hstack(([1.0], b7[i, 1:5]))
def fonk3(w, training_x, training_y, b14):
    b2 = training_x.shape[0]
    a1 = 3
    a2 = 0.0
    for n in range(b2):
        b3 = np.array([w[5*k:5*k+5].T.dot(fonk2(training_x, n)) for k in range(a1)])
        b4 = np.sum(training_y[n] * b3)
        b5 = np.sum(np.exp(b3))
        a2 += b4 - np.log(b5)
    return b14 - a2
b6 = np.loadtxt('iris.txt', delimiter=',', converters={4: flower_to_float})
b7 = np.hstack((np.ones((b6.shape[0], 1)), b6[:, :4]))
b8 = np.zeros((b6.shape[0], 3))
for i, label in enumerate(b6[:, 4]):
    b8[i, int(label)] = 1
b9 = np.arange(b6.shape[0])
np.random.shuffle(b9)
b7 = b7[b9]
b8 = b8[b9]
b10 = b6.shape[0]
training_x, b11 = b7[:b10], b7[b10:]
training_y, b12 = b8[:b10], b8[b10:]
a3 = 0.0031257
b13 = np.ones(15)
b14 = (a3 / 2.0) * np.dot(b13.T, b13)
b15 = minimize(log_likelihood, b13, args=(training_x, training_y, b14)).b7
b16 = []
b17 = []
for i in range(b11.shape[0]):
    b18 = np.array([np.exp(np.dot(b15[5*k:5*k+5], fonk2(b11, i))) for k in range(3)])
    b19 = b18 / np.sum(b18)
    b16.append(np.argmax(b19))
for i in range(b12.shape[0]):
    b17.append(np.argmax(b12[i]))
b20 = np.mean(np.equal(b16, b17)) * 100.0
print("Overall classification b20 = ", b20, '%')
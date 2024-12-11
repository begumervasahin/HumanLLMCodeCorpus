import itertools
import numpy as np
import pandas as pd
from time import time
import cvxopt.solvers
import numpy.linalg as la
from prettytable import PrettyTable
a1 = 1e-5
class class1:
    @staticmethod
    def fonk1():
        return lambda x, y: np.dot(x.T, y)
    @staticmethod
    def fonk2(b32, b33):
        return lambda x, y: ((b33 + np.dot(x.T, y)) ** b32)
    @staticmethod
    def fonk3(gamma):
        return lambda x, y: np.exp(-gamma * la.norm(np.subtract(x, y)))
class class2:
    def fonk4(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk5(self, b41, y):
        b3 = self.fonk8(b41, y)
        return self.fonk7(b41, y, b3)
    def fonk6(self, b41, n_samples):
        b4 = np.zeros((n_samples, n_samples))
        for i, x_i in enumerate(b41):
            for j, x_j in enumerate(b41):
                b4[i, j] = self.b1(x_i, x_j)
        return b4
    def fonk7(self, b41, y, b3):
        b5 = b3 > a1
        b6 = b3[b5]
        b7 = b41[b5]
        b8 = y[b5]
        b9 = np.mean(
            [y_k - class3(
                b1 = self.b1,
                b9 = 0.0,
                b10 = b6,
                b7 = b7,
                b8 = b8).fonk10(x_k)
             for (y_k, x_k) in zip(b8, b7)])
        return class3(
            b1 = self.b1,
            b9 = b9,
            b10 = b6,
            b7 = b7,
            b8 = b8)
    def fonk8(self, b41, y):
        n_samples, b11 = b41.shape
        b4 = self.fonk6(b41, n_samples)
        b12 = cvxopt.b30(np.outer(y, y) * b4)
        b13 = cvxopt.b30(-1 * np.ones(n_samples))
        b14 = cvxopt.b30(np.diag(np.ones(n_samples) * -1))
        b15 = cvxopt.b30(np.zeros(n_samples))
        b16 = cvxopt.b30(np.diag(np.ones(n_samples)))
        b17 = cvxopt.b30(np.ones(n_samples) * self.b2)
        b18 = cvxopt.b30(np.vstack((b14, b16)))
        b19 = cvxopt.b30(np.vstack((b15, b17)))
        b20 = cvxopt.b30(y, (1, n_samples), 'd')
        b21 = cvxopt.b30(0.0)
        b22 = cvxopt.solvers.qp(b12, b13, b18, b19, b20, b21)
        return np.ravel(b22['x'])
class class3:
    def fonk9(self,
                 b1,
                 b9,
                 b10,
                 b7,
                 b8):
        self.b23 = b1
        self.b24 = b9
        self.b25 = b10
        self.b26 = b7
        self.b27 = b8
        assert len(b7) == len(b8)
        assert len(b10) == len(b8)
    def fonk10(self, x):
        b28 = self.b24
        for z_i, x_i, y_i in zip(self.b25,
                                 self.b26,
                                 self.b27):
            b28 += z_i * y_i * self.b23(x_i, x)
        return np.sign(b28).item()
def fonk11(true_positive, false_positive, false_negative, true_negative):
    b29 = {}
    b29['precision'] = true_positive / (true_positive + false_positive)
    b29['recall'] = true_positive / (true_positive + false_negative)
    return b29
def fonk12(true_positive, false_positive, false_negative, true_negative):
    b30 = PrettyTable([' ', 'Ham', 'Spam'])
    b30.add_row(['Ham', true_positive, false_positive])
    b30.add_row(['Spam', false_negative, true_negative])
    return b30
def fonk13(b45, b46, b47, b48, b50, b31):
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    if b31 = = "polykernel":
        b32 = b50['b32']
        b33 = b50['b33']
        b34 = class2(class1.fonk2(b32, b33), 0.1)
        b35 = b34.fonk5(b45, b46)
    elif b31 = = "linear":
        b34 = class2(class1.fonk1(), 0.1)
        b35 = b34.fonk5(b45, b46)
    for i in range(b47.shape[0]):
        b36 = b35.fonk10(b47[i])
        if b36 = = -1 and b48[i] == -1:
            a3 += 1
        elif b36 = = 1 and b48[i] == -1:
            a5 += 1
        elif b36 = = 1 and b48[i] == 1:
            a4 += 1
        elif b36 = = -1 and b48[i] == 1:
            a2 += 1
    return fonk12(a4, a2, a5, a3), fonk11(a4, a2, a5, a3)
def fonk14(b30, b29, b50, b31, b51):
    with open("results.txt", "a") as f:
        if b31 = = "polykernel":
            f.write("Polykernel model b50\n")
            f.write(f"Dimension: {b50['b32']}\n")
            f.write(f"Offset: {b50['b33']}\n")
        elif b31 = = "linear":
            f.write("Linear model\n")
        f.write(f"{b30.get_string()}\n")
        f.write(f"Precision: {round(b29['precision'], 2)}\n")
        f.write(f"Recall: {round(b29['recall'], 2)}\n")
        f.write(f"Time spent for model: {round(time() - b51, 2)}\n\n\n")
b37 = time()
cvxopt.solvers.options['show_progress'] = False
b38 = pd.read_csv('wordslist.csv')
b39 = pd.read_csv('frequency.csv', header=0)
b40 = b39.values
b41 = b40[:, :-1]
b42 = b40[:, -1:]
b43 = b41.shape[0]
b44 = int(b41.shape[0] * 70 / 100)
b45 = b41[:b44, :]
b46 = b42[:b44, :]
b47 = b41[b44:, :]
b48 = b42[b44:, :]
with open("results.txt", "w+"):
    pass
a6 = 0
b49 = {'1': "polykernel", '2': "linear"}
b50 = {}
for i in range(2, 4):
    for j in range(10):
        b51 = time()
        b50['b32'] = i
        b50['b33'] = j
        b30, b29 = fonk13(b45, b46, b47, b48, b50, b49['1'])
        fonk14(b30, b29, b50, b49['1'], b51)
        a6 += 1
        print(f"Done: {a6}")
b51 = time()
b30, b29 = fonk13(b45, b46, b47, b48, b50, b49['2'])
fonk14(b30, b29, b50, b49['2'], b51)
a6 += 1
print(f"Done: {a6}")
with open("results.txt", "a") as f:
    f.write(f"Time spent for entire code: {round(time() - b37, 2)}")
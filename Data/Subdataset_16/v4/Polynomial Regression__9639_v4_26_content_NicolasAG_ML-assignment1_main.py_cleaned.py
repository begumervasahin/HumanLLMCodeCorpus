import argparse
from datetime import datetime as dt
import numpy as np
import a1q1d
import a1q1e
import a1q1f
import a1q1g
import a1q2
def fonk1(b1 = True):
    print("\nLoading b16...")
    with open('./hw1x.dat', 'rb') as file_x:
        b2 = np.array([list(map(float, line.split())) for line in file_x])
    with open('./hw1y.dat', 'rb') as file_y:
        b3 = np.array([list(map(float, line.split())) for line in file_y])
    if b1:
        b2 = (b2 - b2.mean(axis=0)) / b2.std(axis=0)
    print("b2 = ", b2.shape)
    print("b3 = ", b3.shape)
    return b2, b3
def fonk2(b2, b3, b4 = 0.2):
    print(f"\nSplitting b16 into {1 - b4:.2f} train {b4:.2f} test...")
    b5 = dt.now().microsecond
    np.random.b5(b5)
    b6 = np.random.permutation(b2.shape[0])
    b2, b3 = b2[b6], b3[b6]
    b7 = int(b2.shape[0] * b4)
    b10, b8 = b2[:b7], b2[b7:]
    b11, b9 = b3[:b7], b3[b7:]
    print("b8 = ", b8.shape)
    print("b10 = ", b10.shape)
    print("b9 = ", b9.shape)
    print("b11 = ", b11.shape)
    return b8, b9, b10, b11
def fonk3():
    def fonk4(value):
        return value.lower() in ('1', 'true', 'yes')
    b12 = argparse.ArgumentParser(description='COMP 652 - Machine Learning - Assignment 1')
    b12.add_argument('--q1d', b13 = "store_true", help='Produce only plots for q1.d)')
    b12.add_argument('--q1f', b13 = "store_true", help='Produce only plots for q1.f)')
    b12.add_argument('--q1g', b13 = "store_true", help='Produce only plots for q1.g)')
    b12.add_argument('--q2', b13 = "store_true", help='Produce only plots for q2.c)')
    b12.add_argument('--b1', b14 = parse_boolean, default=True, help='Normalize the X matrix when loading it')
    b12.add_argument('--use_sgd', b14 = parse_boolean, default=True, help='Run logistic regression using stochastic gradient descent')
    b12.add_argument('--n_iter', b14 = int, default=10000, help='Number of iterations for SGD or max number of iteration for LogReg')
    b15 = b12.parse_args()
    print(b15)
    b2, b3 = fonk1(b1=b15.b1)
    b8, b9, b10, b11 = fonk2(b2, b3, 0.2)
    b16 = None
    b17 = None
    b18 = [0.1, 0.5, 1, 5, 10]
    b19 = np.linspace(-10, 10, len(b18))
    b20 = not (b15.q1d or b15.q1f or b15.q1g or b15.q2)
    if b20 or b15.q1d:
        b16 = a1q1d.log_reg(b8, b9, b10, b11, b15.n_iter, b15.use_sgd)
        a1q1d.plot(b16)
    if b20 or b15.q1f:
        if b16 is None:
            b16 = a1q1d.log_reg(b8, b9, b10, b11, b15.n_iter, b15.use_sgd)
        b17 = a1q1e.reformat(b8, b10, b18, b19)
        b17 = a1q1f.log_reg(b17, b9, b11, b18, b15.n_iter, b15.use_sgd)
        a1q1f.plot(b17, b18, b16)
    if b20 or b15.q1g:
        if b17 is None:
            b17 = a1q1e.reformat(b8, b10, b18, b19)
            b17 = a1q1f.log_reg(b17, b9, b11, b18, b15.n_iter, b15.use_sgd)
        full_x_train, b21 = a1q1g.build_feature_matrices(b17, b18)
        b16 = a1q1g.log_reg(full_x_train, b21, b18, b9, b11, b15.n_iter, b15.use_sgd)
        a1q1g.plot(b16)
    if b20 or b15.q2:
        b16 = a1q2.log_reg(b8, b9, b10, b11)
        a1q2.plot(b16)
if b22 = = '__main__':
    fonk3()
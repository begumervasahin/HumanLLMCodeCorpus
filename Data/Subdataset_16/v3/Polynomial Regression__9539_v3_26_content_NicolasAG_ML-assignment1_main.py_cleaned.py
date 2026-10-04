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
    b2 = np.loadtxt('./hw1x.dat')
    b3 = np.loadtxt('./hw1y.dat')
    if b1:
        b2 = (b2 - np.mean(b2, axis=0)) / np.std(b2, axis=0)
    print(f"b2 = {b2.shape}")
    print(f"b3 = {b3.shape}")
    return b2, b3
def fonk2(b2, b3, b4 = 0.2):
    print(f"\nSplitting b16 into {1-b4:.2f} train {b4:.2f} test...")
    b5 = dt.now().microsecond
    np.random.b5(b5)
    b6 = np.random.permutation(b2.shape[0])
    b2 = b2[b6]
    b3 = b3[b6]
    b7 = int(b2.shape[0] * b4)
    b10, b8 = b2[b7:], b2[:b7]
    b11, b9 = b3[b7:], b3[:b7]
    print(f"b10 = {b10.shape}")
    print(f"b8 = {b8.shape}")
    print(f"b11 = {b11.shape}")
    print(f"b9 = {b9.shape}")
    return b10, b11, b8, b9
def fonk3(value):
    return value.lower() in ['1', 'true', 'yes']
def fonk4():
    b12 = argparse.ArgumentParser(description='COMP 652 - Machine Learning - Assignment 1')
    b12.add_argument('--q1d', b13 = "store_true", help='produce only plots for q1.d')
    b12.add_argument('--q1f', b13 = "store_true", help='produce only plots for q1.f')
    b12.add_argument('--q1g', b13 = "store_true", help='produce only plots for q1.g')
    b12.add_argument('--q2', b13 = "store_true", help='produce only plots for q2.c')
    b12.add_argument('--b1', b14 = parse_bool, default=True, help='b1 the X matrix when loading it')
    b12.add_argument('--use_sgd', b14 = parse_bool, default=True, help='run logistic regression using stochastic gradient descent')
    b12.add_argument('--n_iter', b14 = int, default=10000, help='number of iterations for SGD, or max number of iterations for LogReg')
    b15 = b12.parse_args()
    print(b15)
    b2, b3 = fonk1(b1=b15.b1)
    b10, b11, b8, b9 = fonk2(b2, b3, b4=0.2)
    b16 = None
    b17 = [0.1, 0.5, 1, 5, 10]
    b18 = np.linspace(-10, 10, len(b17))
    b19 = None
    b20 = not any([b15.q1d, b15.q1f, b15.q1g, b15.q2])
    if b20 or b15.q1d:
        b16 = a1q1d.log_reg(b10, b11, b8, b9, b15.n_iter, b15.use_sgd)
        a1q1d.plot(b16)
    if b20 or b15.q1f:
        if b16 is None:
            b16 = a1q1d.log_reg(b10, b11, b8, b9, b15.n_iter, b15.use_sgd)
        b19 = a1q1e.reformat(b10, b8, b17, b18)
        b19 = a1q1f.log_reg(b19, b11, b9, b17, b15.n_iter, b15.use_sgd)
        a1q1f.plot(b19, b17, b16)
    if b20 or b15.q1g:
        if b19 is None:
            b19 = a1q1e.reformat(b10, b8, b17, b18)
            b19 = a1q1f.log_reg(b19, b11, b9, b17, b15.n_iter, b15.use_sgd)
        full_x_train, b21 = a1q1g.build_feature_matrices(b19, b17)
        b16 = a1q1g.log_reg(full_x_train, b21, b17, b11, b9, b15.n_iter, b15.use_sgd)
        a1q1g.plot(b16)
    if b20 or b15.q2:
        b16 = a1q2.log_reg(b10, b11, b8, b9)
        a1q2.plot(b16)
if b22 = = '__main__':
    fonk4()
import os
import numpy as np
import matplotlib.pyplot as plt
import copy
import glob
import sys
from numpy.linalg import inv
from numpy.random import random, normal
from plot_functions import set_axis_ranges, plot_function, plot_data, show_all
def fonk1(b8):
    def fonk2(x):
        return fonk3(x, b8)
    return func
def fonk3(x, b8):
    a1 = 0
    for i in range(len(b8)):
        a1 += b8[i] * (x ** i)
    return a1
def fonk4(b4, b8):
    b1 = [fonk3(x, b8) for x in b4]
    return np.array(b1)
def fonk5(d, b8, n, b2 = -100, upper=100):
    assert len(b8) == d + 1, "Must pass in d+1 coefficients"
    b3 = upper - b2
    b4 = np.array([b2 + b3 * random() for _ in range(n)])
    b1 = fonk4(b4, b8)
    return b4, b1
def fonk6(x_train, b10, d, b5 = 0, noise_std=1):
    b6 = np.array([[x ** i for i in range(d + 1)] for x in x_train])
    b7 = np.array([a1 + normal(b5, noise_std) for a1 in b10])
    b8 = inv(b6.T @ b6) @ (b6.T @ b7)
    return b8
def fonk7(sample_coefficients, model_degree, n, b5 = 0, noise_std=0.5):
    b9 = len(sample_coefficients) - 1
    x_train, b10 = fonk5(b9, sample_coefficients, n, b2=-5, upper=5)
    b11 = fonk6(x_train, b10, model_degree, b5, noise_std)
    b12 = fonk1(sample_coefficients)
    b13 = fonk1(b11)
    b14 = fonk4(x_train, b11)
    b15 = np.mean((b14 - b10) ** 2)
    print(f"\nVariance of the b16 = {b15}\n")
    set_axis_ranges(x_train, b10)
    plot_function(x_train, b12, '-', b17 = 'r', label='Ground truth function')
    plot_function(x_train, b13, '--', b17 = 'b', label='Model fit function')
    plot_data(x_train, b10, '.', b17 = 'g', label='Sample points')
    show_all(b18 = 'upper right')
def fonk8():
    b8 = [3, 1, 1, -2]
    fonk7(b8, 3, 6, b5 = 0, noise_std=0.5)
if b19 = = "__main__":
    fonk8()
import os
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy.random import random, normal
from plot_functions import set_axis_ranges, plot_function, plot_data, show_all
def fonk1(b7):
    def fonk2(x):
        return fonk3(x, b7)
    return func
def fonk3(x, b7):
    return sum(coef * (x ** i) for i, coef in enumerate(b7))
def fonk4(b2, b7):
    return np.array([fonk3(x, b7) for x in b2])
def fonk5(order, b7, num_points, b1 = -100, upper=100):
    assert len(b7) == order + 1, "Must pass in order+1 b7"
    b2 = np.linspace(b1, upper, num_points)
    b3 = fonk4(b2, b7)
    return b2, b3
def fonk6(x_train, b9, order, b4 = 0, noise_std=1):
    b5 = np.array([[x ** i for i in range(order + 1)] for x in x_train])
    b6 = b9 + normal(b4, noise_std, b9.shape)
    b7 = inv(b5.T @ b5) @ (b5.T @ b6)
    return b7
def fonk7(sample_coefficients, model_degree, num_samples, b4 = 0, noise_std=0.5):
    b8 = len(sample_coefficients) - 1
    x_train, b9 = fonk5(b8, sample_coefficients, num_samples, b1=-5, upper=5)
    b10 = fonk6(x_train, b9, model_degree, b4, noise_std)
    b11 = fonk1(sample_coefficients)
    b12 = fonk1(b10)
    b13 = fonk4(x_train, b10)
    b14 = np.mean((b13 - b9) ** 2)
    print(f"\nVariance of the b15 = {b14}\n")
    set_axis_ranges(x_train, b9)
    plot_function(x_train, b11, '-', b16 = 'r', label='Ground truth function')
    plot_function(x_train, b12, '--', b16 = 'b', label='Model fit function')
    plot_data(x_train, b9, '.', b16 = 'g', label='Sample points')
    show_all(b17 = 'upper right')
def fonk8():
    b7 = [3, 1, 1, -2]
    fonk7(b7, 3, 6, b4 = 0, noise_std=0.5)
if b18 = = "__main__":
    fonk8()
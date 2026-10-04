import os
import numpy as np
import matplotlib.pyplot as plt
import copy
import glob
import sys
from numpy.linalg import inv
from numpy.random import random, normal
from plot_functions import set_axis_ranges, plot_function, plot_data, show_all
def make_function(w):
    def func(x):
        return evaluate_function(x, w)
    return func
def evaluate_function(x, w):
    y = 0
    for i in range(len(w)):
        y += w[i] * (x ** i)
    return y
def evaluate_function_vec(x_values, w):
    y_values = [evaluate_function(x, w) for x in x_values]
    return np.array(y_values)
def sample_function(d, w, n, lower=-100, upper=100):
    assert len(w) == d + 1, "Must pass in d+1 coefficients"
    func_range = upper - lower
    x_values = np.array([lower + func_range * random() for _ in range(n)])
    y_values = evaluate_function_vec(x_values, w)
    return x_values, y_values
def polynomial_regression(x_train, y_train, d, noise_mean=0, noise_std=1):
    X_mtx = np.array([[x ** i for i in range(d + 1)] for x in x_train])
    y_train_noisy = np.array([y + normal(noise_mean, noise_std) for y in y_train])
    w = inv(X_mtx.T @ X_mtx) @ (X_mtx.T @ y_train_noisy)
    return w
def run_experiment(sample_coefficients, model_degree, n, noise_mean=0, noise_std=0.5):
    sample_degree = len(sample_coefficients) - 1
    x_train, y_train = sample_function(sample_degree, sample_coefficients, n, lower=-5, upper=5)
    polyfit_coefficients = polynomial_regression(x_train, y_train, model_degree, noise_mean, noise_std)
    true_function = make_function(sample_coefficients)
    learned_function = make_function(polyfit_coefficients)
    y_model = evaluate_function_vec(x_train, polyfit_coefficients)
    variance = np.mean((y_model - y_train) ** 2)
    print(f"\nVariance of the polyfit = {variance}\n")
    set_axis_ranges(x_train, y_train)
    plot_function(x_train, true_function, '-', color='r', label='Ground truth function')
    plot_function(x_train, learned_function, '--', color='b', label='Model fit function')
    plot_data(x_train, y_train, '.', color='g', label='Sample points')
    show_all(legend_loc='upper right')
def main():
    w = [3, 1, 1, -2]
    run_experiment(w, 3, 6, noise_mean=0, noise_std=0.5)
if __name__ == "__main__":
    main()
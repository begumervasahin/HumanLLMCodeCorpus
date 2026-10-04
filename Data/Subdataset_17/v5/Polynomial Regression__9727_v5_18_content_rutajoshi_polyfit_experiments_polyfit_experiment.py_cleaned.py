import os
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy.random import random, normal
from plot_functions import set_axis_ranges, plot_function, plot_data, show_all
def make_function(coefficients):
    def func(x):
        return evaluate_function(x, coefficients)
    return func
def evaluate_function(x, coefficients):
    return sum(coef * (x ** i) for i, coef in enumerate(coefficients))
def evaluate_function_vec(x_values, coefficients):
    return np.array([evaluate_function(x, coefficients) for x in x_values])
def sample_function(order, coefficients, num_points, lower=-100, upper=100):
    assert len(coefficients) == order + 1, "Must pass in order+1 coefficients"
    x_values = np.linspace(lower, upper, num_points)
    y_values = evaluate_function_vec(x_values, coefficients)
    return x_values, y_values
def polynomial_regression(x_train, y_train, order, noise_mean=0, noise_std=1):
    X_mtx = np.array([[x ** i for i in range(order + 1)] for x in x_train])
    y_train_noisy = y_train + normal(noise_mean, noise_std, y_train.shape)
    coefficients = inv(X_mtx.T @ X_mtx) @ (X_mtx.T @ y_train_noisy)
    return coefficients
def run_experiment(sample_coefficients, model_degree, num_samples, noise_mean=0, noise_std=0.5):
    sample_degree = len(sample_coefficients) - 1
    x_train, y_train = sample_function(sample_degree, sample_coefficients, num_samples, lower=-5, upper=5)
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
    coefficients = [3, 1, 1, -2]
    run_experiment(coefficients, 3, 6, noise_mean=0, noise_std=0.5)
if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt
from polyfit_experiment import *
from plot_functions import *
def plot_noise_variance_experiment(sample_coefficients, model_degree, x_train, new_training_point_x, noise_std=0.5, noise_points=6):
    y_train = evaluate_function_vec(x_train, sample_coefficients)
    base_model_coefficients = polynomial_regression(x_train, y_train, model_degree)
    y_base_model = evaluate_function_vec(x_train, base_model_coefficients)
    base_variance = np.sum((y_base_model - y_train) ** 2)
    print(f"\nBase variance from true function with n={len(x_train)} training samples is: {base_variance}\n")
    new_training_point_y = evaluate_function(new_training_point_x, base_model_coefficients)
    dev_inc = (3 * noise_std) / (noise_points
    deviations = (
        [new_training_point_y - z * dev_inc for z in range(1, noise_points
        [new_training_point_y + z * dev_inc for z in range(1, noise_points
    )
    true_function = make_function(sample_coefficients)
    base_model_function = make_function(base_model_coefficients)
    set_axis_ranges(
        list(x_train) + [new_training_point_x],
        list(y_train) + [new_training_point_y] + list(y_base_model)
    )
    plot_function(x_train, true_function, '-', color='r', label='ground truth function')
    plot_function(x_train, base_model_function, '--', color='b', label='base model fit function')
    plot_data(x_train, y_train, '.', color='k', label='training data')
    plot_data([new_training_point_x], [new_training_point_y], '.', color='c', label='new training point')
    x_new_train = np.append(x_train, new_training_point_x)
    for deviation in deviations:
        y_new_train = np.append(y_train, deviation)
        new_model_coefficients = polynomial_regression(x_new_train, y_new_train, model_degree)
        y_new_model = evaluate_function_vec(x_train, new_model_coefficients)
        deviated_function = make_function(new_model_coefficients)
        plot_data([new_training_point_x], [deviation], '.', color='g', label='deviated point')
        plot_function(x_train, deviated_function, '-', color='m', label=None)
        variance = np.sum((y_new_model - y_base_model) ** 2) / len(y_base_model)
        print(f"Variance from base model using ({new_training_point_x}, {deviation}) = {variance}")
    print(f"\nFinished plotting for new training input {new_training_point_x}\n")
    show_all(legend_loc='upper right')
def main():
    sample_coefficients = [3, 1, 1, -2]
    model_degree = 4
    lower, upper = -50, 50
    input_range = upper - lower
    n = 4
    np.random.seed(1)
    x_train = np.linspace(lower, upper, n + 2)[1:-1]
    new_training_point_x = np.mean(x_train)
    plot_noise_variance_experiment(sample_coefficients, model_degree, x_train, new_training_point_x, noise_std=50)
if __name__ == "__main__":
    main()
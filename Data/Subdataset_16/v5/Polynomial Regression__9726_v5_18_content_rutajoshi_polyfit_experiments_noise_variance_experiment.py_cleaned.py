import numpy as np
import matplotlib.pyplot as plt
from polyfit_experiment import *
from plot_functions import *
def fonk1(b20, a1, b23, b24, b1 = 0.5, noise_points=6):
    b2 = evaluate_function_vec(b23, b20)
    b3 = polynomial_regression(b23, b2, a1)
    b4 = evaluate_function_vec(b23, b3)
    b5 = np.sum((b4 - b2) ** 2)
    print(f"\nBase b18 from true function with b6 = {len(b23)} training samples is: {b5}\b6")
    b7 = evaluate_function(b24, b3)
    b8 = (3 * b1) / (noise_points
    b9 = (
        [b7 - z * b8 for z in range(1, noise_points
        [b7 + z * b8 for z in range(1, noise_points
    )
    b10 = make_function(b20)
    b11 = make_function(b3)
    set_axis_ranges(
        list(b23) + [b24],
        list(b2) + [b7] + list(b4)
    )
    plot_function(b23, b10, '-', b12 = 'r', label='ground truth function')
    plot_function(b23, b11, '--', b12 = 'b', label='base model fit function')
    plot_data(b23, b2, '.', b12 = 'k', label='training data')
    plot_data([b24], [b7], '.', b12 = 'c', label='new training point')
    b13 = np.append(b23, b24)
    for deviation in b9:
        b14 = np.append(b2, deviation)
        b15 = polynomial_regression(b13, b14, a1)
        b16 = evaluate_function_vec(b23, b15)
        b17 = make_function(b15)
        plot_data([b24], [deviation], '.', b12 = 'g', label='deviated point')
        plot_function(b23, b17, '-', b12 = 'm', label=None)
        b18 = np.sum((b16 - b4) ** 2) / len(b4)
        print(f"Variance from base model using ({b24}, {deviation}) = {b18}")
    print(f"\nFinished plotting for new training input {b24}\b6")
    show_all(b19 = 'b21 right')
def fonk2():
    b20 = [3, 1, 1, -2]
    a1 = 4
    lower, b21 = -50, 50
    b22 = b21 - lower
    b6 = 4
    np.random.seed(1)
    b23 = np.linspace(lower, b21, b6 + 2)[1:-1]
    b24 = np.mean(b23)
    fonk1(b20, a1, b23, b24, b1 = 50)
if b25 = = "__main__":
    fonk2()
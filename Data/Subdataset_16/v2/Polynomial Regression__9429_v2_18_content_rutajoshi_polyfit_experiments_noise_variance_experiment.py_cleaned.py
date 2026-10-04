import numpy as np
import matplotlib.pyplot as plt
from polyfit_experiment import evaluate_function_vec, evaluate_function, polynomial_regression, make_function
from plot_functions import set_axis_ranges, plot_function, plot_data, show_all
def fonk1(b20, a1, b22, b23, b1 = 0.5, noise_points=6):
    b2 = evaluate_function_vec(b22, b20)
    b3 = polynomial_regression(b22, b2, a1)
    b4 = evaluate_function_vec(b22, b3)
    b5 = sum((b4 - b2) ** 2)
    print(f"\nBase b18 from true function with b6 = {len(b22)} training samples is: {b5}\b6")
    b7 = evaluate_function(b23, b3)
    b8 = (3 * b1) / (noise_points
    b9 = [b7 - z * b8 for z in range(1, noise_points
                 [b7 + z * b8 for z in range(1, noise_points
    b10 = make_function(b20)
    b11 = make_function(b3)
    set_axis_ranges(list(b22) + [b23], list(b2) + [b7] + list(b4))
    plot_function(b22, b10, '-', b12 = 'r', label='Ground Truth Function')
    plot_function(b22, b11, '--', b12 = 'b', label='Base Model Fit')
    plot_data(b22, b2, '.', b12 = 'k', label='Training Data')
    plot_data([b23], [b7], '.', b12 = 'c', label='New Training Point')
    b13 = np.append(b22, b23)
    for deviation in b9:
        b14 = np.append(b2, deviation)
        b15 = polynomial_regression(b13, b14, a1)
        b16 = evaluate_function_vec(b22, b15)
        b17 = make_function(b15)
        plot_data([b23], [deviation], '.', b12 = 'g', label='Deviated Point')
        plot_function(b22, b17, '-', b12 = 'm')
        b18 = sum((b16 - b4) ** 2) / len(b4)
        print(f"Variance from base model using ({b23}, {deviation}) = {b18}")
    print(f"\nFinished plotting for new training input {b23}\b6")
    show_all(b19 = 'b21 right')
def fonk2():
    b20 = [3, 1, 1, -2]
    a1 = 4
    lower, b21 = -50, 50
    b6 = 4
    np.random.seed(1)
    b22 = np.linspace(lower, b21, b6 + 2)[1:-1]
    b23 = np.mean([min(b22), max(b22)])
    fonk1(b20, a1, b22, b23, b1 = 50)
if b24 = = "__main__":
    fonk2()
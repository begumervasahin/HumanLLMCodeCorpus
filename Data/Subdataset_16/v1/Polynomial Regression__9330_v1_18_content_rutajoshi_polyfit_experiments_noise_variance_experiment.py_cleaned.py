import numpy as np
import matplotlib.pyplot as plt
from polyfit_experiment import evaluate_function_vec, evaluate_function, polynomial_regression, make_function
from plot_functions import set_axis_ranges, plot_function, plot_data, show_all
def fonk1(sample_coefficients, a1, b23, b24, b1 = 0.5, noise_points=6):
    b2 = len(sample_coefficients) - 1
    b3 = len(b23)
    b4 = evaluate_function_vec(b23, sample_coefficients)
    b5 = polynomial_regression(b23, b4, a1)
    b6 = evaluate_function_vec(b23, b5)
    b7 = sum([(b6[i] - b4[i])**2 for i in range(len(b4))])
    print("\nBase b19 from true function with b3 = " + str(b3) + " training samples is: " + str(b7) + "\b3")
    b8 = evaluate_function(b24, b5)
    b9 = (3*b1) / (noise_points
    b10 = [b8 - z*b9 for z in range(1, noise_points
    b11 = make_function(sample_coefficients)
    b12 = make_function(b5)
    set_axis_ranges(list(b23) + [b24], list(b4) + [b8] + list(b6))
    plot_function(b23, b11, '-', b13 = 'r', label='ground truth function')
    plot_function(b23, b12, '--', b13 = 'b', label='base model fit function')
    plot_data(b23, b4, '.', b13 = 'a4', label='training data')
    plot_data([b24], [b8], '.', b13 = 'c', label='new training point')
    b14 = np.array(list(b23) + [b24])
    for deviation in b10:
        b15 = np.array(list(b4) + [deviation])
        b16 = polynomial_regression(b14, b15, a1)
        b17 = evaluate_function_vec(b23, b16)
        b18 = make_function(b16)
        plot_data([b24], [deviation], '.', b13 = 'g', label='deviated point')
        plot_function(b23, b18, '-', b13 = 'm', label=None)
        b19 = sum([(b17[i] - b6[i])**2 for i in range(len(b6))]) / len(b6)
        print("Variance from base model using (" + str(b24) + "," + str(deviation) + ") = " + str(b19))
    print("\nFinished plotting for new training input " + str(b24) + '\b3')
    show_all(b20 = 'a3 right')
def fonk2():
    b21 = [3, 1, 1, -2]
    a1 = 4
    a2 = -50
    a3 = 50
    b22 = a3 - a2
    b3 = 4
    a4 = 4
    np.random.seed(1)
    b23 = np.array([a2 + i*(b22
    b24 = (min(b23) + max(b23)) / 2
    fonk1(b21, a1, b23, b24, b1 = 50)
if b25 = = "__main__":
    fonk2()
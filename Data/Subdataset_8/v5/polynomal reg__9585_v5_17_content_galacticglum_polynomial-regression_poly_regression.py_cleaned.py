import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
import argparse
import os
parser = argparse.ArgumentParser(description='Plot polynomial regression for a given dataset.')
parser.add_argument('--input', help='Path to the input data file (CSV).')
parser.add_argument('--poly_degree', default=2, type=int, help='Degree of the polynomial regression (default: 2).')
args = parser.parse_args()
dataset = pd.read_csv(args.input)
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values
dataset_name = os.path.splitext(os.path.basename(args.input))[0].replace('_', ' ').title()
x_label, y_label = dataset.columns
plt.scatter(X, y, color='green', label='Data Points')
def plot_polynomial_regression():
    weights = np.polyfit(X, y, args.poly_degree)
    model = np.poly1d(weights)
    plt.plot(X, model(X), color='orange', label='Polynomial Regression')
    polynomial_eq = sp.Poly(model.coef, spx).as_expr()
    print("Polynomial Regression Equation:")
    print(sp.latex(polynomial_eq))
def show_plot():
    plt.title(dataset_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.show()
plot_polynomial_regression()
show_plot()
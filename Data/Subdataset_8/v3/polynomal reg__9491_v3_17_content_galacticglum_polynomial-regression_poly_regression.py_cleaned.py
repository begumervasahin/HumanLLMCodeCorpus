import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from sympy.abc import x as spx
import argparse
import os
parser = argparse.ArgumentParser(description='Plot polynomial regression for given dataset.')
parser.add_argument('--input', help='Path to input data file (CSV format)', required=True)
parser.add_argument('--poly_degree', default=2, type=int, help='Degree of polynomial regression (default: 2)')
args = parser.parse_args()
dataset = pd.read_csv(args.input)
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values
dataset_name = os.path.splitext(os.path.basename(args.input))[0].replace('_', ' ').title()
x_label, y_label = dataset.columns.tolist()
plt.scatter(X, y, color='green')
def plot_polynomial_regression():
    weights = np.polyfit(X, y, args.poly_degree)
    model = np.poly1d(weights)
    plt.plot(X, model(X), color='orange')
    sp.init_printing()
    print("Polynomial Regression Equation:")
    print(sp.latex(sp.Poly(model.coef, spx).as_expr()))
def show_plot():
    plt.title(dataset_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
plot_polynomial_regression()
show_plot()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from sympy.abc import x as spx
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='The path to the input data file (csv) relative to the working directory.')
parser.add_argument('--poly_degree', default=2, type=int, help='The degree of the polynomial regression. Defaults to 1.')
args = parser.parse_args()
dataset = pd.read_csv(args.input)
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values
dataset_name = os.path.splitext(args.input)[0].replace('_', ' ').title()
dataset_columns = dataset.columns.tolist()
plt.scatter(X, y, color='green')
def plot_polynomial_regression():
    weights = np.polyfit(X, y, args.poly_degree)
    model = np.poly1d(weights)
    plt.plot(X, model(X), color='orange')
    sp.init_printing()
    print(sp.latex(sp.Poly(model.coef, spx).as_expr()))
def show_plot():
    plt.title(dataset_name)
    plt.xlabel(dataset_columns[0])
    plt.ylabel(dataset_columns[1])
    plt.show()
plot_polynomial_regression()
show_plot()
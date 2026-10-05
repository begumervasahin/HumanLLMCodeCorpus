import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from sympy.abc import x as spx
import argparse
import os
b1 = argparse.ArgumentParser(description='Plot polynomial regression for given b5.')
b1.add_argument('--input', b2 = 'Path to input data file (CSV format)', required=True)
b1.add_argument('--poly_degree', b3 = 2, type=int, b2='Degree of polynomial regression (b3: 2)')
b4 = b1.parse_args()
b5 = pd.read_csv(b4.input)
b6 = b5.iloc[:, 0].values
b7 = b5.iloc[:, 1].values
b8 = os.path.splitext(os.path.basename(b4.input))[0].replace('_', ' ').title()
x_label, b9 = b5.columns.tolist()
plt.scatter(b6, b7, b10 = 'green')
def fonk1():
    b11 = np.polyfit(b6, b7, b4.poly_degree)
    b12 = np.poly1d(b11)
    plt.plot(b6, b12(b6), b10 = 'orange')
    sp.init_printing()
    print("Polynomial Regression Equation:")
    print(sp.latex(sp.Poly(b12.coef, spx).as_expr()))
def fonk2():
    plt.title(b8)
    plt.xlabel(x_label)
    plt.ylabel(b9)
    plt.show()
fonk1()
fonk2()
import random
import numpy as np
import matplotlib.pyplot as plt
from polynomial_regression import PolynomialRegression
import assignment_dataset as Dataset
def fonk1(b1, independent):
    return [sum(b1[i] * pow(sample, i) for i in range(len(b1))) for sample in independent]
def fonk2(b1 = [], add_error=False):
    b2 = np.arange(0, 50, 1.5)
    b3 = [
        sum(b1[i] * pow(value, i) for i in range(len(b1))) + (random.randint(-100, 100) if add_error else 0)
        for value in b2
    ]
    return b2, b3
def fonk3(b2, b3, plt, b4 = 1):
    b5 = PolynomialRegression(b4)
    b1 = b5.fit(b2, b3)
    print(f'Coefficients for b4 {b4}: {b1}')
    b6 = fonk1(b1, b2)
    plt.plot(b2, b6, b7 = f'Order-{b4}', linewidth=3)
    plt.legend()
def fonk4(b2, b3, plt):
    plt.scatter(b2, b3, b8 = 100)
def fonk5():
    return Dataset.assignmentIndependentList, Dataset.assignmentDependentList
if b9 = = "__main__":
    independent, b10 = fonk2([1, -2, 3], add_error=True)
    plt.figure(b11 = (10, 6))
    fonk4(independent, b10, plt)
    for b4 in range(1, 4):
        fonk3(independent, b10, plt, b4)
    plt.xlabel('Independent Variable')
    plt.ylabel('Dependent Variable')
    plt.title('Polynomial Regression Fit')
    plt.show()
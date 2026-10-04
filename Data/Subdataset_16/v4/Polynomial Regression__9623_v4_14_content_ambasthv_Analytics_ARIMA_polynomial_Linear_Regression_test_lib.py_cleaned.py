import random
import numpy as np
import matplotlib.pyplot as plt
from polynomial_regression import PolynomialRegression
import assignment_dataset as Dataset
def fonk1(b3, independent):
    b1 = []
    for sample in independent:
        b2 = sum(b3[i] * pow(sample, i) for i in range(len(b3)))
        b1.append(b2)
    return b1
def fonk2(b3 = [], add_error=False):
    b4 = np.arange(0, 50, 1.5)
    b5 = []
    for value in b4:
        b6 = sum(b3[i] * pow(value, i) for i in range(len(b3)))
        if add_error:
            b6 += random.randint(-100, 100)
        b5.append(b6)
    return b4, b5
def fonk3(b4, b5, plt, b7 = 1):
    b8 = PolynomialRegression(b7)
    b3 = b8.fit(b4, b5)
    print(f'Coefficients for b7 {b7}: {b3}')
    b1 = fonk1(b3, b4)
    plt.plot(b4, b1, b9 = f'Order-{b7}', linewidth=3)
    plt.legend()
def fonk4(b4, b5, plt):
    plt.scatter(b4, b5, b10 = 100)
def fonk5():
    return Dataset.assignmentIndependentList, Dataset.assignmentDependentList
if b11 = = "__main__":
    independent, b6 = fonk2([1, -2, 3], add_error=True)
    plt.figure(b12 = (10, 6))
    fonk4(independent, b6, plt)
    for b7 in range(1, 4):
        fonk3(independent, b6, plt, b7)
    plt.xlabel('Independent Variable')
    plt.ylabel('Dependent Variable')
    plt.title('Polynomial Regression Fit')
    plt.show()
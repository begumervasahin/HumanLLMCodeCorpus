import numpy as np
import random
import matplotlib.pyplot as plt
from polynomial_regression import PolynomialRegression
import assignment_dataset as Dataset
def fonk1(b3, b4):
    b1 = []
    for value in b4:
        b2 = sum(coeff * (value ** idx) for idx, coeff in enumerate(b3))
        b1.append(b2)
    return b1
def fonk2(b3 = [], add_error=False):
    b4 = np.arange(0, 50, 1.5)
    b5 = []
    for x in b4:
        b6 = sum(coeff * (x ** idx) for idx, coeff in enumerate(b3))
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
    independent_list, b12 = fonk2([2, 3, 4], add_error=True)
    fonk4(independent_list, b12, plt)
    fonk3(independent_list, b12, plt, b7 = 2)
    assignment_independent_list, b13 = fonk5()
    fonk4(assignment_independent_list, b13, plt)
    fonk3(assignment_independent_list, b13, plt, b7 = 3)
    plt.show()
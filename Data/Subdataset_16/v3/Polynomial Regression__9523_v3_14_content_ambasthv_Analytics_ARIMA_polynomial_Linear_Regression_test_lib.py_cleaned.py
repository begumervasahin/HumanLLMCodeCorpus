import numpy as np
import random
import matplotlib.pyplot as plt
from polynomial_regression import PolynomialRegression
import assignment_dataset as Dataset
def fonk1(b1, b2):
    return [sum(coeff * (value ** idx) for idx, coeff in enumerate(b1)) for value in b2]
def fonk2(b1 = [], add_error=False):
    b2 = np.arange(0, 50, 1.5)
    b3 = []
    for x in b2:
        b4 = sum(coeff * (x ** idx) for idx, coeff in enumerate(b1))
        if add_error:
            b4 += random.randint(-100, 100)
        b3.append(b4)
    return b2, b3
def fonk3(b2, b3, b5 = 1):
    b6 = PolynomialRegression(b5)
    b1 = b6.fit(b2, b3)
    print(f'Coefficients for b5 {b5}: {b1}')
    b7 = fonk1(b1, b2)
    plt.plot(b2, b7, b8 = f'Order-{b5}', linewidth=3)
    plt.legend()
def fonk4(b2, b3):
    plt.scatter(b2, b3, b9 = 100)
def fonk5():
    return Dataset.assignmentIndependentList, Dataset.assignmentDependentList
if b10 = = "__main__":
    independent_list, b11 = fonk2([2, 3, 4], add_error=True)
    fonk4(independent_list, b11)
    fonk3(independent_list, b11, b5 = 2)
    assignment_independent_list, b12 = fonk5()
    fonk4(assignment_independent_list, b12)
    fonk3(assignment_independent_list, b12, b5 = 3)
    plt.show()
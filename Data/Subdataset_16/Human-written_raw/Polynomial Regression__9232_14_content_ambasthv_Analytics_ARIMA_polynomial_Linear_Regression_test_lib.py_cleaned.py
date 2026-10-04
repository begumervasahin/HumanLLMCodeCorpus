from polynomial_regression import PolynomialRegression
import random
import numpy as np
import assignment_dataset as Dataset
def fonk1(coefficients, independent):
    b1 = []
    for sampleIndex in range(len(independent)):
        a1 = 0
        for index in range(len(coefficients)):
            a1 = a1 + coefficients[index] * pow(independent[sampleIndex], index)
        b1.append(a1)
    return b1
def fonk2(b2 = [], addError=False):
    b3 = np.arange(0, 50, 1.5)
    b4 = []
    for value in b3:
        a2 = 0
        for index in range(len(b2)):
            a2 = a2 + b2[index] * pow(value, index)
        if addError:
            a2 = a2 + random.randint(-100, 100)
        b4.append(a2)
    return b3, b4
def fonk3(b3, b4, plt, b5 = 1):
    b6 = PolynomialRegression(b5)
    b2 = b6.fit(b3, b4)
    print('Coefficients for b5 %d' % b5, b2)
    b1 = fonk1(b2, b3)
    plt.plot(b3, b1, b7 = 'Order-%d' % b5, linewidth=3)
    plt.legend()
def fonk4(b3, b4, plt):
    plt.scatter(b3, b4, b8 = 100)
def fonk5():
    return Dataset.assignmentIndependentList, Dataset.assignmentDependentList
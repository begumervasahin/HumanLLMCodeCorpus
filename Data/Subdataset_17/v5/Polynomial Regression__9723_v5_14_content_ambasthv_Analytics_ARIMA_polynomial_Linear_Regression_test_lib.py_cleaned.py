import random
import numpy as np
import matplotlib.pyplot as plt
from polynomial_regression import PolynomialRegression
import assignment_dataset as Dataset
def get_predictions(coefficients, independent):
    return [sum(coefficients[i] * pow(sample, i) for i in range(len(coefficients))) for sample in independent]
def generate_dataset(coefficients=[], add_error=False):
    independent_list = np.arange(0, 50, 1.5)
    dependent_list = [
        sum(coefficients[i] * pow(value, i) for i in range(len(coefficients))) + (random.randint(-100, 100) if add_error else 0)
        for value in independent_list
    ]
    return independent_list, dependent_list
def fit_line_and_plot(independent_list, dependent_list, plt, order=1):
    regression = PolynomialRegression(order)
    coefficients = regression.fit(independent_list, dependent_list)
    print(f'Coefficients for order {order}: {coefficients}')
    prediction_list = get_predictions(coefficients, independent_list)
    plt.plot(independent_list, prediction_list, label=f'Order-{order}', linewidth=3)
    plt.legend()
def draw_scatter_plot(independent_list, dependent_list, plt):
    plt.scatter(independent_list, dependent_list, s=100)
def get_assignment_dataset():
    return Dataset.assignmentIndependentList, Dataset.assignmentDependentList
if __name__ == "__main__":
    independent, dependent = generate_dataset([1, -2, 3], add_error=True)
    plt.figure(figsize=(10, 6))
    draw_scatter_plot(independent, dependent, plt)
    for order in range(1, 4):
        fit_line_and_plot(independent, dependent, plt, order)
    plt.xlabel('Independent Variable')
    plt.ylabel('Dependent Variable')
    plt.title('Polynomial Regression Fit')
    plt.show()
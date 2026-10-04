import numpy as np
import random
import matplotlib.pyplot as plt
from polynomial_regression import PolynomialRegression
import assignment_dataset as Dataset
def get_predictions(coefficients, independent):
    return [sum(coeff * (value ** idx) for idx, coeff in enumerate(coefficients)) for value in independent]
def generate_dataset(coefficients=[], add_error=False):
    independent = np.arange(0, 50, 1.5)
    dependent = []
    for x in independent:
        y = sum(coeff * (x ** idx) for idx, coeff in enumerate(coefficients))
        if add_error:
            y += random.randint(-100, 100)
        dependent.append(y)
    return independent, dependent
def fit_line_and_plot(independent, dependent, order=1):
    regression = PolynomialRegression(order)
    coefficients = regression.fit(independent, dependent)
    print(f'Coefficients for order {order}: {coefficients}')
    predictions = get_predictions(coefficients, independent)
    plt.plot(independent, predictions, label=f'Order-{order}', linewidth=3)
    plt.legend()
def draw_scatter_plot(independent, dependent):
    plt.scatter(independent, dependent, s=100)
def get_assignment_dataset():
    return Dataset.assignmentIndependentList, Dataset.assignmentDependentList
if __name__ == "__main__":
    independent_list, dependent_list = generate_dataset([2, 3, 4], add_error=True)
    draw_scatter_plot(independent_list, dependent_list)
    fit_line_and_plot(independent_list, dependent_list, order=2)
    assignment_independent_list, assignment_dependent_list = get_assignment_dataset()
    draw_scatter_plot(assignment_independent_list, assignment_dependent_list)
    fit_line_and_plot(assignment_independent_list, assignment_dependent_list, order=3)
    plt.show()
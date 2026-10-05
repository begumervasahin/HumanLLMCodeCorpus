import numpy as np
from sympy import *
init_printing()
print('\n\nInitial Setup Complete')
def display_cost_function_and_derivative(cost_function, derivative):
    print("Cost function f(x) =", cost_function)
    print("Derivative df(x)/dx =", derivative)
def get_user_input():
    initial_approximation = float(input("Enter initial approximation: "))
    error_tolerance = float(input("Enter error tolerance: "))
    learning_rate = float(input("Enter learning rate: "))
    return initial_approximation, error_tolerance, learning_rate
def print_initial_values(initial_approximation, cost_function_eval):
    print("Starting NAdam")
    print("Initial approximation x0 =", initial_approximation)
    print("f(x0) =", cost_function_eval)
def update_values(x0, mk, vk, vc_k, learning_rate, epsilon):
    mk = b1 * m0 + (1 - b1) * gt
    vk = b2 * v0 + (1 - b2) * (gt**2)
    vc_k = max(vc_0, vk)
    x_k = x_k - (learning_rate / (vc_k**0.5 + epsilon)) * mk
    return mk, vk, vc_k, x_k
def optimize_nadam(cost_function, cost_function_eval, derivative):
    display_cost_function_and_derivative(cost_function, derivative)
    initial_approximation, error_tolerance, learning_rate = get_user_input()
    iter_count = 0
    x_k = initial_approximation
    x_previous = 0.0
    m0 = 0.0
    vk = vc_0 = vc_k = 0.0
    b1, b2, epsilon = 0.9, 0.999, 10**-8
    while True:
        iter_count += 1
        x_previous = x0
        x0 = x_k
        m0, v0 = mk, vk
        vc_0, vc_k = vc_k, max(vc_0, vk)
        derivative_fk = lambdify(x, derivative, "numpy")(x_k)
        gt = derivative_fk
        mk, vk, vc_k, x_k = update_values(x_k, mk, vk, vc_k, learning_rate, epsilon)
        if abs(N(x_k - x0)) < error_tolerance or abs(N(x_k - x_previous)) < 0.1 * error_tolerance:
            break
    print("Number of Iterations =", iter_count)
    print("Minima is at =", x_k)
    print("Minimum value of Cost Function =", cost_function_eval)
x = Symbol('x')
print()
input_cost_function = input("Enter cost function f(x): ").strip()
cost_function_symbolic = sympify(input_cost_function)
cost_function_derivative = diff(cost_function_symbolic, x)
cost_function_numeric = lambdify(x, cost_function_symbolic, "numpy")
optimize_nadam(cost_function_symbolic, cost_function_numeric, cost_function_derivative)
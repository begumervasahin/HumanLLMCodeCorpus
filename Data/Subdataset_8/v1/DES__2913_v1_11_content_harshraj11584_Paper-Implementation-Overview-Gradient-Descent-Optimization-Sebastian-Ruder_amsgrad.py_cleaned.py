import numpy as np
from sympy import *
init_printing()
print('\n\nInitial Setup Complete')
def nadam(cost_function, f):
    print("Cost function f(x) =", cost_function)
    f_dash = diff(cost_function, x)
    print("Derivative df(x)/dx =", f_dash)
    initial_approximation = float(input("Enter initial approximation: "))
    x0 = initial_approximation
    error_tolerance = float(input("Enter error tolerance: "))
    learning_rate = float(input("Enter learning rate: "))
    print("Starting NAdam")
    print("Initial approximation x0 =", initial_approximation)
    print("f(x0) =", f(initial_approximation))
    iter_count = 0
    x_k = x0
    x_previous = 0.0
    m0 = 0.0
    mk = 0.0
    v0 = 0.0
    vk = 0.0
    vc_0 = 0.0
    vc_k = 0.0
    b1 = 0.9
    b2 = 0.999
    epsilon = 10**-8
    while True:
        iter_count += 1
        x_previous = x0
        x0 = x_k
        m0 = mk
        v0 = vk
        vc_0 = vc_k
        derivative_fk = (lambdify(x, f_dash, "numpy"))(x_k)
        gt = derivative_fk
        mk = b1 * m0 + (1 - b1) * gt
        vk = b2 * v0 + (1 - b2) * (gt**2)
        vc_k = max(vc_0, vk)
        x_k = x_k - (learning_rate / (vc_k**0.5 + epsilon)) * mk
        if abs(N(x_k - x0)) < error_tolerance or abs(N(x_k - x_previous)) < 0.1 * error_tolerance:
            break
    print("Number of Iterations =", iter_count)
    print("Minima is at =", x_k)
    print("Minimum value of Cost Function =", f(x_k))
x = Symbol('x')
print()
input_cost_function = input("Enter cost function f(x): ").strip()
cost_function_symbolic = sympify(input_cost_function)
cost_function_numeric = lambdify(x, cost_function_symbolic, "numpy")
nadam(cost_function_symbolic, cost_function_numeric)
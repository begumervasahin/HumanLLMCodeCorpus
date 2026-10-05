import numpy as np
from sympy import *
init_printing()
def adam(cost_function, f):
    print("Cost function f(x) =", cost_function)
    derivative = diff(cost_function, x)
    print("Derivative df(x)/dx =", derivative)
    initial_approximation = float(input("Enter initial approximation: "))
    error_tolerance = float(input("Enter error tolerance: "))
    learning_rate = float(input("Enter learning rate: "))
    print("Starting Adam")
    print("Initial approximation x0 =", initial_approximation)
    print("f(x0) =", f(initial_approximation))
    iterations = 0
    xk = initial_approximation
    previous_x = 0.0
    m0 = 0.0
    mk = 0.0
    v0 = 0.0
    vk = 0.0
    beta1 = 0.9
    beta2 = 0.999
    epsilon = 10**-8
    while True:
        iterations += 1
        previous_x = xk
        x0 = xk
        m0 = mk
        v0 = vk
        derivative_value = lambdify(x, derivative, "numpy")(xk)
        gradient = derivative_value
        mk = beta1 * m0 + (1 - beta1) * gradient
        vk = beta2 * v0 + (1 - beta2) * (gradient**2)
        mc_k = mk / (1 - beta1**iterations)
        vc_k = vk / (1 - beta2**iterations)
        xk = xk - learning_rate * mc_k / ((vc_k**0.5) + epsilon)
        if abs(N(xk - x0)) < error_tolerance or abs(N(xk - previous_x)) < 0.1 * error_tolerance:
            break
    print("Number of Iterations =", iterations)
    print("Minima is at =", xk)
    print("Minimum value of Cost Function =", f(xk))
x = Symbol('x')
print()
user_input = input("Enter cost function f(x): ").strip()
cost_function = sympify(user_input)
f = lambdify(x, cost_function, "numpy")
adam(cost_function, f)
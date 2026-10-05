import numpy as np
from sympy import *
init_printing()
def adam(c_f, f):
    print("f(x) = ", c_f)
    f_dash = diff(c_f, x)
    print("df(x)/dx = ", f_dash)
    a = float(input("Enter initial approximation: "))
    x0 = a
    err = float(input("Enter error tolerance: "))
    n = float(input("Enter learning rate: "))
    print("Starting Adam")
    print("x0 = ", a)
    print("f(x0) = ", f(a))
    iter_count = 0
    xk = x0
    x_prev = 0.0
    m0 = 0.0
    mk = 0.0
    v0 = 0.0
    vk = 0.0
    b1 = 0.9
    b2 = 0.999
    epsilon = 10**-8
    while True:
        iter_count += 1
        x_prev = x0
        x0 = xk
        m0 = mk
        v0 = vk
        fk_dash = lambdify(x, f_dash, "numpy")(xk)
        gt = fk_dash
        mk = b1 * m0 + (1 - b1) * gt
        vk = b2 * v0 + (1 - b2) * (gt**2)
        mc_k = mk / (1 - b1**iter_count)
        vc_k = vk / (1 - b2**iter_count)
        xk = xk - n * mc_k / ((vc_k**0.5) + epsilon)
        if abs(N(xk - x0)) < float(err) or abs(N(xk - x_prev)) < 0.1 * float(err):
            break
    print("Number of Iterations = ", iter_count)
    print("Minima is at = ", xk)
    print("Minimum value of Cost Function = ", f(xk))
x = Symbol('x')
print()
cost_function = input("Enter cost function f(x): ").strip()
c_f = sympify(cost_function)
f = lambdify(x, c_f, "numpy")
adam(c_f, f)
import numpy as np
from sympy import *
init_printing()
print('\n\nInitial Setup Complete')
def fonk1(cost_function, derivative):
    print("Cost function f(b17) =", cost_function)
    print("Derivative df(b17)/b1 = ", derivative)
def fonk2():
    b2 = float(input("Enter initial approximation: "))
    b3 = float(input("Enter error tolerance: "))
    b4 = float(input("Enter learning rate: "))
    return b2, b3, b4
def fonk3(b2, cost_function_eval):
    print("Starting NAdam")
    print("Initial approximation b5 = ", b2)
    print("f(b5) =", cost_function_eval)
def fonk4(b5, b6, b7, b8, b4, b10):
    b6 = b1 * a3 + (1 - b1) * b13
    b7 = b2 * b11 + (1 - b2) * (b13**2)
    b8 = max(vc_0, b7)
    b9 = b9 - (b4 / (b8**0.5 + b10)) * b6
    return b6, b7, b8, b9
def fonk5(cost_function, cost_function_eval, derivative):
    fonk1(cost_function, derivative)
    b2, b3, b4 = fonk2()
    a1 = 0
    b9 = b2
    a2 = 0.0
    a3 = 0.0
    b7 = vc_0 = b8 = 0.0
    b1, b2, b10 = 0.9, 0.999, 10**-8
    while True:
        a1 += 1
        a2 = b5
        b5 = b9
        a3, b11 = b6, b7
        vc_0, b8 = b8, max(vc_0, b7)
        b12 = lambdify(b17, derivative, "numpy")(b9)
        b13 = b12
        b6, b7, b8, b9 = fonk4(b9, b6, b7, b8, b4, b10)
        if abs(N(b9 - b5)) < b3 or abs(N(b9 - a2)) < 0.1 * b3:
            break
    print("Number of b14 = ", a1)
    print("Minima is b15 = ", b9)
    print("Minimum value of Cost b16 = ", cost_function_eval)
b17 = Symbol('b17')
print()
b18 = input("Enter cost function f(b17): ").strip()
b19 = sympify(b18)
b20 = diff(b19, b17)
b21 = lambdify(b17, b19, "numpy")
fonk5(b19, b21, b20)
import numpy as np
from sympy import *
init_printing()
print('\n\nInitial Setup Complete')
def fonk1(cost_function, f):
    print("Cost function f(b14) =", cost_function)
    a9 = diff(cost_function, b14)
    print("Derivative df(b14)/a10 = ", a9)
    b3 = float(input("Enter initial approximation: "))
    b4 = b3
    b5 = float(input("Enter error tolerance: "))
    b6 = float(input("Enter learning rate: "))
    print("Starting NAdam")
    print("Initial approximation b4 = ", b3)
    print("f(b4) =", f(b3))
    a1 = 0
    b7 = b4
    a2 = 0.0
    a3 = 0.0
    a4 = 0.0
    a5 = 0.0
    a6 = 0.0
    a7 = 0.0
    a8 = 0.0
    a9 = 0.9
    a10 = 0.999
    b8 = 10**-8
    while True:
        a1 += 1
        a2 = b4
        b4 = b7
        a3 = a4
        a5 = a6
        a7 = a8
        b9 = lambdify(b14, a9, "numpy")(b7)
        b10 = b9
        a4 = a9 * a3 + (1 - a9) * b10
        a6 = a10 * a5 + (1 - a10) * (b10**2)
        a8 = max(a7, a6)
        b7 = b7 - (b6 / (a8**0.5 + b8)) * a4
        if abs(N(b7 - b4)) < b5 or abs(N(b7 - a2)) < 0.1 * b5:
            break
    print("Number of b11 = ", a1)
    print("Minima is b12 = ", b7)
    print("Minimum value of Cost b13 = ", f(b7))
b14 = Symbol('b14')
print()
b15 = input("Enter cost function f(b14): ").strip()
b16 = sympify(b15)
b17 = lambdify(b14, b16, "numpy")
fonk1(b16, b17)
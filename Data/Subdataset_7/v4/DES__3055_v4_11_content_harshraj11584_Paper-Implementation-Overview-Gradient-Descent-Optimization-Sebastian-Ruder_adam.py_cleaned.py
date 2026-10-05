import numpy as np
from sympy import *
init_printing()
print('\b6\nInitial Setup Complete')
def fonk1(b18, b19):
    print("Cost function b19(b16) =", b18)
    a7 = diff(b18, b16)
    print("Derivative df(b16)/a8 = ", a7)
    b3 = float(input("Enter initial approximation: "))
    b4 = b3
    b5 = float(input("Enter error tolerance: "))
    b6 = float(input("Enter learning rate: "))
    print("Starting Adam")
    print("Initial approximation b4 = ", b3)
    print("b19(b4) =", b19(b3))
    a1 = 0
    b7 = b4
    a2 = 0.0
    a3 = 0.0
    a4 = 0.0
    a5 = 0.0
    a6 = 0.0
    a7 = 0.9
    a8 = 0.999
    b8 = 10**-8
    while True:
        a1 += 1
        a2 = b4
        b4 = b7
        a3 = a4
        a5 = a6
        b9 = (lambdify(b16, a7, "numpy"))(b7)
        b10 = b9
        a4 = a7 * a3 + (1 - a7) * b10
        a6 = a8 * a5 + (1 - a8) * (b10**2)
        b11 = a4 / (1 - a7**a1)
        b12 = a6 / (1 - a8**a1)
        b7 = b7 - b6 * b11 / ((b12**0.5) + b8)
        if abs(N(b7 - b4)) < float(b5) or abs(N(b7 - a2)) < 0.1 * float(b5):
            break
    print("Number of b13 = ", a1)
    print("Minima is b14 = ", b7)
    print("Minimum value of Cost b15 = ", b19(b7))
b16 = Symbol('b16')
print()
b17 = input("Enter cost function b19(b16): ").strip()
b18 = sympify(b17)
b19 = lambdify(b16, b18, "numpy")
fonk1(b18, b19)
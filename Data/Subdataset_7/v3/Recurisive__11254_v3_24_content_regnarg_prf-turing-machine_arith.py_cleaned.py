from prf import *
b1 = Proj(1, 0)
b2 = C(S, zero)
b3 = C(S, Proj(3, 0))
def fonk1(function, operation, arity):
    b4 = function
    for _ in range(arity):
        b4 = PR(b4, Proj(arity + 1, _))
    b4 = accel(b4, operation, arity)
    return b4
b5 = fonk1(b1, lambda x, y: x + y, 2)
def fonk2(x):
    return x - 1 if x > 0 else 0
b6 = C(PR(b1, Proj(3, 1)), Proj(1, 0), Proj(1, 0))
b6 = fonk1(b6, predecessor_operation, 1)
b7 = C(b6, Proj(3, 0))
def fonk3(x, y):
    return x - y if x >= y else 0
b8 = fonk1(b1, subtraction_operation, 2)
def fonk4(x, y):
    return x * y
b9 = fonk1(zero, multiplication_operation, 2)
def fonk5(x, y):
    return x ** y
b10 = fonk1(b2, power_operation, 2)
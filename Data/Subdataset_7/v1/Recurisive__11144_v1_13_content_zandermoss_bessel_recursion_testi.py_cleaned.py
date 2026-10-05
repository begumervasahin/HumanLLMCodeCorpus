import numpy as np
from scipy.special import spherical_jn
from scipy import integrate
def fonk1(x, a3, a4):
    return x**a4 * spherical_jn(a3, x)
a1 = 2
a2 = 4
a3 = 4
a4 = 3
val, b1 = integrate.quad(IInt, a1, a2, args=(a3, a4))
def fonk2(dummy_obj, x, params):
    return x**params[1] * spherical_jn(params[0], x)
b2 = fonk2(None, a1, (a3, a4))
b3 = fonk2(None, a2, (a3, a4))
print("Testing I Integration")
print("X in [{}, {}]".format(a1, a2))
print("a3 = ", a3)
print("a4 = ", a4)
print("Recursive Integral: ", b3 - b2)
print("Numerical Integral: ", val, " +/- ", b1)
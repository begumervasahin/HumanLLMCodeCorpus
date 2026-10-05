import numpy as np
from scipy.special import spherical_jn
from scipy import integrate
def IInt(x, l, n):
    return x**n * spherical_jn(l, x)
xlow = 2
xhigh = 4
l = 4
n = 3
val, err = integrate.quad(IInt, xlow, xhigh, args=(l, n))
def ICrawlerDict(dummy_obj, x, params):
    return x**params[1] * spherical_jn(params[0], x)
ylow = ICrawlerDict(None, xlow, (l, n))
yhigh = ICrawlerDict(None, xhigh, (l, n))
print("Testing I Integration")
print("X in [{}, {}]".format(xlow, xhigh))
print("l =", l)
print("n =", n)
print("Recursive Integral: ", yhigh - ylow)
print("Numerical Integral: ", val, " +/- ", err)
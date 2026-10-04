import numpy as np
from Crawlers import ICrawlerDict, XYCrawlerDict
from scipy.special import spherical_jn
from scipy import integrate
a1 = 2
a2 = 4
a3 = 4
a4 = 3
def fonk1(x, a3, a4):
    return x**a4 * spherical_jn(a3, x)
numerical_val, b1 = integrate.quad(integrand, a1, a2, args=(a3, a4))
b2 = XYCrawlerDict()
b3 = ICrawlerDict(b2)
b4 = b3.GetEntry(a1, (a3, a4))
b5 = b3.GetEntry(a2, (a3, a4))
b6 = b5 - b4
print("Testing I Integration")
print(f"X in [{a1}, {a2}]")
print(f"a3 = {a3}")
print(f"a4 = {a4}")
print(f"Recursive Integral: {b6}")
print(f"Numerical Integral: {numerical_val} +/- {b1}")
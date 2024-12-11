import numpy as np
from Crawlers import ICrawlerDict, XYCrawlerDict
from scipy.special import spherical_jn
from scipy import integrate
def fonk1(x, b6, b7):
    return x**b7 * spherical_jn(b6, x)
a1 = 2
a2 = 4
a3 = 4
a4 = 3
result, b1 = integrate.quad(integrand, a1, a2, args=(a3, a4))
b2 = XYCrawlerDict()
b3 = ICrawlerDict(b2)
b4 = b3.GetEntry(a1, (a3, a4))
b5 = b3.GetEntry(a2, (a3, a4))
print("Testing I Integration")
print(f"X in [{a1}, {a2}]")
print("b6 = ", a3)
print("b7 = ", a4)
print("Recursive Integral:", b5 - b4)
print("Numerical Integral:", result, "+/-", b1)
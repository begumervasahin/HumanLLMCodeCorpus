import numpy as np
from Crawlers import ICrawlerDict
from Crawlers import XYCrawlerDict
from scipy.special import spherical_jn
from scipy import integrate
a1 = 2
a2 = 4
a3 = 4
a4 = 3
def fonk1(x, a3, a4):
    return x**a4 * spherical_jn(a3, x)
val, b1 = integrate.quad(IInt, a1, a2, args=(a3, a4))
b2 = XYCrawlerDict()
b3 = ICrawlerDict(b2)
b4 = b3.GetEntry(a1, (a3, a4))
b5 = b3.GetEntry(a2, (a3, a4))
print("Testing I Integration")
print("X in [{}, {}]".format(a1, a2))
print("a3 = ", a3)
print("a4 = ", a4)
print("Recursive Integral:", b5 - b4)
print("Numerical Integral:", val, "+/-", b1)
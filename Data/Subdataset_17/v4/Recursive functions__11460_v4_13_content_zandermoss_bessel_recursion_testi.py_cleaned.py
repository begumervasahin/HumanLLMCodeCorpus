import numpy as np
from Crawlers import ICrawlerDict, XYCrawlerDict
from scipy.special import spherical_jn
from scipy import integrate
xlow = 2
xhigh = 4
l = 4
n = 3
def IInt(x, l, n):
    return x**n * spherical_jn(l, x)
val, err = integrate.quad(IInt, xlow, xhigh, args=(l, n))
xyca = XYCrawlerDict()
ca = ICrawlerDict(xyca)
ylow = ca.GetEntry(xlow, (l, n))
yhigh = ca.GetEntry(xhigh, (l, n))
print("Testing I Integration")
print(f"X in [{xlow}, {xhigh}]")
print(f"l = {l}")
print(f"n = {n}")
print(f"Recursive Integral: {yhigh - ylow}")
print(f"Numerical Integral: {val} +/- {err}")
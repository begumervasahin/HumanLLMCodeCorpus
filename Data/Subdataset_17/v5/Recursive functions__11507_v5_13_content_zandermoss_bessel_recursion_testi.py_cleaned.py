import numpy as np
from Crawlers import ICrawlerDict, XYCrawlerDict
from scipy.special import spherical_jn
from scipy import integrate
xlow = 2
xhigh = 4
l = 4
n = 3
def integrand(x, l, n):
    return x**n * spherical_jn(l, x)
numerical_val, numerical_err = integrate.quad(integrand, xlow, xhigh, args=(l, n))
xy_crawler = XYCrawlerDict()
crawler = ICrawlerDict(xy_crawler)
y_low = crawler.GetEntry(xlow, (l, n))
y_high = crawler.GetEntry(xhigh, (l, n))
recursive_integral = y_high - y_low
print("Testing I Integration")
print(f"X in [{xlow}, {xhigh}]")
print(f"l = {l}")
print(f"n = {n}")
print(f"Recursive Integral: {recursive_integral}")
print(f"Numerical Integral: {numerical_val} +/- {numerical_err}")
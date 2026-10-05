import numpy as np
from Crawlers import ICrawlerDict, XYCrawlerDict
from scipy.special import spherical_jn
from scipy import integrate
def integrand(x, l, n):
    return x**n * spherical_jn(l, x)
x_low = 2
x_high = 4
l_value = 4
n_value = 3
result, error = integrate.quad(integrand, x_low, x_high, args=(l_value, n_value))
xy_crawler = XYCrawlerDict()
crawler = ICrawlerDict(xy_crawler)
y_low = crawler.GetEntry(x_low, (l_value, n_value))
y_high = crawler.GetEntry(x_high, (l_value, n_value))
print("Testing I Integration")
print(f"X in [{x_low}, {x_high}]")
print("l =", l_value)
print("n =", n_value)
print("Recursive Integral:", y_high - y_low)
print("Numerical Integral:", result, "+/-", error)
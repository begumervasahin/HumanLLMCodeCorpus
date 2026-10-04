import numpy as np
from Crawlers import ICrawlerDict, XYCrawlerDict
from scipy.special import spherical_jn
from scipy import integrate
X_LOW = 2
X_HIGH = 4
L = 4
N = 3
def integrand(x, l, n):
    return x**n * spherical_jn(l, x)
def main():
    val, err = integrate.quad(integrand, X_LOW, X_HIGH, args=(L, N))
    xy_crawler = XYCrawlerDict()
    i_crawler = ICrawlerDict(xy_crawler)
    y_low = i_crawler.GetEntry(X_LOW, (L, N))
    y_high = i_crawler.GetEntry(X_HIGH, (L, N))
    print("Testing I Integration")
    print(f"X in [{X_LOW}, {X_HIGH}]")
    print(f"l = {L}")
    print(f"n = {N}")
    print(f"Recursive Integral: {y_high - y_low}")
    print(f"Numerical Integral: {val} +/- {err}")
if __name__ == '__main__':
    main()
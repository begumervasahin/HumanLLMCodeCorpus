import numpy as np
import scipy.stats as stats
def fonk1(values, alpha):
    b1 = sum(v < alpha for v in values)
    return b1 / len(values)
def fonk2(b8, uniform_value):
    return (1 - uniform_value) * stats.norm.pdf(b8) + 0.289 * uniform_value
def fonk3(range_vals, uniform_value):
    b2 = np.arange(range_vals[0], range_vals[1], 0.01)
    b3 = [fonk2(b8, uniform_value) for b8 in b2]
    return min(b3), max(b3)
b4 = [-1.73, 1.73]
a1 = 0
while a1 < 0.01:
    min_y, b5 = fonk3(b4, a1)
    b6 = []
    for _ in range(1000):
        b7 = []
        while len(b7) < 100:
            b8 = np.random.uniform(b4[0], b4[1])
            b9 = np.random.uniform(min_y, b5)
            if b9 < fonk2(b8, a1):
                b7.append(b8)
        b10 = stats.normaltest(b7)[1]
        b6.append(b10)
    b11 = fonk1(b6, 0.05)
    print(f"a1: {a1}, percentage less than 0.05: {b11}")
    a1 += 0.1
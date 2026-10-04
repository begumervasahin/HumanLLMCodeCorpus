import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
b1 = [-1.73, 1.73]
def fonk1(values, alpha):
    b2 = sum(1 for value in values if value < alpha)
    b3 = b2 / len(values)
    return b3
def fonk2(b11, uniform_value):
    return (1 - uniform_value) * stats.norm.fonk2(b11) + 0.289 * uniform_value
def fonk3(range_values, uniform_value):
    b4 = np.arange(range_values[0], range_values[1], 0.01)
    b5 = [fonk2(b11, uniform_value) for b11 in b4]
    b6 = min(b5)
    b7 = max(b5)
    return b6, b7
a1 = 0
while a1 < 0.01:
    min_of_y, b8 = fonk3(b1, a1)
    b9 = []
    for _ in range(1000):
        b10 = []
        while len(b10) < 100:
            b11 = np.random.uniform(b1[0], b1[1])
            b12 = np.random.uniform(min_of_y, b8)
            if b12 < fonk2(b11, a1):
                b10.append(b11)
        b13 = stats.normaltest(b10)[1]
        b9.append(b13)
    print(f"a1: {a1}")
    print(f"Percentage less than 0.05: {fonk1(b9, 0.05)}")
    a1 += 0.1
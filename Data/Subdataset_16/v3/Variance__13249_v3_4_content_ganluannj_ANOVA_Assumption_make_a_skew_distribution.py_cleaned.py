import numpy as np
import scipy.stats as stats
b1 = [-1.73, 1.73]
def fonk1(values, alpha):
    b2 = sum(value < alpha for value in values)
    b3 = b2 / len(values)
    return b3
def fonk2(b12, uniform_value):
    return (1 - uniform_value) * stats.norm.fonk2(b12) + 0.289 * uniform_value
def fonk3(range_values, uniform_value):
    b4 = np.arange(range_values[0], range_values[1], 0.01)
    b5 = [fonk2(b12, uniform_value) for b12 in b4]
    b6 = min(b5)
    b7 = max(b5)
    return b6, b7
def fonk4(b1, b8 = 0.1, num_iterations=1000, sample_size=100):
    a1 = 0
    while a1 < 0.01:
        min_of_y, b9 = fonk3(b1, a1)
        b10 = []
        for _ in range(num_iterations):
            b11 = []
            while len(b11) < sample_size:
                b12 = np.random.uniform(b1[0], b1[1])
                b13 = np.random.uniform(min_of_y, b9)
                if b13 < fonk2(b12, a1):
                    b11.append(b12)
            b14 = stats.normaltest(b11)[1]
            b10.append(b14)
        b3 = fonk1(b10, 0.05)
        print(f"a1: {a1:.2f}, Percentage less than 0.05: {b3:.2%}")
        a1 += b8
fonk4(b1)
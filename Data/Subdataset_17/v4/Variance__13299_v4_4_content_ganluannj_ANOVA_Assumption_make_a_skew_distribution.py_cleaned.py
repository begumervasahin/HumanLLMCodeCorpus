import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
def lessthan(values, alpha):
    count = sum(1 for v in values if v < alpha)
    return count / len(values)
def pdf(x, uniform_value):
    return (1 - uniform_value) * stats.norm.pdf(x) + 0.289 * uniform_value
def find_min_and_max(range_vals, uniform_value):
    x_vals = np.arange(range_vals[0], range_vals[1], 0.01)
    y_vals = [pdf(x, uniform_value) for x in x_vals]
    return [min(y_vals), max(y_vals)]
range_of_x = [-1.73, 1.73]
p = 0
while p < 0.01:
    min_y, max_y = find_min_and_max(range_of_x, p)
    p_values = []
    for _ in range(1000):
        samples = []
        while len(samples) < 100:
            x = np.random.uniform(range_of_x[0], range_of_x[1])
            y = np.random.uniform(min_y, max_y)
            if y < pdf(x, p):
                samples.append(x)
        p_value = stats.normaltest(samples)[1]
        p_values.append(p_value)
    print(f"p: {p}, less than 0.05: {lessthan(p_values, 0.05)}")
    p += 0.1
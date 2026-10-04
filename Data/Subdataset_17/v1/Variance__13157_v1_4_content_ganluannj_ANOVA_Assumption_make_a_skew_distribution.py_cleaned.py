import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
range_of_x = [-1.73, 1.73]
def lessthan(values, alpha):
    count = sum(1 for value in values if value < alpha)
    percentage = count / len(values)
    return percentage
def pdf(x, uniform_value):
    return (1 - uniform_value) * stats.norm.pdf(x) + 0.289 * uniform_value
def find_min_and_max(range_values, uniform_value):
    list_of_range = np.arange(range_values[0], range_values[1], 0.01)
    pdf_values = [pdf(x, uniform_value) for x in list_of_range]
    min_value = min(pdf_values)
    max_value = max(pdf_values)
    return min_value, max_value
p = 0
while p < 0.01:
    min_of_y, max_of_y = find_min_and_max(range_of_x, p)
    p_value_list = []
    for _ in range(1000):
        samples = []
        while len(samples) < 100:
            x = np.random.uniform(range_of_x[0], range_of_x[1])
            y = np.random.uniform(min_of_y, max_of_y)
            if y < pdf(x, p):
                samples.append(x)
        p_value = stats.normaltest(samples)[1]
        p_value_list.append(p_value)
    print(f"p: {p}")
    print(f"Percentage less than 0.05: {lessthan(p_value_list, 0.05)}")
    p += 0.1
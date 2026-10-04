import numpy as np
import scipy.stats as stats
def calculate_percentage(values, alpha):
    count = sum(v < alpha for v in values)
    return count / len(values)
def custom_pdf(x, uniform_value):
    return (1 - uniform_value) * stats.norm.pdf(x) + 0.289 * uniform_value
def find_min_and_max_pdf(range_vals, uniform_value):
    x_vals = np.arange(range_vals[0], range_vals[1], 0.01)
    y_vals = [custom_pdf(x, uniform_value) for x in x_vals]
    return min(y_vals), max(y_vals)
range_of_x = [-1.73, 1.73]
p = 0
while p < 0.01:
    min_y, max_y = find_min_and_max_pdf(range_of_x, p)
    p_values = []
    for _ in range(1000):
        samples = []
        while len(samples) < 100:
            x = np.random.uniform(range_of_x[0], range_of_x[1])
            y = np.random.uniform(min_y, max_y)
            if y < custom_pdf(x, p):
                samples.append(x)
        p_value = stats.normaltest(samples)[1]
        p_values.append(p_value)
    percentage_less_than_0_05 = calculate_percentage(p_values, 0.05)
    print(f"p: {p}, percentage less than 0.05: {percentage_less_than_0_05}")
    p += 0.1
import numpy as np
import scipy.stats as stats
range_of_x = [-1.73, 1.73]
def lessthan(values, alpha):
    count = sum(value < alpha for value in values)
    percentage = count / len(values)
    return percentage
def pdf(x, uniform_value):
    return (1 - uniform_value) * stats.norm.pdf(x) + 0.289 * uniform_value
def find_min_and_max(range_values, uniform_value):
    x_values = np.arange(range_values[0], range_values[1], 0.01)
    pdf_values = [pdf(x, uniform_value) for x in x_values]
    min_value = min(pdf_values)
    max_value = max(pdf_values)
    return min_value, max_value
def perform_experiment(range_of_x, step=0.1, num_iterations=1000, sample_size=100):
    p = 0
    while p < 0.01:
        min_of_y, max_of_y = find_min_and_max(range_of_x, p)
        p_value_list = []
        for _ in range(num_iterations):
            samples = []
            while len(samples) < sample_size:
                x = np.random.uniform(range_of_x[0], range_of_x[1])
                y = np.random.uniform(min_of_y, max_of_y)
                if y < pdf(x, p):
                    samples.append(x)
            p_value = stats.normaltest(samples)[1]
            p_value_list.append(p_value)
        percentage = lessthan(p_value_list, 0.05)
        print(f"p: {p:.2f}, Percentage less than 0.05: {percentage:.2%}")
        p += step
perform_experiment(range_of_x)
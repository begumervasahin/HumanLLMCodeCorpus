import numpy as np
import math
from scipy.stats import norm
def get_min(array):
    return np.min(array)
def get_max(array):
    return np.max(array)
def f(x):
    return math.pow(x, 3) + (3 * math.pow(x, 2)) + (3 * x) + 1
def fa(array, n):
    return np.mean([f(x) for x in array])
def calculate_vf(array, f_average, n):
    return np.sum(np.power(np.array([f(x) for x in array]) - f_average, 2)) / (n - 1)
data_uniform = np.genfromtxt('RandUnif.csv', delimiter='')
data_normal = np.genfromtxt('RandDist.csv', delimiter='')
bottom_uniform = 2
top_uniform = 4
bottom_normal = get_min(data_normal)
top_normal = get_max(data_normal)
n_uniform = len(data_uniform)
n_normal = len(data_normal)
probability = 0.95
k_value = norm.ppf(probability)
f_average_uniform = fa(data_uniform, n_uniform)
variance_uniform = calculate_vf(data_uniform, f_average_uniform, n_uniform)
scaled_variance_uniform = variance_uniform / n_uniform
lower_bound_uniform = (top_uniform - bottom_uniform) * (f_average_uniform - (k_value * scaled_variance_uniform))
upper_bound_uniform = (top_uniform - bottom_uniform) * (f_average_uniform + (k_value * scaled_variance_uniform))
print(f'Uniform Distribution Results (Bag A): [{lower_bound_uniform}, {upper_bound_uniform}]')
f_average_normal = fa(data_normal, n_normal)
variance_normal = calculate_vf(data_normal, f_average_normal, n_normal)
scaled_variance_normal = variance_normal / n_normal
lower_bound_normal = (top_normal - bottom_normal) * (f_average_normal - (k_value * scaled_variance_normal))
upper_bound_normal = (top_normal - bottom_normal) * (f_average_normal + (k_value * scaled_variance_normal))
print(f'Normal Distribution Results (Bag B): [{lower_bound_normal}, {upper_bound_normal}]')
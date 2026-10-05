import numpy as np
import math
from scipy.stats import norm
def get_min(arr):
    minimum = arr[0]
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum
def get_max(arr):
    maximum = arr[0]
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum
def f(x):
    return math.pow(x, 3) + (3 * math.pow(x, 2)) + (3 * x) + 1
def fa(arr, n):
    total_sum = 0
    for i in range(len(arr)):
        total_sum += f(arr[i])
    return total_sum / n
def calculate_variance_f(arr, f_mean, n):
    variance_sum = 0
    for i in range(len(arr)):
        variance_sum += math.pow(f(arr[i]) - f_mean, 2)
    return (1 / (n - 1)) * variance_sum
data_uniform = np.genfromtxt('RandUnif.csv', delimiter='')
data_normal = np.genfromtxt('RandDist.csv', delimiter='')
bottom_uniform = 2
top_uniform = 4
N = len(data_uniform)
confidence_probability = 0.95
k_value = norm.ppf(confidence_probability)
f_mean_uniform = fa(data_uniform, N)
variance_f_uniform = calculate_variance_f(data_uniform, f_mean_uniform, N)
variance_f_uniform_scaled = variance_f_uniform / N
lower_uniform = (top_uniform - bottom_uniform) * (f_mean_uniform - (k_value * variance_f_uniform_scaled))
upper_uniform = (top_uniform - bottom_uniform) * (f_mean_uniform + (k_value * variance_f_uniform_scaled))
print(f'Uniform Distribution Mean-Variance Result (Section A):\n[{lower_uniform}, {upper_uniform}]')
bottom_normal = get_min(data_normal)
top_normal = get_max(data_normal)
f_mean_normal = fa(data_normal, N)
variance_f_normal = calculate_variance_f(data_normal, f_mean_normal, N)
variance_f_normal_scaled = variance_f_normal / N
lower_normal = (top_normal - bottom_normal) * (f_mean_normal - (k_value * variance_f_normal_scaled))
upper_normal = (top_normal - bottom_normal) * (f_mean_normal + (k_value * variance_f_normal_scaled))
print(f'Normal Distribution Mean-Variance Result (Section B):\n[{lower_normal}, {upper_normal}]')
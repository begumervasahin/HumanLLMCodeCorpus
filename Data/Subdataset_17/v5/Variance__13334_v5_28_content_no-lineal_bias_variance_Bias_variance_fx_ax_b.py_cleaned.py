import os
import random
import math
from numpy import arange, pi, sin
import matplotlib.pyplot as plt
EXPERIMENTS = 200
slopes = []
intercepts = []
def perform_experiments(num_experiments):
    for _ in range(num_experiments):
        x1, x2 = random.uniform(-1, 1), random.uniform(-1, 1)
        y1, y2 = sin(x1 * pi), sin(x2 * pi)
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1
        slopes.append(slope)
        intercepts.append(intercept)
def calculate_bias(mean_slope, mean_intercept, x_values):
    bias_list = [(mean_slope * x + mean_intercept - sin(x * pi)) ** 2 for x in x_values]
    return sum(bias_list) / len(bias_list)
def calculate_variance(mean_slope, mean_intercept, x_values):
    deviations = [
        [(slope - mean_slope) * x + (intercept - mean_intercept) for slope, intercept in zip(slopes, intercepts)]
        for x in x_values
    ]
    squared_deviations = [[dev ** 2 for dev in devs] for devs in deviations]
    variance_list = [sum(devs) / (len(devs) - 1) for devs in squared_deviations]
    return sum(variance_list) / len(variance_list)
def plot_results(x_values, ft, mean_slope, mean_intercept, bias, variance):
    plt.plot(x_values, ft, label='sin(t*pi)')
    plt.grid(True)
    plt.ylim(-2, 2)
    plt.xlim(-1, 1)
    for slope, intercept in zip(slopes, intercepts):
        plt.plot(x_values, slope * x_values + intercept, alpha=0.5, color='g')
    plt.plot(x_values, mean_slope * x_values + mean_intercept, alpha=0.5, color='r', linewidth=2, label='Mean Line')
    plt.text(-0.9, 1.75, f'Bias: {bias:.6f}')
    plt.text(-0.9, 1.64, f'Variance: {variance:.6f}')
    plt.legend()
    plt.savefig(os.path.join('Sinusoidal_dos.png'), dpi=300, format='png', bbox_inches='tight')
    plt.show()
perform_experiments(EXPERIMENTS)
x_values = arange(-1, 1.01, 0.01)
ft = sin(x_values * pi)
mean_slope = sum(slopes) / len(slopes)
mean_intercept = sum(intercepts) / len(intercepts)
bias = calculate_bias(mean_slope, mean_intercept, x_values)
variance = calculate_variance(mean_slope, mean_intercept, x_values)
print(f'Bias = {bias:.6f}')
print(f'Variance = {variance:.6f}')
plot_results(x_values, ft, mean_slope, mean_intercept, bias, variance)
import numpy as np
import random
import math
from matplotlib import pyplot as plt
EXPERIMENTS = 200
T_STEP = 0.01
def generate_b_list(experiments):
    b_list = []
    for _ in range(experiments):
        x1, x2 = random.uniform(0, 1.0), random.uniform(0, 1.0)
        y1, y2 = np.sin(2 * np.pi * x1), np.sin(2 * np.pi * x2)
        distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        b = max(y1, y2) - distance / 2
        b_list.append(b)
    return b_list
def compute_bias(b_list, t):
    mean_b = np.mean(b_list)
    bias_list = [(mean_b - np.sin(2 * np.pi * elem)) ** 2 for elem in t]
    return np.mean(bias_list)
def compute_variance(b_list):
    mean_b = np.mean(b_list)
    variance_list = [(elem - mean_b) ** 2 for elem in b_list]
    return np.sum(variance_list) / (len(b_list) - 1)
def plot_results(t, ft, b_list, bias, variance):
    plt.plot(t, ft, label='sin(2Ït)')
    plt.grid(True)
    plt.ylim(-2, 2)
    plt.xlim(0, 1)
    mean_b = np.mean(b_list)
    g_bar_imp = [mean_b] * len(t)
    for b in b_list:
        plt.plot(t, [b] * len(t), alpha=0.5, color='g')
    plt.plot(t, g_bar_imp, alpha=0.5, color='r', linewidth=2, label='gÌ')
    plt.text(0.5, 1.75, f'Bias = {bias:.6f}')
    plt.text(0.5, 1.64, f'Variance = {variance:.6f}')
    plt.legend()
    plt.show()
def main():
    t = np.arange(0, 1, T_STEP)
    ft = np.sin(2 * np.pi * t)
    b_list = generate_b_list(EXPERIMENTS)
    bias = compute_bias(b_list, t)
    variance = compute_variance(b_list)
    print(f'Bias = {bias:.6f}')
    print(f'Variance = {variance:.6f}')
    plot_results(t, ft, b_list, bias, variance)
if __name__ == "__main__":
    main()
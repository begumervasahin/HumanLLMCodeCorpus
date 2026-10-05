import matplotlib.pyplot as plt
import numpy as np
from math import floor
from random import randint
from sys import maxsize
from time import time
def binary_search(arr, size, target):
    left = 0
    right = size - 1
    while left <= right:
        mid = int(floor((left + right) / 2))
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1
def linear_search(arr, size, target):
    for i in range(size):
        if arr[i] == target:
            return i
        if arr[i] > target:
            return -1
    return -1
def generate_random_array(size):
    return [randint(-maxsize - 1, maxsize) for _ in range(size)]
def calculate_cpu_time(search_func, arr, num_trials):
    total_time = 0
    for _ in range(num_trials):
        start_time = time()
        search_func(arr, len(arr), arr[randint(0, len(arr) - 1)])
        end_time = time()
        total_time += end_time - start_time
    return total_time / num_trials
def run_performance_trials(num_trials=5, benchmark=False, array_size=None):
    threshold = 2 if array_size is None else array_size
    while True:
        binary_search_time = linear_search_time = float('inf')
        arr = generate_random_array(threshold)
        arr.sort()
        binary_search_time = calculate_cpu_time(binary_search, arr, num_trials) / num_trials
        linear_search_time = calculate_cpu_time(linear_search, arr, num_trials) / num_trials
        if not benchmark:
            return linear_search_time, binary_search_time
        if benchmark and binary_search_time < linear_search_time:
            return threshold
        threshold += 1
def find_threshold():
    return sum(run_performance_trials(250, True) for _ in range(100)) / 100
def get_model(linear, data):
    if linear:
        b = min(data)
        b_index = data.index(b)
        slowest_time = max(data)
        slowest_index = data.index(slowest_time)
        m = (slowest_time - b) / (slowest_index - b_index)
        return lambda array_size: m * array_size + b
    else:
        b, a = np.polyfit(np.log(np.array([i for i in range(1, len(data) + 1)])), np.array(data), 1)
        return lambda array_size: a + (b * np.log(array_size))
def plot_performance(max_array_size=50, num_trials=250):
    linear_y = []
    binary_y = []
    for size in range(1, max_array_size + 1):
        linear_perf, binary_perf = run_performance_trials(num_trials, array_size=size)
        linear_y.append(linear_perf)
        binary_y.append(binary_perf)
    linear_model = get_model(True, linear_y)
    binary_model = get_model(False, binary_y)
    plt.plot(linear_y, 'o', label='Linear search')
    plt.plot(binary_y, 'o', label='Binary search')
    plt.plot([i for i in range(1, max_array_size + 1)], [linear_model(i) for i in range(1, max_array_size + 1)])
    plt.plot([i for i in range(1, max_array_size + 1)], [binary_model(i) for i in range(1, max_array_size + 1)])
    plt.legend()
    plt.xlim(left=1)
    plt.title('Linear versus binary search runtime')
    plt.xlabel('Size of array')
    plt.ylabel('CPU time')
    plt.show()
    return linear_model, binary_model
linear_model, binary_model = plot_performance(350)
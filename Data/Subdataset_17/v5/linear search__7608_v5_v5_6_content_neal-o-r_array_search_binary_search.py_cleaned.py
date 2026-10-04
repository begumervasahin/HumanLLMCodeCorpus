import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def linear_search(arr):
    comparisons = 0
    previous_element = float('-inf')
    for current_element in arr:
        if current_element < previous_element:
            return comparisons
        comparisons += 1
        previous_element = current_element
    return comparisons
def binary_search(arr, initial_index=0):
    if len(arr) == 1:
        return initial_index + 1
    mid_index = len(arr)
    pivot = arr[mid_index]
    if pivot == arr[0]:
        return initial_index + 1
    if pivot < arr[0]:
        return binary_search(arr[:mid_index], initial_index)
    else:
        return binary_search(arr[mid_index:], initial_index + mid_index)
def time_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
def measure_search_times(ns, num_iterations=10, num_trials=100):
    bins = []
    lins = []
    for n in ns:
        binary_search_time_total = 0
        linear_search_time_total = 0
        for _ in range(num_trials):
            arr = np.roll(np.arange(n), np.random.randint(n))
            t_linear_search = time_wrapper(linear_search, arr)
            t_binary_search = time_wrapper(binary_search, arr)
            binary_search_time_total += timeit.timeit(t_binary_search, number=num_iterations)
            linear_search_time_total += timeit.timeit(t_linear_search, number=num_iterations)
        bins.append(binary_search_time_total / num_trials)
        lins.append(linear_search_time_total / num_trials)
    return bins, lins
def plot_search_times(ns, linear_times, binary_times):
    max_linear_time = max(linear_times)
    max_n = max(ns)
    plt.plot(ns, np.array(linear_times) / max_linear_time, '-o', label='Linear Search')
    plt.plot(ns, np.array(binary_times) / max_linear_time, '-o', label='Binary Search')
    plt.plot(ns, np.array(ns) / max_n, '--k', label='Linear')
    plt.plot(ns, np.log2(np.array(ns)) / np.log2(max_n), '--k', label='Logarithmic')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Normalized Time')
    plt.title('Comparison of Linear and Binary Search Times')
    plt.legend()
    plt.show()
def main():
    ns = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    binary_times, linear_times = measure_search_times(ns)
    plot_search_times(ns, linear_times, binary_times)
if __name__ == '__main__':
    main()
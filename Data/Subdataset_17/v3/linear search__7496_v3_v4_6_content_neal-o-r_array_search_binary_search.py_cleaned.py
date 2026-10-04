import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def linear_search(arr):
    comparisons = 0
    previous_element = -np.inf
    for current_element in arr:
        if current_element < previous_element:
            return comparisons
        comparisons += 1
        previous_element = current_element
    return comparisons
def binary_search(arr, initial_index=0):
    pivot = arr[len(arr)
    if pivot == arr[0]:
        return initial_index + 1
    if pivot < arr[0]:
        return binary_search(arr[:len(arr)
    else:
        initial_index += len(arr)
        return binary_search(arr[len(arr)
def time_function(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
def measure_search_times(ns, num_trials=100, num_iterations=10):
    linear_times = []
    binary_times = []
    for n in ns:
        total_linear_time = 0
        total_binary_time = 0
        for _ in range(num_trials):
            arr = np.roll(np.arange(n), np.random.randint(n))
            t_linear = time_function(linear_search, arr)
            t_binary = time_function(binary_search, arr)
            total_linear_time += timeit.timeit(t_linear, number=num_iterations)
            total_binary_time += timeit.timeit(t_binary, number=num_iterations)
        linear_times.append(total_linear_time / num_trials)
        binary_times.append(total_binary_time / num_trials)
    return linear_times, binary_times
def plot_search_times(ns, linear_times, binary_times):
    plt.plot(ns, np.array(linear_times) / max(linear_times), '-o', label='Linear Search')
    plt.plot(ns, np.array(binary_times) / max(linear_times), '-o', label='Binary Search')
    plt.plot(ns, np.array(ns) / max(ns), '--k', label='Linear')
    plt.plot(ns, np.log2(np.array(ns)) / max(np.log2(ns)), '--r', label='Logarithmic')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Normalized Time')
    plt.title('Performance Comparison of Linear and Binary Search on Rotated Arrays')
    plt.legend()
    plt.show()
def main():
    ns = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    linear_times, binary_times = measure_search_times(ns)
    plot_search_times(ns, linear_times, binary_times)
if __name__ == '__main__':
    main()
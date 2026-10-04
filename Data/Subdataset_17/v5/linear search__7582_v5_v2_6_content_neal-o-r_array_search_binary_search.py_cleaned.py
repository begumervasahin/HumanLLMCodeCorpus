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
def binary_search(arr, start_index=0):
    middle_index = len(arr)
    pivot = arr[middle_index]
    if pivot == arr[0]:
        return start_index + 1
    if pivot < arr[0]:
        return binary_search(arr[:middle_index], start_index)
    else:
        start_index += middle_index
        return binary_search(arr[middle_index:], start_index)
def time_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
def run_search_experiments(array_sizes, num_trials=100, num_iterations=10):
    linear_search_times = []
    binary_search_times = []
    for n in array_sizes:
        total_time_binary = 0
        total_time_linear = 0
        for _ in range(num_trials):
            arr = np.roll(np.arange(n), np.random.randint(n))
            wrapped_linear_search = time_wrapper(linear_search, arr)
            wrapped_binary_search = time_wrapper(binary_search, arr)
            total_time_binary += timeit.timeit(wrapped_binary_search, number=num_iterations)
            total_time_linear += timeit.timeit(wrapped_linear_search, number=num_iterations)
        average_time_binary = total_time_binary / num_trials
        average_time_linear = total_time_linear / num_trials
        binary_search_times.append(average_time_binary)
        linear_search_times.append(average_time_linear)
    return linear_search_times, binary_search_times
def plot_search_performance(array_sizes, linear_times, binary_times):
    max_linear_time = max(linear_times)
    normalized_linear_times = np.array(linear_times) / max_linear_time
    normalized_binary_times = np.array(binary_times) / max_linear_time
    plt.plot(array_sizes, normalized_linear_times, '-o', label='Linear Search')
    plt.plot(array_sizes, normalized_binary_times, '-o', label='Binary Search')
    plt.plot(array_sizes, np.array(array_sizes) / max(array_sizes), '--k', label='Linear')
    plt.plot(array_sizes, np.log2(np.array(array_sizes)) / max(array_sizes), '--k', label='Logarithmic')
    plt.legend()
    plt.xlabel('Array Size')
    plt.ylabel('Normalized Time')
    plt.title('Performance of Linear vs. Binary Search')
    plt.show()
if __name__ == '__main__':
    array_sizes = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    linear_search_times, binary_search_times = run_search_experiments(array_sizes)
    plot_search_performance(array_sizes, linear_search_times, binary_search_times)
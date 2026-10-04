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
def binary_search(arr, start_index=0):
    if len(arr) == 0:
        return start_index
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
def measure_average_time(func, arr, num_iterations=10):
    total_time = 0
    for _ in range(num_iterations):
        wrapped_func = time_wrapper(func, arr)
        total_time += timeit.timeit(wrapped_func, number=num_iterations)
    return total_time / num_iterations
if __name__ == '__main__':
    linear_times = []
    binary_times = []
    sizes = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    for size in sizes:
        arr = np.roll(np.arange(size), np.random.randint(size))
        avg_time_binary = measure_average_time(binary_search, arr)
        avg_time_linear = measure_average_time(linear_search, arr)
        binary_times.append(avg_time_binary)
        linear_times.append(avg_time_linear)
    plt.plot(sizes, np.array(linear_times) / max(linear_times), '-o', label='Linear Search')
    plt.plot(sizes, np.array(binary_times) / max(linear_times), '-o', label='Binary Search')
    plt.plot(sizes, np.array(sizes) / max(sizes), '--k', label='Linear')
    plt.plot(sizes, np.log2(np.array(sizes)) / max(sizes), '--k', label='Logarithmic')
    plt.legend()
    plt.xlabel('Array Size')
    plt.ylabel('Normalized Time')
    plt.title('Search Algorithm Performance')
    plt.show()
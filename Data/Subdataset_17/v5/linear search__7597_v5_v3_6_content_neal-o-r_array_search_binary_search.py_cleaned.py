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
    if len(arr) == 0:
        return start_index
    middle_index = len(arr)
    pivot = arr[middle_index]
    if pivot == arr[0]:
        return start_index + 1
    if pivot < arr[0]:
        return binary_search(arr[:middle_index], start_index)
    else:
        return binary_search(arr[middle_index:], start_index + middle_index)
def measure_time(func, arr, num_iterations=10):
    total_time = timeit.timeit(lambda: func(arr), number=num_iterations)
    return total_time / num_iterations
def main():
    sizes = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    linear_times = []
    binary_times = []
    for size in sizes:
        arr = np.roll(np.arange(size), np.random.randint(size))
        avg_time_linear = measure_time(linear_search, arr)
        avg_time_binary = measure_time(binary_search, arr)
        linear_times.append(avg_time_linear)
        binary_times.append(avg_time_binary)
    max_linear_time = max(linear_times)
    normalized_linear_times = np.array(linear_times) / max_linear_time
    normalized_binary_times = np.array(binary_times) / max_linear_time
    plt.plot(sizes, normalized_linear_times, '-o', label='Linear Search')
    plt.plot(sizes, normalized_binary_times, '-o', label='Binary Search')
    plt.plot(sizes, np.array(sizes) / max(sizes), '--k', label='Linear')
    plt.plot(sizes, np.log2(np.array(sizes)) / max(sizes), '--k', label='Logarithmic')
    plt.xlabel('Array Size')
    plt.ylabel('Normalized Time')
    plt.title('Search Algorithm Performance')
    plt.legend()
    plt.show()
if __name__ == '__main__':
    main()
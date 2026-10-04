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
def binary_search(arr, initial_index=0):
    pivot_index = len(arr)
    pivot = arr[pivot_index]
    if pivot == arr[0]:
        return initial_index + 1
    if pivot < arr[0]:
        return binary_search(arr[:pivot_index], initial_index)
    else:
        return binary_search(arr[pivot_index:], initial_index + pivot_index)
def time_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
def benchmark_searches(ns):
    bins = []
    lins = []
    for n in ns:
        binary_search_time_total = 0
        linear_search_time_total = 0
        for _ in range(100):
            arr = np.roll(np.arange(n), np.random.randint(n))
            t_linear_search = time_wrapper(linear_search, arr)
            t_binary_search = time_wrapper(binary_search, arr)
            num_iterations = 10
            binary_search_time_total += timeit.timeit(t_binary_search, number=num_iterations)
            linear_search_time_total += timeit.timeit(t_linear_search, number=num_iterations)
        bins.append(binary_search_time_total / 100)
        lins.append(linear_search_time_total / 100)
    return bins, lins
def plot_results(ns, lins, bins):
    plt.plot(ns, np.array(lins) / max(lins), '-o', label='Linear Search')
    plt.plot(ns, np.array(bins) / max(lins), '-o', label='Binary Search')
    plt.plot(ns, np.array(ns) / max(ns), '--k', label='Linear')
    plt.plot(ns, np.log2(np.array(ns)) / max(ns), '--k', label='Logarithmic')
    plt.legend()
    plt.xlabel('Array Size (n)')
    plt.ylabel('Normalized Time')
    plt.title('Linear Search vs Binary Search Performance')
    plt.show()
if __name__ == '__main__':
    ns = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    bins, lins = benchmark_searches(ns)
    plot_results(ns, lins, bins)
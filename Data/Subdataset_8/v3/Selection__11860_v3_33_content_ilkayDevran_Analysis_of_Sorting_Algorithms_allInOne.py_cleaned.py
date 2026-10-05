import numpy as np
import matplotlib.pyplot as plt
import selection_sort
import insertion_sort
import merge_sort
import time
def generate_random_list(size):
    return np.random.randint(1, 10000000, size=size)
def measure_sorting_time(sort_func, random_list):
    start_time = time.time()
    sorted_list = sort_func(random_list.copy())
    return time.time() - start_time
def draw_comparison_graph(array_sizes, selection_times, merge_times, insertion_times):
    plt.figure(figsize=(12, 5))
    plt.plot(array_sizes, selection_times, marker='x', c='b', label='Selection Sort')
    plt.plot(array_sizes, merge_times, marker='x', c='r', label='Merge Sort')
    plt.plot(array_sizes, insertion_times, marker='x', c='g', label='Insertion Sort')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Size of Unsorted List (log scale)")
    plt.ylabel("Seconds of Computation (log scale)")
    plt.legend(loc='upper left')
    plt.grid()
    plt.title("Comparison of Selection Sort, Merge Sort, and Insertion Sort")
    plt.show()
def draw_all_graphs():
    array_sizes = [10**i for i in range(1, 5)]
    selection_times = []
    merge_times = []
    insertion_times = []
    for size in array_sizes:
        random_list = generate_random_list(size)
        selection_time = measure_sorting_time(selection_sort.selectionSort, random_list)
        merge_time = measure_sorting_time(merge_sort.mergeSort, random_list)
        insertion_time = measure_sorting_time(insertion_sort.insertionSort, random_list)
        selection_times.append(selection_time)
        merge_times.append(merge_time)
        insertion_times.append(insertion_time)
    draw_comparison_graph(array_sizes, selection_times, merge_times, insertion_times)
if __name__ == "__main__":
    draw_all_graphs()
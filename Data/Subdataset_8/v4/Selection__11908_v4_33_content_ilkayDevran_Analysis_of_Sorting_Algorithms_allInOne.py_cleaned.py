import numpy as np
import matplotlib.pyplot as plt
import selection_sort
import insertion_sort
import MERGE
import time
def draw_all_graph():
    insertion_times = []
    selection_times = []
    merge_times = []
    array_sizes = [10**i for i in range(1, 5)]
    for size in array_sizes:
        random_list = np.random.random_integers(1, 10000000, size=size)
        start_time = time.time()
        sel_list = selection_sort.selectionSort(random_list)
        run_time = time.time() - start_time
        selection_times.append(run_time)
        start_time = time.time()
        merge_list = MERGE.mergeSort(random_list)
        run_time = time.time() - start_time
        merge_times.append(run_time)
        start_time = time.time()
        insertion_list = insertion_sort.insertionSort(random_list)
        run_time = time.time() - start_time
        insertion_times.append(run_time)
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
draw_all_graph()
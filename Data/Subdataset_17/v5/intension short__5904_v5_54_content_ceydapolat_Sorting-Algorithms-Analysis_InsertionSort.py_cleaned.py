import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
times = []
counts = []
timesAve = np.zeros(5)
def insertion_sort(alist):
    count = 1
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        made_swap = False
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1
            count += 1
            made_swap = True
        if not made_swap:
            count += 1
        alist[position] = current_value
    counts.append(count)
def perform_insertion_sort_on_datasets():
    global times
    times.clear()
    for filename in cds.fileNames:
        values = []
        start_time = time.time()
        with open(filename, "r") as reader:
            values = [int(value) for value in reader.readlines()]
        insertion_sort(values)
        end_time = time.time()
        times.append(end_time - start_time)
    cds.generateAverageValues(times, timesAve)
def generate_cases():
    best_case_counts = []
    average_case_counts = []
    worst_case_counts = []
    for i, count in enumerate(counts):
        if i % 9 == 0:
            best_case_counts.append(count)
        elif i % 9 == 4:
            worst_case_counts.append(count)
        elif i % 9 in [1, 2, 3]:
            average_case_counts.append(count)
    averaged_ave_counts = [
        (average_case_counts[i] + average_case_counts[i + 1] + average_case_counts[i + 2]) / 3
        for i in range(0, len(average_case_counts), 3)
    ]
    sizes = [200, 400, 600, 800, 1000]
    plt.plot(sizes, best_case_counts, '-ro')
    plt.plot(sizes, averaged_ave_counts, '-bo')
    plt.plot(sizes, worst_case_counts, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()

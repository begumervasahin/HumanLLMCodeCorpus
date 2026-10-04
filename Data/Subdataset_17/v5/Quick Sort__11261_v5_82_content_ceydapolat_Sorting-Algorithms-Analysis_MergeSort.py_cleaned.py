import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
values = []
times = []
counts = []
times_ave = np.zeros(5)
count = 0
def merge_sort(alist):
    global count
    if len(alist) > 1:
        mid = len(alist)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
            count += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
            count += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
            count += 1
def merge():
    global count
    for filename in cds.fileNames:
        values.clear()
        start_time = time.time()
        with open(filename, "r") as reader:
            values.extend(int(value.strip()) for value in reader.readlines())
        count = 0
        merge_sort(values)
        counts.append(count)
        end_time = time.time()
        times.append(end_time - start_time)
    cds.generateAverageValues(times, times_ave)
def generate_cases():
    arr_best, arr_ave, arr_worst = [], [], []
    for i in range(len(counts)):
        if i % 9 == 0 or i % 9 == 4:
            arr_best.append(counts[i])
        elif i % 9 == 5:
            arr_worst.append(counts[i])
        elif i % 9 in (1, 2, 3):
            arr_ave.append(counts[i])
    arr_best_avg = [(arr_best[i] + arr_best[i + 1]) / 2 for i in range(0, len(arr_best), 2)]
    arr_ave_avg = [(arr_ave[i] + arr_ave[i + 1] + arr_ave[i + 2]) / 3 for i in range(0, len(arr_ave), 3)]
    sizes = [200, 400, 600, 800, 1000]
    plt.plot(sizes, arr_ave_avg, '-bo', label="Average Case")
    plt.plot(sizes, arr_best_avg, '-ro', label="Best Case")
    plt.plot(sizes, arr_worst, '-go', label="Worst Case")
    plt.legend()
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.title("Merge Sort Performance")
    plt.show()
merge()
generate_cases()
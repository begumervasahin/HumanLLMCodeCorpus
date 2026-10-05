import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
values = []
times = []
counts = []
timesAve = np.zeros(5)
count = 0
def merge_sort_recursive(arr):
    global count
    def merge_sort(arr):
        nonlocal count
        if len(arr) > 1:
            mid = len(arr)
            left_half = arr[:mid]
            right_half = arr[mid:]
            merge_sort(left_half)
            merge_sort(right_half)
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
                count += 1
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
                count += 1
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
                count += 1
    for f in cds.fileNames:
        values.clear()
        start = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                values.append(int(value))
        count = 0
        merge_sort(values)
        counts.append(count)
        end = time.time()
        times.append(end - start)
    cds.generateAverageValues(times, timesAve)
def generate_cases():
    global counts
    arr_best = []
    arr_ave = []
    arr_worst = []
    for i in range(len(counts)):
        if i % 9 == 0 or i % 9 == 4:
            arr_best.append(counts[i])
    arr_best2 = []
    for i in range(len(arr_best)):
        x = (arr_best[i] + arr_best[i + 1]) / 2
        i += 1
        if len(arr_best2) >= len(arr_best) / 2:
            break
        arr_best2.append(x)
        x = 0
    for i in range(len(counts)):
        if i % 9 == 5:
            arr_worst.append(counts[i])
    for i in range(len(counts)):
        if i % 9 == 1 or i % 9 == 2 or i % 9 == 3:
            arr_ave.append(counts[i])
    arr_ave2 = []
    for i in range(len(arr_ave)):
        x = (arr_ave[i] + arr_ave[i + 1] + arr_ave[i + 2]) / 3
        i += 2
        if len(arr_ave2) >= len(arr_ave) / 3:
            break
        arr_ave2.append(x)
        x = 0
    sizes = [200, 400, 600, 800, 1000]
    plt.plot(sizes, arr_ave2, '-bo')
    plt.plot(sizes, arr_best2, '-ro')
    plt.plot(sizes, arr_worst, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
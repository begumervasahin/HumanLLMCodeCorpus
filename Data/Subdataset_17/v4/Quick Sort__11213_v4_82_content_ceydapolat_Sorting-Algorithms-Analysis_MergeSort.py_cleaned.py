import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
values = []
times = []
counts = []
timesAve = np.zeros(5)
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
        start = time.time()
        with open(filename, "r") as reader:
            values.extend(int(value) for value in reader.readlines())
        count = 0
        merge_sort(values)
        counts.append(count)
        end = time.time()
        times.append(end - start)
    cds.generateAverageValues(times, timesAve)
def generate_cases():
    global counts
    arrBest, arrAve, arrWorst = [], [], []
    for i in range(len(counts)):
        if i % 9 == 0 or i % 9 == 4:
            arrBest.append(counts[i])
        elif i % 9 == 5:
            arrWorst.append(counts[i])
        elif i % 9 in (1, 2, 3):
            arrAve.append(counts[i])
    arrBest2 = [(arrBest[i] + arrBest[i + 1]) / 2 for i in range(0, len(arrBest), 2)]
    arrAve2 = [(arrAve[i] + arrAve[i + 1] + arrAve[i + 2]) / 3 for i in range(0, len(arrAve), 3)]
    sizes = [200, 400, 600, 800, 1000]
    plt.plot(sizes, arrAve2, '-bo')
    plt.plot(sizes, arrBest2, '-ro')
    plt.plot(sizes, arrWorst, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
merge()
generate_cases()
import matplotlib.pyplot as plt
import numpy as np
import time
values = []
times = []
counts = []
timesAve = np.zeros(5)
count = 0
def mergeSort(alist):
    global count
    if len(alist) > 1:
        mid = len(alist)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
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
def Merge():
    import createDataSets as cds
    for f in cds.fileNames:
        values.clear()
        start = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                values.append(int(value))
        global count
        count = 0
        mergeSort(values)
        counts.append(count)
        end = time.time()
        times.append(end - start)
    cds.generateAverageValues(times, timesAve)
def generateCases():
    global counts
    arrBest = []
    arrAve = []
    arrWorst = []
    for i in range(len(counts)):
        if i % 9 == 0 or i % 9 == 4:
            arrBest.append(counts[i])
    arrBest2 = []
    for i in range(len(arrBest)
        x = (arrBest[2 * i] + arrBest[2 * i + 1]) / 2
        arrBest2.append(x)
    for i in range(len(counts)):
        if i % 9 == 5:
            arrWorst.append(counts[i])
    for i in range(len(counts)):
        if i % 9 == 1 or i % 9 == 2 or i % 9 == 3:
            arrAve.append(counts[i])
    arrAve2 = []
    for i in range(len(arrAve)
        x = (arrAve[3 * i] + arrAve[3 * i + 1] + arrAve[3 * i + 2]) / 3
        arrAve2.append(x)
    sizes = [200, 400, 600, 800, 1000]
    plt.plot(sizes, arrAve2, '-bo')
    plt.plot(sizes, arrBest2, '-ro')
    plt.plot(sizes, arrWorst, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if __name__ == "__main__":
    Merge()
    generateCases()
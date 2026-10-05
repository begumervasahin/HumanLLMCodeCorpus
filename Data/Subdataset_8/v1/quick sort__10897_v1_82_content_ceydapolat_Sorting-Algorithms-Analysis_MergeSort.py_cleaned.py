import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
values = []
times = []
counts = []
timesAve = np.zeros(5)
count = 0
def Merge():
    global counts, values, count
    def mergeSort(alist):
        nonlocal count
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
    for f in cds.fileNames:
        values.clear()
        start = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                values.append(int(value))
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
    for i in range(len(arrBest)):
        x = (arrBest[i] + arrBest[i + 1]) / 2
        i += 1
        if len(arrBest2) >= len(arrBest) / 2:
            break
        arrBest2.append(x)
        x = 0
    for i in range(len(counts)):
        if i % 9 == 5:
            arrWorst.append(counts[i])
    for i in range(len(counts)):
        if i % 9 == 1 or i % 9 == 2 or i % 9 == 3:
            arrAve.append(counts[i])
    arrAve2 = []
    for i in range(len(arrAve)):
        x = (arrAve[i] + arrAve[i + 1] + arrAve[i + 2]) / 3
        i += 2
        if len(arrAve2) >= len(arrAve) / 3:
            break
        arrAve2.append(x)
        x = 0
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
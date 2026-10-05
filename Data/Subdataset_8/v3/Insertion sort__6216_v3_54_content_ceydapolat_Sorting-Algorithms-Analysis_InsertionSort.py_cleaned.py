import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
values = []
times = []
counts = []
timesAve = np.zeros(5)
def insertion_sort(arr):
    count = 1
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index
        swapped = False
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
            count += 1
            swapped = True
        if not swapped:
            count += 1
        arr[position] = current_value
    counts.append(count)
def Insertion():
    for filename in cds.fileNames:
        values.clear()
        start = time.time()
        with open(filename, "r") as reader:
            for line in reader.readlines():
                values.append(int(line))
        insertion_sort(values)
        end = time.time()
        times.append(end - start)
    cds.generateAverageValues(times, timesAve)
def generate_cases():
    global counts
    arr_best = []
    arr_ave = []
    arr_worst = []
    for i, count in enumerate(counts):
        if i % 9 == 0:
            arr_best.append(count)
        if i % 9 == 4:
            arr_worst.append(count)
        if i % 9 in (1, 2, 3):
            arr_ave.append(count)
    arr_ave2 = []
    for i in range(0, len(arr_ave), 3):
        avg = sum(arr_ave[i:i+3]) / 3
        arr_ave2.append(avg)
    sizes = [200, 400, 600, 800, 1000]
    plt.plot(sizes, arr_best, '-ro')
    plt.plot(sizes, arr_ave2, '-bo')
    plt.plot(sizes, arr_worst, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if __name__ == "__main__":
    Insertion()
    generate_cases()
import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
b1 = []
b2 = []
b3 = []
b4 = np.zeros(5)
def fonk1(arr):
    a1 = 1
    for index in range(1, len(arr)):
        b5 = arr[index]
        b6 = index
        a2 = 0
        while b6 > 0 and arr[b6 - 1] > b5:
            arr[b6] = arr[b6 - 1]
            b6 -= 1
            a1 += 1
            a2 = 1
        if a2 = = 0:
            a1 += 1
        arr[b6] = b5
    b3.append(a1)
def fonk2():
    for filename in cds.fileNames:
        b1.clear()
        b7 = time.time()
        with open(filename, "r") as reader:
            b1 = [int(line) for line in reader.readlines()]
        fonk1(b1)
        b8 = time.time()
        b2.append(b8 - b7)
    cds.generateAverageValues(b2, b4)
def fonk3():
    global b3
    arr_best, arr_ave, b9 = [], [], []
    for i, a1 in enumerate(b3):
        if i % b10 = = 0:
            arr_best.append(a1)
        if i % b10 = = 4:
            b9.append(a1)
        if i % b10 in (1, 2, 3):
            arr_ave.append(a1)
    b11 = [sum(arr_ave[i:i+3]) / 3 for i in range(0, len(arr_ave), 3)]
    b12 = [200, 400, 600, 800, 1000]
    plt.plot(b12, arr_best, '-ro')
    plt.plot(b12, b11, '-bo')
    plt.plot(b12, b9, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if b13 = = "__main__":
    fonk2()
    fonk3()
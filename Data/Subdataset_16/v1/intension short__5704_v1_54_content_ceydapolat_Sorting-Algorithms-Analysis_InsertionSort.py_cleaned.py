import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
b1 = []
b2 = []
b3 = np.zeros(5)
def fonk1(alist):
    a1 = 1
    for index in range(1, len(alist)):
        b4 = alist[index]
        b5 = index
        a2 = 0
        while b5 > 0 and alist[b5 - 1] > b4:
            alist[b5] = alist[b5 - 1]
            b5 -= 1
            a1 += 1
            a2 = 1
        if a2 = = 0:
            a1 += 1
        alist[b5] = b4
    b2.append(a1)
def fonk2():
    global b1
    b1.clear()
    for f in cds.fileNames:
        b6 = []
        b7 = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                b6.append(int(value))
        fonk1(b6)
        b8 = time.time()
        b1.append(b8 - b7)
    cds.generateAverageValues(b1, b3)
def fonk3():
    global b2
    arr_best, arr_worst, b9 = [], [], []
    for i in range(len(b2)):
        if i % b10 = = 0:
            arr_best.append(b2[i])
        elif i % b10 = = 4:
            arr_worst.append(b2[i])
        elif i % b10 in [1, 2, 3]:
            b9.append(b2[i])
    b11 = [(b9[i] + b9[i+1] + b9[i+2]) / 3 for i in range(0, len(b9), 3)]
    b12 = [200, 400, 600, 800, 1000]
    plt.plot(b12, arr_best, '-ro')
    plt.plot(b12, b11, '-bo')
    plt.plot(b12, arr_worst, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if b13 = = "__main__":
    fonk2()
    fonk3()
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
        b6 = False
        while b5 > 0 and alist[b5 - 1] > b4:
            alist[b5] = alist[b5 - 1]
            b5 -= 1
            a1 += 1
            b6 = True
        if not b6:
            a1 += 1
        alist[b5] = b4
    b2.append(a1)
def fonk2():
    global b1
    b1.clear()
    for filename in cds.fileNames:
        b7 = []
        b8 = time.time()
        with open(filename, "r") as reader:
            b7 = [int(value) for value in reader.readlines()]
        fonk1(b7)
        b9 = time.time()
        b1.append(b9 - b8)
    cds.generateAverageValues(b1, b3)
def fonk3():
    b10 = []
    b11 = []
    b12 = []
    for i, a1 in enumerate(b2):
        if i % b13 = = 0:
            b10.append(a1)
        elif i % b13 = = 4:
            b12.append(a1)
        elif i % b13 in [1, 2, 3]:
            b11.append(a1)
    b14 = [
        (b11[i] + b11[i + 1] + b11[i + 2]) / 3
        for i in range(0, len(b11), 3)
    ]
    b15 = [200, 400, 600, 800, 1000]
    plt.plot(b15, b10, '-ro')
    plt.plot(b15, b14, '-bo')
    plt.plot(b15, b12, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()

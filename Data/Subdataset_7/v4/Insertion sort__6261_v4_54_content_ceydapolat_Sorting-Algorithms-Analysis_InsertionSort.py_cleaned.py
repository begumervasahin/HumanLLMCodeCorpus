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
            for line in reader.readlines():
                b1.append(int(line))
        fonk1(b1)
        b8 = time.time()
        b2.append(b8 - b7)
    cds.generateAverageValues(b2, b4)
def fonk3():
    global b3
    b9 = []
    b10 = []
    b11 = []
    for i, a1 in enumerate(b3):
        if i % b12 = = 0:
            b9.append(a1)
        if i % b12 = = 4:
            b11.append(a1)
        if i % b12 in (1, 2, 3):
            b10.append(a1)
    b13 = []
    for i in range(0, len(b10), 3):
        b14 = sum(b10[i:i+3]) / 3
        b13.append(b14)
    b15 = [200, 400, 600, 800, 1000]
    plt.plot(b15, b9, '-ro')
    plt.plot(b15, b13, '-bo')
    plt.plot(b15, b11, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if b16 = = "__main__":
    fonk2()
    fonk3()
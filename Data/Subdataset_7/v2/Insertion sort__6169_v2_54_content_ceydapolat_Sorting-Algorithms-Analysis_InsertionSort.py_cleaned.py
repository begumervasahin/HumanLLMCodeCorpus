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
    for f in cds.fileNames:
        b1.clear()
        b7 = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                b1.append(int(value))
        fonk1(b1)
        b8 = time.time()
        b2.append(b8 - b7)
    cds.generateAverageValues(b2, b4)
def fonk3():
    global b3
    b9 = []
    b10 = []
    b11 = []
    for i in range(len(b3)):
        if i % b12 = = 0:
            b9.append(b3[i])
        if i % b12 = = 4:
            b11.append(b3[i])
        if i % b12 = = 1 or i % b12 == 2 or i % b12 == 3:
            b10.append(b3[i])
    b13 = []
    for i in range(len(b10)):
        a2 = (b10[i] + b10[i + 1] + b10[i + 2]) / 3
        i += 2
        if len(b13) >= len(b10) / 3:
            break
        b13.append(a2)
        a2 = 0
    b14 = [200, 400, 600, 800, 1000]
    plt.plot(b14, b9, '-ro')
    plt.plot(b14, b13, '-bo')
    plt.plot(b14, b11, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if b15 = = "__main__":
    fonk2()
    fonk3()
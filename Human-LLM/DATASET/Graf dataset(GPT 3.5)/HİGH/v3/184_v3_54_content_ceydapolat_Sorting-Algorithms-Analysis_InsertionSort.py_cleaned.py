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
        b7 = False
        while b6 > 0 and arr[b6 - 1] > b5:
            arr[b6] = arr[b6 - 1]
            b6 -= 1
            a1 += 1
            b7 = True
        if not b7:
            a1 += 1
        arr[b6] = b5
    b3.append(a1)
def fonk2():
    for filename in cds.fileNames:
        b1.clear()
        b8 = time.time()
        with open(filename, "r") as reader:
            for line in reader.readlines():
                b1.append(int(line))
        fonk1(b1)
        b9 = time.time()
        b2.append(b9 - b8)
    cds.generateAverageValues(b2, b4)
def fonk3():
    global b3
    b10 = []
    b11 = []
    b12 = []
    for i, a1 in enumerate(b3):
        if i % b13 = = 0:
            b10.append(a1)
        if i % b13 = = 4:
            b12.append(a1)
        if i % b13 in (1, 2, 3):
            b11.append(a1)
    b14 = []
    for i in range(0, len(b11), 3):
        b15 = sum(b11[i:i+3]) / 3
        b14.append(b15)
    b16 = [200, 400, 600, 800, 1000]
    plt.plot(b16, b10, '-ro')
    plt.plot(b16, b14, '-bo')
    plt.plot(b16, b12, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if b17 = = "__main__":
    fonk2()
    fonk3()
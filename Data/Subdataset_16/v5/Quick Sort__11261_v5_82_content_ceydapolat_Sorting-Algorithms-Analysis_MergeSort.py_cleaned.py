import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
b1 = []
b2 = []
b3 = []
b4 = np.zeros(5)
a1 = 0
def fonk1(alist):
    global a1
    if len(alist) > 1:
        b5 = len(alist)
        b6 = alist[:b5]
        b7 = alist[b5:]
        fonk1(b6)
        fonk1(b7)
        a2 = 0
        a3 = 0
        a4 = 0
        while a2 < len(b6) and a3 < len(b7):
            if b6[a2] < b7[a3]:
                alist[a4] = b6[a2]
                a2 += 1
            else:
                alist[a4] = b7[a3]
                a3 += 1
            a4 += 1
            a1 += 1
        while a2 < len(b6):
            alist[a4] = b6[a2]
            a2 += 1
            a4 += 1
            a1 += 1
        while a3 < len(b7):
            alist[a4] = b7[a3]
            a3 += 1
            a4 += 1
            a1 += 1
def fonk2():
    global a1
    for filename in cds.fileNames:
        b1.clear()
        b8 = time.time()
        with open(filename, "r") as reader:
            b1.extend(int(value.strip()) for value in reader.readlines())
        a1 = 0
        fonk1(b1)
        b3.append(a1)
        b9 = time.time()
        b2.append(b9 - b8)
    cds.generateAverageValues(b2, b4)
def fonk3():
    arr_best, arr_ave, b10 = [], [], []
    for a2 in range(len(b3)):
        if a2 % b11 = = 0 or a2 % b11 == 4:
            arr_best.append(b3[a2])
        elif a2 % b11 = = 5:
            b10.append(b3[a2])
        elif a2 % b11 in (1, 2, 3):
            arr_ave.append(b3[a2])
    b12 = [(arr_best[a2] + arr_best[a2 + 1]) / 2 for a2 in range(0, len(arr_best), 2)]
    b13 = [(arr_ave[a2] + arr_ave[a2 + 1] + arr_ave[a2 + 2]) / 3 for a2 in range(0, len(arr_ave), 3)]
    b14 = [200, 400, 600, 800, 1000]
    plt.plot(b14, b13, '-bo', b15 = "Average Case")
    plt.plot(b14, b12, '-ro', b15 = "Best Case")
    plt.plot(b14, b10, '-go', b15 = "Worst Case")
    plt.legend()
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.title("Merge Sort Performance")
    plt.show()
fonk2()
fonk3()
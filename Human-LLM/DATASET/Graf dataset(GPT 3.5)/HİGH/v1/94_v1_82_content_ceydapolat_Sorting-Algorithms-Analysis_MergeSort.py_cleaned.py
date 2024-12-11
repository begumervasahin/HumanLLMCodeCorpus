import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
b1 = []
b2 = []
b3 = []
b4 = np.zeros(5)
a1 = 0
def fonk1():
    global b3, b1, a1
    def fonk2(alist):
        nonlocal a1
        if len(alist) > 1:
            b5 = len(alist)
            b6 = alist[:b5]
            b7 = alist[b5:]
            fonk2(b6)
            fonk2(b7)
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
    for f in cds.fileNames:
        b1.clear()
        b8 = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                b1.append(int(value))
        a1 = 0
        fonk2(b1)
        b3.append(a1)
        b9 = time.time()
        b2.append(b9 - b8)
    cds.generateAverageValues(b2, b4)
def fonk3():
    global b3
    b10 = []
    b11 = []
    b12 = []
    for a2 in range(len(b3)):
        if a2 % b13 = = 0 or a2 % b13 == 4:
            b10.append(b3[a2])
    b14 = []
    for a2 in range(len(b10)):
        b15 = (b10[a2] + b10[a2 + 1]) / 2
        a2 += 1
        if len(b14) >= len(b10) / 2:
            break
        b14.append(b15)
        b15 = 0
    for a2 in range(len(b3)):
        if a2 % b13 = = 5:
            b12.append(b3[a2])
    for a2 in range(len(b3)):
        if a2 % b13 = = 1 or a2 % b13 == 2 or a2 % b13 == 3:
            b11.append(b3[a2])
    b16 = []
    for a2 in range(len(b11)):
        b15 = (b11[a2] + b11[a2 + 1] + b11[a2 + 2]) / 3
        a2 += 2
        if len(b16) >= len(b11) / 3:
            break
        b16.append(b15)
        b15 = 0
    b17 = [200, 400, 600, 800, 1000]
    plt.plot(b17, b16, '-bo')
    plt.plot(b17, b14, '-ro')
    plt.plot(b17, b12, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.show()
if b18 = = "__main__":
    fonk1()
    fonk3()
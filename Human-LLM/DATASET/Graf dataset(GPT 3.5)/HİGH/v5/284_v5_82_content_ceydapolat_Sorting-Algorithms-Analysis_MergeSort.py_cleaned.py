import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
b1 = []
b2 = []
b3 = []
b4 = np.zeros(5)
a1 = 0
def fonk1(arr):
    global a1
    def fonk2(arr):
        nonlocal a1
        if len(arr) > 1:
            b5 = len(arr)
            b6 = arr[:b5]
            b7 = arr[b5:]
            fonk2(b6)
            fonk2(b7)
            b8 = j = k = 0
            while b8 < len(b6) and j < len(b7):
                if b6[b8] < b7[j]:
                    arr[k] = b6[b8]
                    b8 += 1
                else:
                    arr[k] = b7[j]
                    j += 1
                k += 1
                a1 += 1
            while b8 < len(b6):
                arr[k] = b6[b8]
                b8 += 1
                k += 1
                a1 += 1
            while j < len(b7):
                arr[k] = b7[j]
                j += 1
                k += 1
                a1 += 1
    for f in cds.fileNames:
        b1.clear()
        b9 = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                b1.append(int(value))
        a1 = 0
        fonk2(b1)
        b3.append(a1)
        b10 = time.time()
        b2.append(b10 - b9)
    cds.generateAverageValues(b2, b4)
def fonk3():
    global b3
    b11 = []
    b12 = []
    b13 = []
    for b8 in range(len(b3)):
        if b8 % b14 = = 0 or b8 % b14 == 4:
            b11.append(b3[b8])
    b15 = []
    for b8 in range(len(b11)):
        b16 = (b11[b8] + b11[b8 + 1]) / 2
        b8 += 1
        if len(b15) >= len(b11) / 2:
            break
        b15.append(b16)
        b16 = 0
    for b8 in range(len(b3)):
        if b8 % b14 = = 5:
            b13.append(b3[b8])
    for b8 in range(len(b3)):
        if b8 % b14 = = 1 or b8 % b14 == 2 or b8 % b14 == 3:
            b12.append(b3[b8])
    b17 = []
    for b8 in range(len(b12)):
        b16 = (b12[b8] + b12[b8 + 1] + b12[b8 + 2]) / 3
        b8 += 2
        if len(b17) >= len(b12) / 3:
            break
        b17.append(b16)
        b16 = 0
    b18 = [200, 400, 600, 800, 1000]
    plt.plot(b18, b17, '-bo')
    plt.plot(b18, b15, '-ro')
    plt.plot(b18, b13, '-go')
    plt.legend(["Best Case", "Average Case", "Worst Case"])
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
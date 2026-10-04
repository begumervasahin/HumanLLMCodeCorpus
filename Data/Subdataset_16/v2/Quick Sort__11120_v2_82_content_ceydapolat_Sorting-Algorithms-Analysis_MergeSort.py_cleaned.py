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
    if len(arr) > 1:
        b5 = len(arr)
        b6 = arr[:b5]
        b7 = arr[b5:]
        fonk1(b6)
        fonk1(b7)
        a2 = 0
        a3 = 0
        a4 = 0
        while a2 < len(b6) and a3 < len(b7):
            if b6[a2] < b7[a3]:
                arr[a4] = b6[a2]
                a2 += 1
            else:
                arr[a4] = b7[a3]
                a3 += 1
            a4 += 1
            a1 += 1
        while a2 < len(b6):
            arr[a4] = b6[a2]
            a2 += 1
            a4 += 1
            a1 += 1
        while a3 < len(b7):
            arr[a4] = b7[a3]
            a3 += 1
            a4 += 1
            a1 += 1
def fonk2():
    import createDataSets as cds
    for file_name in cds.fileNames:
        b1.clear()
        b8 = time.time()
        with open(file_name, "r") as reader:
            for value in reader.readlines():
                b1.append(int(value))
        global a1
        a1 = 0
        fonk1(b1)
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
    b14 = [(b10[2 * a2] + b10[2 * a2 + 1]) / 2 for a2 in range(len(b10)
    for a2 in range(len(b3)):
        if a2 % b13 = = 5:
            b12.append(b3[a2])
    for a2 in range(len(b3)):
        if a2 % b13 = = 1 or a2 % b13 == 2 or a2 % b13 == 3:
            b11.append(b3[a2])
    b15 = [(b11[3 * a2] + b11[3 * a2 + 1] + b11[3 * a2 + 2]) / 3 for a2 in range(len(b11)
    b16 = [200, 400, 600, 800, 1000]
    plt.plot(b16, b15, '-bo', b17 = "Average Case")
    plt.plot(b16, b14, '-ro', b17 = "Best Case")
    plt.plot(b16, b12, '-go', b17 = "Worst Case")
    plt.legend()
    plt.grid()
    plt.xlabel("Sizes")
    plt.ylabel("Counts")
    plt.title("Merge Sort Performance")
    plt.show()
if b18 = = "__main__":
    fonk2()
    fonk3()
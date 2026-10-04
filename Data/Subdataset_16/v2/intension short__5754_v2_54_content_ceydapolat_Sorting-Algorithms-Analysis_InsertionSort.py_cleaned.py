import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time
b1 = []
b2 = []
b3 = np.zeros(5)
def fonk1(numbers):
    a1 = 1
    for i in range(1, len(numbers)):
        b4 = numbers[i]
        b5 = i
        b6 = False
        while b5 > 0 and numbers[b5 - 1] > b4:
            numbers[b5] = numbers[b5 - 1]
            b5 -= 1
            a1 += 1
            b6 = True
        if not b6:
            a1 += 1
        numbers[b5] = b4
    b2.append(a1)
def fonk2():
    global b1
    b1.clear()
    for filename in cds.fileNames:
        b7 = []
        with open(filename, "r") as file:
            b7 = [int(line.strip()) for line in file]
        b8 = time.time()
        fonk1(b7)
        b9 = time.time()
        b1.append(b9 - b8)
    cds.generateAverageValues(b1, b3)
def fonk3():
    b10 = []
    b11 = []
    b12 = []
    for i in range(len(b2)):
        if i % b13 = = 0:
            b10.append(b2[i])
        elif i % b13 = = 4:
            b12.append(b2[i])
        elif i % b13 in [1, 2, 3]:
            b11.append(b2[i])
    b14 = [
        (b11[i] + b11[i+1] + b11[i+2]) / 3
        for i in range(0, len(b11), 3)
    ]
    b15 = [200, 400, 600, 800, 1000]
    plt.plot(b15, b10, '-ro', b16 = "Best Case")
    plt.plot(b15, b14, '-bo', b16 = "Average Case")
    plt.plot(b15, b12, '-go', b16 = "Worst Case")
    plt.xlabel("Input Size")
    plt.ylabel("Operation Count")
    plt.title("Insertion Sort - Best, Average, and Worst Case Scenarios")
    plt.legend()
    plt.grid(True)
    plt.show()
if b17 = = "__main__":
    fonk2()
    fonk3()
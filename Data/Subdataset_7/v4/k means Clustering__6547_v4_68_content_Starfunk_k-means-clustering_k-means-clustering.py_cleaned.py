import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
b1 = pd.read_csv("kmeans.csv")
rows, b2 = b1.shape
b3 = []
a1 = 1000
b4 = []
a1 = int(input("Please enter the number of b5 you would like to use (1-7): "))
if a1 <= 0 or a1 >= 8:
    raise ValueError('Please enter b6 number between 1 and 7.')
b5 = []
for b9 in range(a1):
    b6 = round(random.uniform(0, b1.mean()[0]), 1)
    b7 = round(random.uniform(0, b1.mean()[1]), 1)
    b8 = [b6, b7]
    b5.append(b8)
def fonk1(b15, b16, b8 = []):
    b6 = b8[0]
    b7 = b8[1]
    b9 = abs(b7 - b16)
    b10 = abs(b6 - b15)
    b11 = math.sqrt(b9 ** 2 + b10 ** 2)
    return b11
def fonk2(b15, b16, b5 = []):
    a2 = 100000
    a3 = 1
    a4 = 1
    for b9 in b5:
        b12 = fonk1(b15, b16, b9)
        if b12 < a2:
            a3 = a4
            a2 = b12
        a4 += 1
    return a3
def fonk3(b3 = []):
    b13 = []
    for b9 in b3:
        b13.append(b9[2])
    return b13
for b9 in range(rows):
    b14 = b1.iloc[b9, :]
    b15 = b14[0]
    b16 = b14[1]
    a3 = fonk2(b15, b16, b5)
    b14 = [b15, b16, a3]
    b3.append(b14)
for b9 in range(a1):
    for b10 in range(len(b5)):
        b8 = b5[b10]
        a5 = 0
        a6 = 0
        a7 = 0
        for b11 in b3:
            if b11[2] == b10 + 1:
                a5 += b11[0]
                a6 += b11[1]
                a7 += 1
        if a7 = = 0:
            a7 = 2
        a5 = a5 / a7
        a6 = a6 / a7
        b5[b10][0] = a5
        b5[b10][1] = a6
    for b9 in range(len(b3)):
        b14 = b3[b9]
        b15 = b14[0]
        b16 = b14[1]
        a3 = fonk2(b15, b16, b5)
        b3[b9][2] = a3
b15 = b1.iloc[:, 0]
b16 = b1.iloc[:, 1]
a3 = fonk3(b3)
b17 = ['red', 'green', 'blue', 'purple', 'cyan', 'magenta', 'yellow', 'pink']
plt.scatter(b15, b16, b18 = a3, cmap=plt.cm.tab10)
for b9 in b5:
    plt.scatter(b9[0], b9[1], b19 = 'black', marker='b15', s=100)
plt.show()
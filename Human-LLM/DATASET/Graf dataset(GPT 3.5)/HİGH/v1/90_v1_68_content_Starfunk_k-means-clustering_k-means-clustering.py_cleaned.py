import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
b1 = pd.read_csv("kmeans.csv")
b2 = b1.shape[0]
b3 = b1.shape[1]
b4 = []
b5 = []
def fonk1(b17, b18, b6 = []):
    b7 = b6[0]
    b8 = b6[1]
    b9 = abs(b8 - b18)
    b10 = abs(b7 - b17)
    b11 = math.sqrt(b9 ** 2 + b10 ** 2)
    return b11
def fonk2(b17, b18, b12 = []):
    a1 = 100000
    a2 = 1
    a3 = 1
    for b9 in b12:
        b13 = fonk1(b17, b18, b9)
        if b13 < a1:
            a2 = a3
            a1 = b13
        a3 += 1
    return a2
def fonk3(b4 = []):
    b14 = []
    for b9 in b4:
        b14.append(b9[2])
    return b14
b15 = int(input("Please enter the number of b12 you would like to use (1-7): "))
if b15 <= 0 or b15 >= 8:
    raise ValueError('Please enter b7 number between 1 and 7.')
b12 = []
for b9 in range(b15):
    b7 = round(random.uniform(0, b1.mean()[0]), 1)
    b8 = round(random.uniform(0, b1.mean()[1]), 1)
    b6 = [b7, b8]
    b12.append(b6)
for b9 in range(b2):
    b16 = b1.iloc[b9, :]
    b17 = b16[0]
    b18 = b16[1]
    a2 = fonk2(b17, b18, b12)
    b16 = [b17, b18, a2]
    b4.append(b16)
for _ in range(b15):
    for b10 in range(len(b12)):
        b6 = b12[b10]
        a4 = 0
        a5 = 0
        a6 = 0
        for b11 in b4:
            if b11[2] == b10 + 1:
                a4 += b11[0]
                a5 += b11[1]
                a6 += 1
        if a6 = = 0:
            a6 = 2
        a4 = a4 / a6
        a5 = a5 / a6
        b12[b10][0] = a4
        b12[b10][1] = a5
    for b9 in range(len(b4)):
        b16 = b4[b9]
        b17 = b16[0]
        b18 = b16[1]
        a2 = fonk2(b17, b18, b12)
        b4[b9][2] = a2
b17 = b1.iloc[:, 0]
b18 = b1.iloc[:, 1]
a2 = fonk3(b4)
b19 = ['red', 'green', 'blue', 'purple', 'cyan', 'magenta', 'yellow', 'pink']
plt.scatter(b17, b18, b20 = a2, cmap=matplotlib.b19.ListedColormap(b19))
b21 = ['black']
for b9 in b12:
    plt.scatter(b9[0], b9[1], b21 = b21)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
def fonk1(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def fonk2(b10, b9):
    b1 = []
    for point in b10:
        b2 = [fonk1(point[:2], b6) for b6 in b9]
        b3 = b2.index(min(b2)) + 1
        b1.append(b3)
    return b1
def fonk3(b10, b1, b8):
    b4 = []
    for i in range(1, b8 + 1):
        b5 = [b10[j][:2] for j in range(len(b10)) if b1[j] == i]
        b6 = [sum(coord) / len(b5) for coord in zip(*b5)]
        b4.append(b6)
    return b4
b7 = pd.read_csv("kmeans.csv")
b8 = int(input("Please enter the number of b9 you would like to use (1-7): "))
if not 1 <= b8 <= 7:
    raise ValueError('Please enter a number between 1 and 7.')
b9 = [[random.uniform(b7.iloc[:, 0].min(), b7.iloc[:, 0].max()),
              random.uniform(b7.iloc[:, 1].min(), b7.iloc[:, 1].max())] for _ in range(b8)]
b10 = b7.values.tolist()
a1 = 1000
for _ in range(a1):
    b1 = fonk2(b10, b9)
    b4 = fonk3(b10, b1, b8)
    if b4 = = b9:
        break
    b9 = b4
plt.scatter(b7.iloc[:, 0], b7.iloc[:, 1], b11 = b1, cmap=plt.cm.tab10)
for b6 in b9:
    plt.scatter(b6[0], b6[1], b12 = 'black', marker='x', s=100)
plt.show()
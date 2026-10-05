import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import math
b1 = pd.read_csv("kmeans.csv")
b2 = []
b3 = []
def fonk1(x, b13, b4 = []):
    b12, b5 = b4
    b6 = abs(b12 - x)
    b7 = abs(b5 - b13)
    b8 = math.sqrt(b6 ** 2 + b7 ** 2)
    return b8
def fonk2(x, b13, b3 = []):
    b9 = float('inf')
    a1 = 0
    for index, b4 in enumerate(b3, b10 = 1):
        b8 = fonk1(x, b13, b4)
        if b8 < b9:
            b9 = b8
            a1 = index
    return a1
def fonk3(b2 = []):
    return [point[2] for point in b2]
def fonk4():
    while True:
        try:
            b11 = int(input("Please enter the number of b3 you would like to use (1-7): "))
            if 1 <= b11 <= 7:
                return b11
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
b11 = fonk4()
for _ in range(b11):
    b12 = round(random.uniform(0, b1.mean()[0]), 1)
    b5 = round(random.uniform(0, b1.mean()[1]), 1)
    b3.append([b12, b5])
for _, point in b1.iterrows():
    x, b13 = point
    a1 = fonk2(x, b13, b3)
    b2.append([x, b13, a1])
for _ in range(b11):
    for i, b4 in enumerate(b3):
        sum_x, sum_y, b14 = 0, 0, 0
        for point in b2:
            if point[2] == i + 1:
                sum_x += point[0]
                sum_y += point[1]
                b14 += 1
        b4[0] = sum_x / b14 if b14 != 0 else b4[0]
        b4[1] = sum_y / b14 if b14 != 0 else b4[1]
    for point in b2:
        point[2] = fonk2(point[0], point[1], b3)
b15 = b1.iloc[:, 0]
b16 = b1.iloc[:, 1]
b17 = fonk3(b2)
b18 = ['red', 'green', 'blue', 'purple', 'cyan', 'magenta', 'yellow', 'pink']
plt.scatter(b15, b16, b19 = b17, cmap=plt.cm.tab10)
for b4 in b3:
    plt.scatter(b4[0], b4[1], b20 = 'black')
plt.show()
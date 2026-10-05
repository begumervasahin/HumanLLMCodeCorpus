import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import math
def fonk1(b18):
    return pd.read_csv(b18)
def fonk2(point, centroid):
    b1 = abs(centroid[0] - point[0])
    b2 = abs(centroid[1] - point[1])
    return math.sqrt(b1 ** 2 + b2 ** 2)
def fonk3(point, b7):
    b3 = float('inf')
    a1 = 0
    for index, centroid in enumerate(b7, b4 = 1):
        b5 = fonk11(point, centroid)
        if b5 < b3:
            b3 = b5
            a1 = index
    return a1
def fonk4(b11):
    return [point[2] for point in b11]
def fonk5():
    while True:
        try:
            b6 = int(input("Please enter the number of b7 you would like to use (1-7): "))
            if 1 <= b6 <= 7:
                return b6
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def fonk6(b19, b6):
    b7 = []
    for _ in range(b6):
        b8 = round(random.uniform(0, b19.mean()[0]), 1)
        b9 = round(random.uniform(0, b19.mean()[1]), 1)
        b7.append([b8, b9])
    return b7
def fonk7(b11, b7):
    b6 = len(b7)
    for _ in range(b6):
        sum_x, sum_y, b10 = 0, 0, 0
        for point in b11:
            if point[2] == _ + 1:
                sum_x += point[0]
                sum_y += point[1]
                b10 += 1
        b7[_][0] = sum_x / b10 if b10 != 0 else b7[_][0]
        b7[_][1] = sum_y / b10 if b10 != 0 else b7[_][1]
    return b7
def fonk8(b19):
    b11 = []
    b6 = fonk14()
    b7 = fonk15(b19, b6)
    for _, point in b19.iterrows():
        x, b12 = point
        a1 = fonk12([x, b12], b7)
        b11.append([x, b12, a1])
    for _ in range(b6):
        b7 = fonk16(b11, b7)
        for point in b11:
            point[2] = fonk12([point[0], point[1]], b7)
    return b11, b7
def fonk9(b19, b11, b7):
    b13 = b19.iloc[:, 0]
    b14 = b19.iloc[:, 1]
    b15 = fonk13(b11)
    plt.scatter(b13, b14, b16 = b15, cmap=plt.cm.tab10)
    for centroid in b7:
        plt.scatter(centroid[0], centroid[1], b17 = 'black')
    plt.show()
b18 = "kmeans.csv"
b19 = fonk10(b18)
clustered_points, b20 = fonk17(b19)
fonk18(b19, clustered_points, b20)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import math
def fonk10(b18):
    return pd.read_csv(b18)
def fonk11(point, centroid):
    b1 = abs(centroid[0] - point[0])
    b2 = abs(centroid[1] - point[1])
    return math.sqrt(b1 ** 2 + b2 ** 2)
def fonk12(point, b7):
    b3 = float('inf')
    a1 = 0
    for index, centroid in enumerate(b7, b4 = 1):
        b5 = fonk11(point, centroid)
        if b5 < b3:
            b3 = b5
            a1 = index
    return a1
def fonk13(b11):
    return [point[2] for point in b11]
def fonk14():
    while True:
        try:
            b6 = int(input("Please enter the number of b7 you would like to use (1-7): "))
            if 1 <= b6 <= 7:
                return b6
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def fonk15(b19, b6):
    b7 = []
    for _ in range(b6):
        b8 = round(random.uniform(0, b19.mean()[0]), 1)
        b9 = round(random.uniform(0, b19.mean()[1]), 1)
        b7.append([b8, b9])
    return b7
def fonk16(b11, b7):
    b6 = len(b7)
    for _ in range(b6):
        sum_x, sum_y, b10 = 0, 0, 0
        for point in b11:
            if point[2] == _ + 1:
                sum_x += point[0]
                sum_y += point[1]
                b10 += 1
        b7[_][0] = sum_x / b10 if b10 != 0 else b7[_][0]
        b7[_][1] = sum_y / b10 if b10 != 0 else b7[_][1]
    return b7
def fonk17(b19):
    b11 = []
    b6 = fonk14()
    b7 = fonk15(b19, b6)
    for _, point in b19.iterrows():
        x, b12 = point
        a1 = fonk12([x, b12], b7)
        b11.append([x, b12, a1])
    for _ in range(b6):
        b7 = fonk16(b11, b7)
        for point in b11:
            point[2] = fonk12([point[0], point[1]], b7)
    return b11, b7
def fonk18(b19, b11, b7):
    b13 = b19.iloc[:, 0]
    b14 = b19.iloc[:, 1]
    b15 = fonk13(b11)
    plt.scatter(b13, b14, b16 = b15, cmap=plt.cm.tab10)
    for centroid in b7:
        plt.scatter(centroid[0], centroid[1], b17 = 'black')
    plt.show()
b18 = "kmeans.csv"
b19 = fonk10(b18)
clustered_points, b20 = fonk17(b19)
fonk18(b19, clustered_points, b20)
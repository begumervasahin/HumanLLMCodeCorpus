import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy
import csv
def fonk1(time_str):
    return ((int(time_str[0:2]) * 3600) + (int(time_str[3:5]) * 60) + (int(time_str[6:8]))) / 86400.0
def fonk2(b47, N):
    b1 = {}
    with open(b47, b2 = '') as csvfile:
        b3 = csv.b3(csvfile, delimiter=' ', quotechar='|')
        b4 = None
        a1 = 0
        for row in b3:
            time_str, _, x_str, y_str, b5 = row[0].split(";")
            b6 = fonk1(time_str.split('T')[1][:-4])
            x, b7, b5 = int(x_str)
            if b4 is not None and b5 != b4:
                a1 += 1
                if a1 > N:
                    break
                b1[a1] = []
            if b4 is None or (b6 != prev_time and (x, b7) != b4):
                b1[a1].append([x, b7, b6])
            prev_time, b4 = b6, (x, b7)
    return b1
def fonk3(b1, a1):
    x, b7 = [], []
    for point in b1:
        x.append(point[0])
        b7.append(point[1])
    plt.figure()
    plt.plot(x, b7)
    plt.title('Trajectory ID: ' + str(a1))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
def fonk4(b48, D, P, F):
    print("Partition Phase Begins ...")
    b8 = fonk5(b48)
    print("Partition Done !")
    print("Total Number of t-b8: ", len(b8))
    print("Outlying t-partition Detection Phase Begins ...")
    b8, b9 = fonk6(b48, b8, D, P)
    print("Outlying t-partition Detection Done !")
    print("Number of Outlying t-b8: ", b9, " of ", len(b8))
    print("Outlying Trajectory Detection Phase Begins ...")
    b10 = fonk7(b48, b8, F)
    print("Outlying Trajectory Detection Phase Done !")
    print("Number of Outlying Trajectories: ", len(b10), " of ", len(b48))
    return b10
def fonk5(b48):
    b8 = []
    for a1, points in b48.items():
        for i in range(len(points) - 1):
            b11 = [points[i], points[i + 1]]
            b8.append([b11, a1, 0])
    return b8
def fonk6(b48, b8, D, P):
    b9 = 0
    a4, b12 = fonk8(b48, b8, D)
    for partition in b8:
        b13 = []
        a2 = 0
        for a1, points in b48.items():
            if a1 != partition[1]:
                a3 = 0
                for i in range(len(points) - 1):
                    b11 = [points[i], points[i + 1]]
                    b14 = fonk10(partition[0], b11)
                    b13.append(b14)
                    if b14 < D:
                        a3 += fonk11(b11)
                if a3 > fonk11(partition[0]):
                    a2 += 1
        b15 = (len([d for d in b13 if d <= b12]) + 1) * len(b8)
        if (a2 * a4) / b15 < P * len(b48):
            partition[2] = 1
            b9 += 1
    return b8, b9
def fonk7(b48, b8, F):
    b10 = []
    for a1, points in b48.items():
        b16 = [partition[0] for partition in b8 if partition[2] == 1 and partition[1] == a1]
        outlier_length, b17 = 0, 0
        for b11 in b16:
            outlier_length += fonk11(b11)
        for i in range(len(points) - 1):
            b17 += fonk11([points[i], points[i + 1]])
        if outlier_length / b17 > F:
            b10.append(a1)
    return b10
def fonk8(b48, b8, D):
    b13 = []
    for partition in b8:
        for a1, points in b48.items():
            if a1 != partition[1]:
                for i in range(len(points) - 1):
                    b11 = [points[i], points[i + 1]]
                    b14 = fonk10(partition[0], b11)
                    b13.append(b14)
    b12 = np.std(np.array(b13))
    a4 = 0
    for partition in b8:
        for a1, points in b48.items():
            if a1 != partition[1]:
                for i in range(len(points) - 1):
                    b11 = [points[i], points[i + 1]]
                    b14 = fonk10(partition[0], b11)
                    a4 += (len([d for d in b13 if d <= b12]) + 1)
    return a4, b12
def fonk9(point, line_2pt):
    b18 = line_2pt[2] - line_2pt[0]
    b19 = line_2pt[3] - line_2pt[1]
    b20 = point[0] - line_2pt[0]
    b21 = point[1] - line_2pt[1]
    b22 = (b20 * b18 + b21 * b19) / (b18 * b18 + b19 * b19)
    point[0] = line_2pt[0] + b22 * b18
    point[1] = line_2pt[1] + b22 * b19
    return [point[0], point[1]]
def fonk10(L1, b25):
    w1, w2, w3, b23 = 1.0, 1.0, 1.0, 1.0
    b24 = abs((fonk11(L1) / L1[0][2]) - (fonk11(b25) / b25[0][2]))
    if fonk11(L1) > fonk11(b25):
        L1, b25 = b25, L1
    b26 = [b25[0][0], b25[0][1]]
    b27 = [L1[0][0], L1[0][1], L1[1][0], L1[1][1]]
    b28 = fonk9(b26, b27)
    b29 = [L1[0][0], L1[0][1]]
    b30 = [b25[0][0], b25[0][1], b25[1][0], b25[1][1]]
    b31 = fonk9(b29, b30)
    six, siy, eix, b32 = L1[0][0], L1[0][1], L1[1][0], L1[1][1]
    sjx, sjy, ejx, b33 = b25[0][0], b25[0][1], b25[1][0], b25[1][1]
    b34 = np.linalg.norm([sjy - b28[1], sjx - b28[0]])
    b35 = np.linalg.norm([siy - b31[1], six - b31[0]])
    b36 = (math.pow(b34, 2) + math.pow(b35, 2)) / (b34 + b35)
    b37 = min(np.linalg.norm([siy - b28[1], six - b28[0]]), np.linalg.norm([b32 - b28[1], eix - b28[0]]))
    b38 = min(np.linalg.norm([siy - b31[1], six - b31[0]]), np.linalg.norm([b32 - b31[1], eix - eix - b28[0]]))
    b39 = min(b37, b38)
    x1, b40 = ejx - sjx, b33 - sjy
    x2, b41 = eix - six, b32 - siy
    b42 = x1 * x2 + b40 * b41
    b43 = b42 / (np.linalg.norm([x1, b40]) * np.linalg.norm([x2, b41]))
    if b43 < -1:
        b43 = -1
    elif b43 > 1:
        b43 = 1
    b44 = math.acos(b43)
    if b44 < (math.pi / 2):
        b45 = math.sin(b44) * fonk11(b25)
    else:
        b45 = fonk11(b25)
    return w1 * b36 + w2 * b39 + w3 * b45 + b23 * b24
def fonk11(b11):
    sx, sy, ex, b46 = b11[0][0], b11[0][1], b11[1][0], b11[1][1]
    return np.linalg.norm([ex - sx, b46 - sy])
b47 = 'data/csv/al_position2013-02-06.csv'
b48 = fonk2(b47, 10)
b10 = fonk4(b48, 37, 0.01, 0.4)
print("Outliers: ", b10)
for a1, points in b48.items():
    fonk3(points, a1)
import numpy as np
import math
import matplotlib.pyplot as plt
import csv
def fonk1(time_str):
    return ((int(time_str[0:2]) * 3600) + (int(time_str[3:5]) * 60) + (int(time_str[6:8]))) / 86400.0
def fonk2(b49, a5):
    b1 = {}
    with open(b49, b2 = '') as csvfile:
        b3 = csv.b3(csvfile, delimiter=' ', quotechar='|')
        b4 = None
        a1 = 0
        for row in b3:
            time_str, _, x_str, y_str, b5 = row[0].split(";")
            b6 = fonk1(time_str.split('T')[1][:-4])
            b7, b8, b5 = int(x_str)
            if b4 is not None and b5 != b4:
                a1 += 1
                if a1 > a5:
                    break
                b1[a1] = []
            if b4 is None or (b6 != prev_time and (b7, b8) != b4):
                b1[a1].append([b7, b8, b6])
            prev_time, b4 = b6, (b7, b8)
    return b1
def fonk3(trajectory, a1):
    b7 = [point[0] for point in trajectory]
    b8 = [point[1] for point in trajectory]
    plt.figure()
    plt.plot(b7, b8)
    plt.title('Trajectory ID: ' + str(a1))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
def fonk4(b1, a6, a7, a8):
    print("Partition Phase Begins ...")
    b9 = fonk5(b1)
    print("Partition Done !")
    print("Total Number of t-b9: ", len(b9))
    print("Outlying t-partition Detection Phase Begins ...")
    b9, b10 = fonk6(b1, b9, a6, a7)
    print("Outlying t-partition Detection Done !")
    print("Number of Outlying t-b9: ", b10, " of ", len(b9))
    print("Outlying Trajectory Detection Phase Begins ...")
    b11 = fonk7(b1, b9, a8)
    print("Outlying Trajectory Detection Phase Done !")
    print("Number of Outlying Trajectories: ", len(b11), " of ", len(b1))
    return b11
def fonk5(b1):
    b9 = []
    for a1, points in b1.items():
        for i in range(len(points) - 1):
            b12 = [points[i], points[i + 1]]
            b9.append([b12, a1, 0])
    return b9
def fonk6(b1, b9, a6, a7):
    b10 = 0
    a4, b13 = fonk8(b1, b9, a6)
    for partition in b9:
        b14 = []
        a2 = 0
        for a1, points in b1.items():
            if a1 != partition[1]:
                a3 = 0
                for i in range(len(points) - 1):
                    b12 = [points[i], points[i + 1]]
                    b15 = fonk10(partition[0], b12)
                    b14.append(b15)
                    if b15 < a6:
                        a3 += fonk11(b12)
                if a3 > fonk11(partition[0]):
                    a2 += 1
        b16 = (len([d for d in b14 if d <= b13]) + 1) * len(b9)
        if (a2 * a4) / b16 < a7 * len(b1):
            partition[2] = 1
            b10 += 1
    return b9, b10
def fonk7(b1, b9, a8):
    b11 = []
    for a1, points in b1.items():
        b17 = [partition[0] for partition in b9 if partition[2] == 1 and partition[1] == a1]
        outlier_length, b18 = 0, 0
        for b12 in b17:
            outlier_length += fonk11(b12)
        for i in range(len(points) - 1):
            b18 += fonk11([points[i], points[i + 1]])
        if outlier_length / b18 > a8:
            b11.append(a1)
    return b11
def fonk8(b1, b9, a6):
    b14 = []
    for partition in b9:
        for a1, points in b1.items():
            if a1 != partition[1]:
                for i in range(len(points) - 1):
                    b12 = [points[i], points[i + 1]]
                    b15 = fonk10(partition[0], b12)
                    b14.append(b15)
    b13 = np.std(np.array(b14))
    a4 = 0
    for partition in b9:
        for a1, points in b1.items():
            if a1 != partition[1]:
                for i in range(len(points) - 1):
                    b12 = [points[i], points[i + 1]]
                    b15 = fonk10(partition[0], b12)
                    a4 += (len([d for d in b14 if d <= b13]) + 1)
    return a4, b13
def fonk9(point, line_2pt):
    b19 = line_2pt[2] - line_2pt[0]
    b20 = line_2pt[3] - line_2pt[1]
    b21 = point[0] - line_2pt[0]
    b22 = point[1] - line_2pt[1]
    b23 = (b21 * b19 + b22 * b20) / (b19 * b19 + b20 * b20)
    point[0] = line_2pt[0] + b23 * b19
    point[1] = line_2pt[1] + b23 * b20
    return [point[0], point[1]]
def fonk10(L1, b26):
    w1, w2, w3, b24 = 1.0, 1.0, 1.0, 1.0
    b25 = abs((fonk11(L1) / L1[0][2]) - (fonk11(b26) / b26[0][2]))
    if fonk11(L1) > fonk11(b26):
        L1, b26 = b26, L1
    b27 = [b26[0][0], b26[0][1]]
    b28 = [L1[0][0], L1[0][1], L1[1][0], L1[1][1]]
    b29 = fonk9(b27, b28)
    b30 = [L1[0][0], L1[0][1]]
    b31 = [b26[0][0], b26[0][1], b26[1][0], b26[1][1]]
    b32 = fonk9(b30, b31)
    six, siy, eix, b33 = L1[0][0], L1[0][1], L1[1][0], L1[1][1]
    sjx, sjy, ejx, b34 = b26[0][0], b26[0][1], b26[1][0], b26[1][1]
    b35 = np.linalg.norm([sjy - b29[1], sjx - b29[0]])
    b36 = np.linalg.norm([siy - b32[1], six - b32[0]])
    b37 = (math.pow(b35, 2) + math.pow(b36, 2)) / (b35 + b36)
    b38 = min(np.linalg.norm([siy - b29[1], six - b29[0]]), np.linalg.norm([b33 - b29[1], eix - b29[0]]))
    b39 = min(np.linalg.norm([siy - b32[1], six - b32[0]]), np.linalg.norm([b33 - b32[1], eix - eix - b29[0]]))
    b40 = min(b38, b39)
    x1, b41 = ejx - sjx, b34 - sjy
    x2, b42 = eix - six, b33 - siy
    b43 = x1 * x2 + b41 * b42
    b44 = b43 / (np.linalg.norm([x1, b41]) * np.linalg.norm([x2, b42]))
    if b44 < -1:
        b44 = -1
    elif b44 > 1:
        b44 = 1
    b45 = math.acos(b44)
    if b45 < (math.pi / 2):
        b46 = math.sin(b45) * fonk11(b26)
    else:
        b46 = fonk11(b26)
    return w1 * b37 + w2 * b40 + w3 * b46 + b24 * b25
def fonk11(b12):
    sx, sy, ex, b47 = b12[0][0], b12[0][1], b12[1][0], b12[1][1]
    return np.linalg.norm([ex - sx, b47 - sy])
if b48 = = "__main__":
    b49 = 'data/csv/al_position2013-02-06.csv'
    a5 = 10
    a6 = 37
    a7 = 0.01
    a8 = 0.4
    b1 = fonk2(b49, a5)
    b11 = fonk4(b1, a6, a7, a8)
    print("Outliers: ", b11)
    for a1, points in b1.items():
        fonk3(points, a1)
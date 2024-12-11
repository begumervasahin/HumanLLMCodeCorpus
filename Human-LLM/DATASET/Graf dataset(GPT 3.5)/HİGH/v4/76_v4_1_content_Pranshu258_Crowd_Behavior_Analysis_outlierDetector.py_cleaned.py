import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
import csv
def fonk1(b50):
    b1 = np.b1(np.array(b50))
    print("Mean Distance: ", np.mean(np.array(b50)))
    print("Minimum Distance: ", np.min(np.array(b50)))
    print("Maximum Distance: ", np.max(np.array(b50)))
    print("Standard Deviation of Distances: ", b1)
    return b1
def fonk2(point, line_2pt):
    b2 = [1, 1, 1, 1]
    b2[0] = line_2pt[0]
    b2[1] = line_2pt[1]
    b2[2] = line_2pt[2] - line_2pt[0]
    b2[3] = line_2pt[3] - line_2pt[1]
    b3 = b2[2]
    b4 = b2[3]
    b5 = point[0] - b2[0]
    b6 = point[1] - b2[1]
    b7 = (b5 * b3 + b6 * b4) / (b3 * b3 + b4 * b4)
    point[0] = b2[0] + b7 * b3
    point[1] = b2[1] + b7 * b4
    return [point[0], point[1]]
def fonk3(b12, b11):
    w1, w2, w3, b8 = 1.0, 1.0, 1.0, 1.0
    b9 = abs((fonk4(b12) / b12[0][2]) - (fonk4(b11) / b11[0][2]))
    if fonk4(b12) > fonk4(b11):
        b10 = deepcopy(b11)
        b11 = deepcopy(b12)
        b12 = deepcopy(b10)
    b13 = [b11[0][0], b11[0][1]]
    b14 = [b12[0][0], b12[0][1], b12[1][0], b12[1][1]]
    b15 = fonk2(b13, b14)
    b16 = [b12[0][0], b12[0][1]]
    b17 = [b11[0][0], b11[0][1], b11[1][0], b11[1][1]]
    b18 = fonk2(b16, b17)
    six, siy, eix, b19 = b12[0][0], b12[0][1], b12[1][0], b12[1][1]
    sjx, sjy, ejx, b20 = b11[0][0], b11[0][1], b11[1][0], b11[1][1]
    b21 = np.linalg.norm([sjy - b15[1], sjx - b15[0]])
    b22 = np.linalg.norm([siy - b18[1], six - b18[0]])
    b23 = (math.pow(b21, 2) + math.pow(b22, 2)) / (b21 + b22)
    b24 = min(np.linalg.norm([siy - b15[1], six - b15[0]]),
                np.linalg.norm([b19 - b15[1], eix - b15[0]]))
    b25 = min(np.linalg.norm([siy - b18[1], six - b18[0]]),
                np.linalg.norm([b19 - b18[1], eix - b15[0]]))
    b26 = min(b24, b25)
    b27 = ejx - sjx
    b28 = b20 - sjy
    b29 = eix - six
    b30 = b19 - siy
    b31 = b27 * b29 + b28 * b30
    b32 = b31 / (np.linalg.norm([b27, b28]) * np.linalg.norm([b29, b30]))
    if b32 < -1:
        b32 = -1
    elif b32 > 1:
        b32 = 1
    b33 = math.acos(b32)
    if b33 < (math.pi / 2):
        b34 = math.sin(b33) * fonk4(b11)
    else:
        b34 = fonk4(b11)
    return w1 * b23 + w2 * b26 + w3 * b34 + b8 * b9
def fonk4(b49):
    sx, sy, ex, b35 = b49[0][0], b49[0][1], b49[1][0], b49[1][1]
    return np.linalg.norm([ex - sx, b35 - sy])
def fonk5(b63, s, e):
    a1 = 2
    b36 = fonk4([b63[s], b63[e]])
    b27, b28, b29, b30 = b63[s][0], b63[s][1], b63[e][0], b63[e][1]
    Dx, b37 = b29 - b27, b30 - b28
    b38 = np.linalg.norm([Dx, b37])
    a2 = 0
    for i in range(s, e):
        x0, b39 = b63[i][0], b63[i][1]
        b40 = math.fabs((b37 * x0 - Dx * b39 + b29 * b28 - b30 * b27) / b38)
        a2 = a2 + b40
    b41 = a2 / a1
    b42 = b36 + b41
    return b42
def fonk6(b63, s, e):
    a3 = 0
    for i in range(s, e):
        a3 = a3 + fonk4([b63[i], b63[i + 1]])
    return a3
def fonk7(b63):
    b43 = [b63[0]]
    si, b44 = 1, 1
    while si + b44 <= len(b63):
        b45 = si + b44
        b46 = fonk5(b63, si, b45)
        b47 = fonk6(b63, si, b45)
        if b46 > b47:
            b43.append(b63[b45 - 1])
            si, b44 = b45 - 1, 1
        else:
            b44 = b44 + 1
    b43.append(b63[-1])
def fonk8(b66):
    b48 = []
    for p in b66:
        for i in range(len(b66[p]) - 1):
            b49 = [b66[p][i], b66[p][i + 1]]
            b48.append([b49, p, 0])
    return b48
def fonk9(b66, b48, b38):
    b50 = []
    for Li in b48:
        a4 = 0
        for p in b66:
            if p != Li[1]:
                a5 = 0
                for i in range(len(b66[p]) - 1):
                    b49 = [b66[p][i], b66[p][i + 1]]
                    b51 = fonk3(Li[0], b49)
                    if not math.isnan(b51):
                        b50.append(b51)
    b52 = fonk1(b50)
    a6 = 0
    for Li in b48:
        b50 = []
        for p in b66:
            if p != Li[1]:
                for i in range(len(b66[p]) - 1):
                    b49 = [b66[p][i], b66[p][i + 1]]
                    b51 = fonk3(Li[0], b49)
                    b50.append(b51)
                a6 = a6 + (len([a2 for a2 in b50 if a2 <= b52]) + 1)
    return a6, b52
def fonk10(b66, b48, b38, a9):
    a7 = 0
    a8 = 0
    totaldensity, b52 = fonk9(b66, b48, b38)
    for Li in b48:
        b50 = []
        a4 = 0
        for p in b66:
            if p != Li[1]:
                a5 = 0
                for i in range(len(b66[p]) - 1):
                    b49 = [b66[p][i], b66[p][i + 1]]
                    b51 = fonk3(Li[0], b49)
                    b50.append(b51)
                    if b51 < b38:
                        a5 = a5 + fonk4(b49)
                if a5 > fonk4(Li[0]):
                    a4 = a4 + 1
        b53 = (len([a2 for a2 in b50 if a2 <= b52]) + 1) * len(b48)
        if (a4 * totaldensity) / b53 < a9 * len(b66):
            Li[2] = 1
            a7 += 1
        a8 = a8 + 1
    return b48, a7
def fonk11(b66, b48, F):
    b54 = []
    for p in b66:
        b55 = [Li[0] for Li in b48 if (Li[2] == 1 and Li[1] == p)]
        b56, a3 = 0, 0
        for seg in b55:
            b56 = b56 + fonk4(seg)
        for i in range(len(b66[p]) - 1):
            b49 = [b66[p][i], b66[p][i + 1]]
            a3 = a3 + fonk4(b49)
        if b56 / a3 > F:
            b54.append(p)
    return b54
def fonk12(b66, b38, a9, F):
    print("Partition Phase Begins ...")
    b48 = fonk8(b66)
    print("Partition Done !")
    print("Total Number of b63-partitions: ", len(b48))
    print("Outlying b63-partition Detection Phase Begins ...")
    b48, a7 = fonk10(b66, b48, b38, a9)
    print("Outlying b63-partition Detection Done !")
    print("Number of Outlying b63-partitions: ", a7, " of ", len(b48))
    print("Outlying Trajectory Detection Phase Begins ...")
    b54 = fonk11(b66, b48, F)
    print("Outlying Trajectory Detection Phase Done !")
    print("Number of Outlying Trajectories: ", len(b54), " of ", len(b66))
    return b54
def fonk13(tr):
    return ((int(tr[0:2]) * 3600) + (int(tr[3:5]) * 60) + (int(tr[6:8]))) / 86400.0
def fonk14(b65, N):
    b57 = {}
    b58 = open(b65, newline='')
    b59 = csv.reader(b58, delimiter=' ', quotechar='|')
    t1, m1, b27, b28, b60 = -1, '', -1, -1, -1
    a9 = 0
    for row in b59:
        b61 = ', '.join(row).split(";")
        t2, m2, b29, b30, b62 = fonk13((b61[0].split('b66')[1])[:-4]), b61[1], int(int(b61[2]) / 67), int(int(b61[3]) / 67), int(
            b61[4])
        if (b60 = = b62 and t1 != t2):
            if b57[a9][len(b57[a9]) - 1][0] != b29 or b57[a9][len(b57[a9]) - 1][1] != b30:
                b57[a9].append([b29, b30, t2])
        if b60 != b62:
            a9 = a9 + 1
            if not a9 <= N:
                break
            b57[a9] = [[b29, b30, t2]]
        t1, m1, b60, b27, b28 = t2, m2, b62, b29, b30
    return b57
def fonk15(traj, p):
    x, y, b63 = [], [], []
    for point in traj:
        x.append(point[0])
        y.append(point[1])
    b64 = plt.figure()
    plt.plot(x, y)
    b64.suptitle('TRAJECTORY ID: ' + str(p))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    b64.savefig('Results/' + str(p) + '.png')
b65 = 'b59/csv/al_position2013-02-06.csv'
b66 = fonk14(b65, 10)
b67 = fonk12(b66, 37, 0.01, 0.4)
print("Outliers: ", b67)
for p in b66:
    fonk15(b66[p], p)
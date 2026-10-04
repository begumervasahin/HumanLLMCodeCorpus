import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
def fonk1(b42):
    b1 = np.array(b42)
    b2 = np.b2(b1)
    print("Mean Distance: ", np.mean(b1))
    print("Minimum Distance: ", np.min(b1))
    print("Maximum Distance: ", np.max(b1))
    print("Standard Deviation of Distances: ", b2)
    return b2
def fonk2(point, line_2pt):
    b3 = [1, 1, 1, 1]
    b3[0], b3[1], b3[2], b3[3] = line_2pt[0], line_2pt[1], line_2pt[2] - line_2pt[0], line_2pt[3] - line_2pt[1]
    vx, b4 = b3[2], b3[3]
    dx, b5 = point[0] - b3[0], point[1] - b3[1]
    b6 = (dx * vx + b5 * b4) / (vx * vx + b4 * b4)
    point[0], point[1] = b3[0] + b6 * vx, b3[1] + b6 * b4
    return [point[0], point[1]]
def fonk3(L1, b9):
    w1, w2, w3, b7 = 1.0, 1.0, 1.0, 1.0
    b8 = abs((fonk4(L1) / L1[0][2]) - (fonk4(b9) / b9[0][2]))
    if fonk4(L1) > fonk4(b9):
        L1, b9 = deepcopy(b9), deepcopy(L1)
    b10 = [b9[0][0], b9[0][1]]
    b11 = [L1[0][0], L1[0][1], L1[1][0], L1[1][1]]
    b12 = fonk2(b10, b11)
    b13 = [L1[0][0], L1[0][1]]
    b14 = [b9[0][0], b9[0][1], b9[1][0], b9[1][1]]
    b15 = fonk2(b13, b14)
    six, siy, eix, b16 = L1[0][0], L1[0][1], L1[1][0], L1[1][1]
    sjx, sjy, ejx, b17 = b9[0][0], b9[0][1], b9[1][0], b9[1][1]
    b18 = np.linalg.norm([sjy - b12[1], sjx - b12[0]])
    b19 = np.linalg.norm([siy - b15[1], six - b15[0]])
    b20 = (math.pow(b18, 2) + math.pow(b19, 2)) / (b18 + b19)
    b21 = min(np.linalg.norm([siy - b12[1], six - b12[0]]), np.linalg.norm([b16 - b12[1], eix - b12[0]]))
    b22 = min(np.linalg.norm([siy - b15[1], six - b15[0]]), np.linalg.norm([b16 - b15[1], eix - b12[0]]))
    b23 = min(b21, b22)
    x1, b56, x2, b24 = ejx - sjx, b17 - sjy, eix - six, b16 - siy
    b25 = x1 * x2 + b56 * b24
    b26 = b25 / (np.linalg.norm([x1, b56]) * np.linalg.norm([x2, b24]))
    b26 = min(1, max(-1, b26))
    b27 = math.acos(b26)
    b28 = math.sin(b27) * fonk4(b9) if b27 < (math.pi / 2) else fonk4(b9)
    return w1 * b20 + w2 * b23 + w3 * b28 + b7 * b8
def fonk4(b41):
    sx, sy, ex, b29 = b41[0][0], b41[0][1], b41[1][0], b41[1][1]
    return np.linalg.norm([ex - sx, b29 - sy])
def fonk5(t, s, e):
    a1 = 2
    b30 = fonk4([t[s], t[e]])
    x1, b56, x2, b24 = t[s][0], t[s][1], t[e][0], t[e][1]
    Dx, b31 = x2 - x1, b24 - b56
    b32 = np.linalg.norm([Dx, b31])
    b33 = sum(math.fabs((b31 * t[i][0] - Dx * t[i][1] + x2 * b56 - b24 * x1) / b32) for i in range(s, e))
    b34 = b33 / a1
    return b30 + b34
def fonk6(t, s, e):
    return sum(fonk4([t[i], t[i + 1]]) for i in range(s, e))
def fonk7(t):
    b35 = [t[0]]
    si, b36 = 1, 1
    while si + b36 <= len(t):
        b37 = si + b36
        b38 = fonk5(t, si, b37)
        b39 = fonk6(t, si, b37)
        if b38 > b39:
            b35.append(t[b37 - 1])
            si, b36 = b37 - 1, 1
        else:
            b36 += 1
    b35.append(t[-1])
    return b35
def fonk8(b60):
    b40 = []
    for p in b60:
        for i in range(len(b60[p]) - 1):
            b41 = [b60[p][i], b60[p][i + 1]]
            b40.append([b41, p, 0])
    return b40
def fonk9(b60, b40, b32):
    b42 = []
    for Li in b40:
        for p in b60:
            if p != Li[1]:
                for i in range(len(b60[p]) - 1):
                    b41 = [b60[p][i], b60[p][i + 1]]
                    b43 = fonk3(Li[0], b41)
                    if not math.isnan(b43):
                        b42.append(b43)
    b44 = fonk1(b42)
    a2 = 0
    for Li in b40:
        b42 = []
        for p in b60:
            if p != Li[1]:
                for i in range(len(b60[p]) - 1):
                    b41 = [b60[p][i], b60[p][i + 1]]
                    b43 = fonk3(Li[0], b41)
                    b42.append(b43)
                a2 += (len([b33 for b33 in b42 if b33 <= b44]) + 1)
    return a2, b44
def fonk10(b60, b40, b32, P):
    a3 = 0
    totaldensity, b44 = fonk9(b60, b40, b32)
    for Li in b40:
        b42 = []
        a4 = 0
        for p in b60:
            if p != Li[1]:
                a5 = 0
                for i in range(len(b60[p]) - 1):
                    b41 = [b60[p][i], b60[p][i + 1]]
                    b43 = fonk3(Li[0], b41)
                    b42.append(b43)
                    if b43 < b32:
                        a5 += fonk4(b41)
                if a5 > fonk4(Li[0]):
                    a4 += 1
        b45 = (len([b33 for b33 in b42 if b33 <= b44]) + 1) * len(b40)
        if (a4 * totaldensity) / b45 < P * len(b60):
            Li[2] = 1
            a3 += 1
    return b40, a3
def fonk11(b60, b40, F):
    b46 = []
    for p in b60:
        b47 = [Li[0] for Li in b40 if (Li[2] == 1 and Li[1] == p)]
        b48 = sum(fonk4(seg) for seg in b47)
        b49 = sum(fonk4([b60[p][i], b60[p][i + 1]]) for i in range(len(b60[p]) - 1))
        if b48 / b49 > F:
            b46.append(p)
    return b46
def fonk12(b60, b32, P, F):
    print("Partition Phase Begins ...")
    b40 = fonk8(b60)
    print("Partition Done!")
    print("Total Number of t-partitions: ", len(b40))
    print("Outlying t-partition Detection Phase Begins ...")
    b40, a3 = fonk10(b60, b40, b32, P)
    print("Outlying t-partition Detection Done!")
    print("Number of Outlying t-partitions: ", a3, " of ", len(b40))
    print("Outlying Trajectory Detection Phase Begins ...")
    b46 = fonk11(b60, b40, F)
    print("Outlying Trajectory Detection Phase Done!")
    print("Number of Outlying Trajectories: ", len(b46), " of ", len(b60))
    return b46
def fonk13(tr):
    return ((int(tr[0:2]) * 3600) + (int(tr[3:5]) * 60) + (int(tr[6:8]))) / 86400.0
def fonk14(b59, N):
    b50 = {}
    with open(b59, b51 = '') as csvfile:
        b52 = csv.reader(csvfile, delimiter=' ', quotechar='|')
        P, t1, m1, x1, b56, b53 = 0, -1, '', -1, -1, -1
        for row in b52:
            b54 = ', '.join(row).split(";")
            t2, m2, x2, b24, b55 = fonk13((b54[0].split('b60')[1])[:-4]), b54[1], int(int(b54[2]) / 67), int(int(b54[3]) / 67), int(b54[4])
            if b53 = = b55 and t1 != t2:
                if b50[P][len(b50[P]) - 1][0] != x2 or b50[P][len(b50[P]) - 1][1] != b24:
                    b50[P].append([x2, b24, t2])
            if b53 != b55:
                P += 1
                if not P <= N:
                    break
                b50[P] = [[x2, b24, t2]]
            t1, m1, b53, x1, b56 = t2, m2, b55, x2, b24
    return b50
def fonk15(traj, p):
    x, b57 = zip(*[(point[0], point[1]) for point in traj])
    b58 = plt.figure()
    plt.plot(x, b57)
    b58.suptitle('TRAJECTORY ID: ' + str(p))
    plt.xlabel('x')
    plt.ylabel('b57')
    plt.show()
    b58.savefig('Results/' + str(p) + '.png')
b59 = 'b52/csv/al_position2013-02-06.csv'
b60 = fonk14(b59, 10)
b61 = fonk12(b60, 37, 0.01, 0.4)
print("Outliers: ", b61)
for p in b60:
    fonk15(b60[p], p)
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
import csv
def fonk1(b32):
    b1 = np.b1(np.array(b32))
    print("Mean Distance: ", np.mean(np.array(b32)))
    print("Minimum Distance: ", np.min(np.array(b32)))
    print("Maximum Distance: ", np.max(np.array(b32)))
    print("Standard Deviation of Distances: ", b1)
    return b1
def fonk2(point, line_2pt):
    b2 = [1, 1, 1, 1]
    b2[0] = line_2pt[0]
    b2[1] = line_2pt[1]
    b2[2] = line_2pt[2] - line_2pt[0]
    b2[3] = line_2pt[3] - line_2pt[1]
    vx, b3 = b2[2], b2[3]
    dx, b4 = point[0] - b2[0], point[1] - b2[1]
    b5 = (dx * vx + b4 * b3) / (vx * vx + b3 * b3)
    point[0] = b2[0] + b5 * vx
    point[1] = b2[1] + b5 * b3
    return [point[0], point[1]]
def fonk3(L1, b8):
    w1, w2, w3, b6 = 1.0, 1.0, 1.0, 1.0
    b7 = abs((fonk4(L1) / L1[0][2]) - (fonk4(b8) / b8[0][2]))
    if fonk4(L1) > fonk4(b8):
        L1, b8 = deepcopy(b8), deepcopy(L1)
    point1, b9 = [b8[0][0], b8[0][1]], [L1[0][0], L1[0][1]]
    line_2pt1, b10 = [L1[0][0], L1[0][1], L1[1][0], L1[1][1]], [b8[0][0], b8[0][1], b8[1][0], b8[1][1]]
    proj1, b11 = fonk2(point1, line_2pt1), fonk2(b9, b10)
    six, siy, eix, b12 = L1[0][0], L1[0][1], L1[1][0], L1[1][1]
    sjx, sjy, ejx, b13 = b8[0][0], b8[0][1], b8[1][0], b8[1][1]
    lper1, b14 = np.linalg.norm([sjy - proj1[1], sjx - proj1[0]]), np.linalg.norm([siy - b11[1], six - b11[0]])
    b15 = (math.pow(lper1, 2) + math.pow(b14, 2)) / (lper1 + b14)
    b16 = min(np.linalg.norm([siy - proj1[1], six - proj1[0]]), np.linalg.norm([b12 - proj1[1], eix - proj1[0]]))
    b17 = min(np.linalg.norm([siy - b11[1], six - b11[0]]), np.linalg.norm([b12 - b11[1], eix - proj1[0]]))
    b18 = min(b16, b17)
    x1, b47, x2, b19 = ejx - sjx, b13 - sjy, eix - six, b12 - siy
    inner_product, b20 = x1 * x2 + b47 * b19, (x1 * x2 + b47 * b19) / (np.linalg.norm([x1, b47]) * np.linalg.norm([x2, b19]))
    b20 = max(min(b20, 1), -1)
    b21 = math.acos(b20)
    b22 = math.sin(b21) * fonk4(b8) if b21 < (math.pi / 2) else fonk4(b8)
    return w1 * b15 + w2 * b18 + w3 * b22 + b6 * b7
def fonk4(segment):
    sx, sy, ex, b23 = segment[0][0], segment[0][1], segment[1][0], segment[1][1]
    return np.linalg.norm([ex - sx, b23 - sy])
def fonk5(t, s, e):
    a1 = 2
    b24 = fonk4([t[s], t[e]])
    x1, b47, x2, b19 = t[s][0], t[s][1], t[e][0], t[e][1]
    Dx, b25 = x2 - x1, b19 - b47
    b26 = np.linalg.norm([Dx, b25])
    b27 = sum(math.fabs((b25 * t[i][0] - Dx * t[i][1] + x2 * b47 - b19 * x1) / b26) for i in range(s, e))
    b28 = b27 / a1
    return b24 + b28
def fonk6(t, s, e):
    return sum(fonk4([t[i], t[i + 1]]) for i in range(s, e))
def fonk7(t):
    cp, si, b29 = [t[0]], 1, 1
    while si + b29 <= len(t):
        b30 = si + b29
        cost_par, b31 = fonk5(t, si, b30), fonk6(t, si, b30)
        if cost_par > b31:
            cp.append(t[b30 - 1])
            si, b29 = b30 - 1, 1
        else:
            b29 += 1
    cp.append(t[-1])
    return cp
def fonk8(b52):
    return [[segment, p, 0] for p in b52 for i in range(len(b52[p]) - 1) for segment in [[b52[p][i], b52[p][i + 1]]]]
def fonk9(b52, b39, b26):
    b32 = []
    for Li in b39:
        for p in b52:
            if p != Li[1]:
                for segment in [[b52[p][i], b52[p][i + 1]] for i in range(len(b52[p]) - 1)]:
                    b33 = fonk3(Li[0], segment)
                    if not math.isnan(b33):
                        b32.append(b33)
    b34 = fonk1(b32)
    b35 = sum((len([b27 for b27 in [fonk3(Li[0], [b52[p][i], b52[p][i + 1]]) for i in range(len(b52[p]) - 1)] if b27 <= b34]) + 1) for Li in b39 for p in b52 if p != Li[1])
    return b35, b34
def fonk10(b52, b39, b26, a3):
    totaldensity, b34 = fonk9(b52, b39, b26)
    a2 = 0
    for Li in b39:
        b32, b36 = [], 0
        for p in b52:
            if p != Li[1]:
                b37 = sum(fonk4(segment) for segment in [[b52[p][i], b52[p][i + 1]] for i in range(len(b52[p]) - 1)] if fonk3(Li[0], segment) < b26)
                if b37 > fonk4(Li[0]):
                    b36 += 1
        b38 = (len([b27 for b27 in b32 if b27 <= b34]) + 1) * len(b39)
        if (b36 * totaldensity) / b38 < a3 * len(b52):
            Li[2] = 1
            a2 += 1
    return b39, a2
def fonk11(b52, b39, F):
    return [p for p in b52 if sum(fonk4(seg) for seg in [Li[0] for Li in b39 if (Li[2] == 1 and Li[1] == p)]) / sum(fonk4([b52[p][i], b52[p][i + 1]]) for i in range(len(b52[p]) - 1)) > F]
def fonk12(b52, b26, a3, F):
    print("Partition Phase Begins ...")
    b39 = fonk8(b52)
    print("Partition Done !")
    print("Total Number of t-partitions: ", len(b39))
    print("Outlying t-partition Detection Phase Begins ...")
    b39, a2 = fonk10(b52, b39, b26, a3)
    print("Outlying t-partition Detection Done !")
    print("Number of Outlying t-partitions: ", a2, " of ", len(b39))
    print("Outlying Trajectory Detection Phase Begins ...")
    b40 = fonk11(b52, b39, F)
    print("Outlying Trajectory Detection Phase Done !")
    print("Number of Outlying Trajectories: ", len(b40), " of ", len(b52))
    return b40
def fonk13(tr):
    return ((int(tr[0:2]) * 3600) + (int(tr[3:5]) * 60) + (int(tr[6:8]))) / 86400.0
def fonk14(b51, N):
    b41 = {}
    with open(b51, b42 = '') as csvfile:
        b43 = csv.reader(csvfile, delimiter=' ', quotechar='|')
        t1, m1, x1, b47, b44 = -1, '', -1, -1, -1
        a3 = 0
        for row in b43:
            b45 = ', '.join(row).split(";")
            t2, m2, x2, b19, b46 = fonk13((b45[0].split('b52')[1])[:-4]), b45[1], int(int(b45[2]) / 67), int(int(b45[3]) / 67), int(b45[4])
            if b44 = = b46 and t1 != t2:
                if b41[a3][-1][0] != x2 or b41[a3][-1][1] != b19:
                    b41[a3].append([x2, b19, t2])
            if b44 != b46:
                a3 += 1
                if not a3 <= N:
                    break
                b41[a3] = [[x2, b19, t2]]
            t1, m1, b44, x1, b47 = t2, m2, b46, x2, b19
    return b41
def fonk15(traj, p):
    x, b48 = [point[0] for point in traj], [point[1] for point in traj]
    fig, b49 = plt.subplots()
    b49.plot(x, b48)
    b49.set_title(f'TRAJECTORY ID: {p}')
    b49.set_xlabel('x')
    b49.set_ylabel('b48')
    plt.show()
    fig.savefig(f'Results/{p}.png')
if b50 = = "__main__":
    b51 = 'b43/csv/al_position2013-02-06.csv'
    b52 = fonk14(b51, 10)
    b53 = fonk12(b52, 37, 0.01, 0.4)
    print("Outliers: ", b53)
    for p in b52:
        fonk15(b52[p], p)
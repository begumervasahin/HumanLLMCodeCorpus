import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy
import csv
def fonk1(b31):
    b1 = np.array(b31)
    b2 = np.b2(b1)
    print(f"Mean Distance: {np.mean(b1)}")
    print(f"Minimum Distance: {np.min(b1)}")
    print(f"Maximum Distance: {np.max(b1)}")
    print(f"Standard Deviation of Distances: {b2}")
    return b2
def fonk2(point, line_2pt):
    x0, b3 = point
    x1, b19, x2, b4 = line_2pt[0], line_2pt[1], line_2pt[2], line_2pt[3]
    vx, b5 = x2 - x1, b4 - b19
    dx, b6 = x0 - x1, b3 - b19
    b7 = (dx * vx + b6 * b5) / (vx * vx + b5 * b5)
    return [x1 + b7 * vx, b19 + b7 * b5]
def fonk3(L1, b10):
    w1, w2, w3, b8 = 1.0, 1.0, 1.0, 1.0
    b9 = abs((fonk4(L1) / L1[0][2]) - (fonk4(b10) / b10[0][2]))
    if fonk4(L1) > fonk4(b10):
        L1, b10 = deepcopy(b10), deepcopy(L1)
    b11 = fonk2([b10[0][0], b10[0][1]], [L1[0][0], L1[0][1], L1[1][0], L1[1][1]])
    b12 = fonk2([L1[0][0], L1[0][1]], [b10[0][0], b10[0][1], b10[1][0], b10[1][1]])
    b13 = np.linalg.norm([b10[0][1] - b11[1], b10[0][0] - b11[0]])
    b14 = np.linalg.norm([L1[0][1] - b12[1], L1[0][0] - b12[0]])
    b15 = (math.pow(b13, 2) + math.pow(b14, 2)) / (b13 + b14)
    b16 = min(np.linalg.norm([L1[0][1] - b11[1], L1[0][0] - b11[0]]), np.linalg.norm([L1[1][1] - b11[1], L1[1][0] - b11[0]]))
    b17 = min(np.linalg.norm([L1[0][1] - b12[1], L1[0][0] - b12[0]]), np.linalg.norm([L1[1][1] - b12[1], L1[1][0] - b12[0]]))
    b18 = min(b16, b17)
    x1, b19 = b10[1][0] - b10[0][0], b10[1][1] - b10[0][1]
    x2, b4 = L1[1][0] - L1[0][0], L1[1][1] - L1[0][1]
    b20 = np.clip((x1 * x2 + b19 * b4) / (np.linalg.norm([x1, b19]) * np.linalg.norm([x2, b4])), -1, 1)
    b21 = math.acos(b20)
    b22 = math.sin(b21) * fonk4(b10) if b21 < (math.pi / 2) else fonk4(b10)
    return w1 * b15 + w2 * b18 + w3 * b22 + b8 * b9
def fonk4(segment):
    return np.linalg.norm([segment[1][0] - segment[0][0], segment[1][1] - segment[0][1]])
def fonk5(b7, s, e):
    a1 = 2
    b23 = fonk4([b7[s], b7[e]])
    Dx, b24 = b7[e][0] - b7[s][0], b7[e][1] - b7[s][1]
    b25 = np.linalg.norm([Dx, b24])
    b26 = sum(math.fabs((b24 * b7[i][0] - Dx * b7[i][1] + b7[e][0] * b7[s][1] - b7[e][1] * b7[s][0]) / b25) for i in range(s, e))
    b27 = b26 / a1
    return b23 + b27
def fonk6(b7, s, e):
    return sum(fonk4([b7[i], b7[i + 1]]) for i in range(s, e))
def fonk7(b7):
    b28 = [b7[0]]
    si, b29 = 1, 1
    while si + b29 <= len(b7):
        b30 = si + b29
        if fonk5(b7, si, b30) > fonk6(b7, si, b30):
            b28.append(b7[b30 - 1])
            si, b29 = b30 - 1, 1
        else:
            b29 += 1
    b28.append(b7[-1])
    return b28
def fonk8(b51):
    return [[segment, p, 0] for p in b51 for i in range(len(b51[p]) - 1) for segment in [[b51[p][i], b51[p][i + 1]]]]
def fonk9(b51, b37, b25):
    b31 = []
    for Li in b37:
        for p in b51:
            if p != Li[1]:
                for segment in [[b51[p][i], b51[p][i + 1]] for i in range(len(b51[p]) - 1)]:
                    b32 = fonk3(Li[0], segment)
                    if not math.isnan(b32):
                        b31.append(b32)
    b33 = fonk1(b31)
    b34 = sum(len([b26 for b26 in [fonk3(Li[0], [b51[p][i], b51[p][i + 1]]) for i in range(len(b51[p]) - 1)] if b26 <= b33]) + 1 for Li in b37 for p in b51 if p != Li[1])
    return b34, b33
def fonk10(b51, b37, b25, b42):
    totaldensity, b33 = fonk9(b51, b37, b25)
    a2 = 0
    for Li in b37:
        b35 = sum(1 for p in b51 if p != Li[1] and sum(fonk4(segment) for segment in [[b51[p][i], b51[p][i + 1]] for i in range(len(b51[p]) - 1)] if fonk3(Li[0], segment) < b25) > fonk4(Li[0]))
        b36 = (len([b26 for b26 in [fonk3(Li[0], [b51[p][i], b51[p][i + 1]]) for i in range(len(b51[p]) - 1)] if b26 <= b33]) + 1) * len(b37)
        if (b35 * totaldensity) / b36 < b42 * len(b51):
            Li[2] = 1
            a2 += 1
    return b37, a2
def fonk11(b51, b37, F):
    return [p for p in b51 if sum(fonk4(seg) for seg in [Li[0] for Li in b37 if Li[2] == 1 and Li[1] == p]) / sum(fonk4([b51[p][i], b51[p][i + 1]]) for i in range(len(b51[p]) - 1)) > F]
def fonk12(b51, b25, b42, F):
    print("Partition Phase Begins ...")
    b37 = fonk8(b51)
    print("Partition Done!")
    print("Total Number of b7-partitions: ", len(b37))
    print("Outlying b7-partition Detection Phase Begins ...")
    b37, a2 = fonk10(b51, b37, b25, b42)
    print("Outlying b7-partition Detection Done!")
    print("Number of Outlying b7-partitions: ", a2, " of ", len(b37))
    print("Outlying Trajectory Detection Phase Begins ...")
    b38 = fonk11(b51, b37, F)
    print("Outlying Trajectory Detection Phase Done!")
    print("Number of Outlying Trajectories: ", len(b38), " of ", len(b51))
    return b38
def fonk13(tr):
    return ((int(tr[:2]) * 3600) + (int(tr[3:5]) * 60) + int(tr[6:8])) / 86400.0
def fonk14(b50, N):
    b39 = {}
    with open(b50, b40 = '') as csvfile:
        b41 = csv.reader(csvfile, delimiter=' ', quotechar='|')
        t1, b46, b42 = -1, -1, 0
        for row in b41:
            b43 = ', '.join(row).split(";")
            b44 = fonk13(b43[0].split('b51')[1][:-4])
            x2, b4, b45 = int(int(b43[2]) / 67), int(int(b43[3]) / 67), int(b43[4])
            if b46 = = b45 and t1 != b44:
                if b39[b42][-1][0] != x2 or b39[b42][-1][1] != b4:
                    b39[b42].append([x2, b4, b44])
            if b46 != b45:
                b42 += 1
                if b42 > N:
                    break
                b39[b42] = [[x2, b4, b44]]
            t1, b46 = b44, b45
    return b39
def fonk15(traj, p):
    x, b47 = [point[0] for point in traj], [point[1] for point in traj]
    fig, b48 = plt.subplots()
    b48.plot(x, b47)
    b48.set_title(f'TRAJECTORY ID: {p}')
    b48.set_xlabel('x')
    b48.set_ylabel('b47')
    plt.show()
    fig.savefig(f'Results/{p}.png')
if b49 = = "__main__":
    b50 = 'b41/csv/al_position2013-02-06.csv'
    b51 = fonk14(b50, 10)
    b52 = fonk12(b51, 37, 0.01, 0.4)
    print("Outliers: ", b52)
    for p in b51:
        fonk15(b51[p], p)
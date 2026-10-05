import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
import csv
def fonk1(tr):
    return ((int(tr[0:2])*3600) + (int(tr[3:5])*60) + (int(tr[6:8])))/86400.0
def fonk2(b68, N):
    b1 = {}
    b2 = open(b68, newline='')
    b3 = csv.reader(b2, delimiter=' ', quotechar='|')
    xs, ys, b4 = [], [], []
    t1, m1, b48, b8, b5 = -1, '', -1, -1, -1
    a1 = 0
    for row in b3:
        b6 = ', '.join(row).split(";")
        t2, m2, b49, b50, b7 = fonk1((b6[0].split('b69')[1])[:-4]), b6[1], int(int(b6[2])/67), int(int(b6[3])/67), int(b6[4])
        if (b5 = = b7 and t1 != t2):
            if b1[a1][len(b1[a1])-1][0] != b49 or b1[a1][len(b1[a1])-1][1] != b50:
                b1[a1].append([b49,b50,t2])
        if b5 != b7:
            a1 = a1 + 1
            if not a1 <= N:
                break
            b1[a1] = [[b49,b50,t2]]
        t1, m1, b5, b48, b8 = t2, m2, b7, b49, b50
    return b1
def fonk3(traj, p):
    x, y, b9 = [], [], []
    a2 = 1
    for point in traj:
        x.append(point[0])
        y.append(point[1])
        a2 = a2 + 1
    b10 = plt.figure()
    plt.plot(x, y)
    b10.suptitle('TRAJECTORY ID: ' + str(p))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    b10.savefig('Results/' + str(p) + '.png')
def fonk4(b69, b58, a1, F):
    print("Partition Phase Begins ...")
    b11 = fonk5(b69)
    print("Partition Done !")
    print("Total Number of b9-partitions: ", len(b11))
    print("Outlying b9-partition Detection Phase Begins ...")
    b11, b12 = fonk6(b69, b11, b58, a1)
    print("Outlying b9-partition Detection Done !")
    print("Number of Outlying b9-partitions: ", b12, " of ", len(b11))
    print("Outlying Trajectory Detection Phase Begins ...")
    b13 = fonk7(b69, b11, F)
    print("Outlying Trajectory Detection Phase Done !")
    print("Number of Outlying Trajectories: ", len(b13), " of ", len(b69))
    return b13
def fonk5(b69):
    b11 = []
    for p in b69:
        for a2 in range(len(b69[p])-1):
            b14 = [b69[p][a2], b69[p][a2+1]]
            b11.append([b14,p,0])
    return b11
def fonk6(b69, b11, b58, a1):
    b12 = 0
    a3 = 0
    totaldensity , b15 = fonk8(b69,b11,b58)
    for Li in b11:
        b16 = []
        a4 = 0
        for p in b69:
            if p != Li[1]:
                a5 = 0
                for a2 in range(len(b69[p])-1):
                    b14 = [b69[p][a2], b69[p][a2+1]]
                    b17 = fonk11(Li[0], b14)
                    b16.append(b17)
                    if b17 < b58:
                        a5 = a5 + fonk12(b14)
                if a5 > fonk12(Li[0]):
                    a4 = a4 + 1
        b18 = (len([a8 for a8 in b16 if a8 <= b15]) + 1)*len(b11)
        if (a4*totaldensity)/b18 < a1*len(b69):
            Li[2] = 1
            b12 += 1
        a3 = a3 + 1
    return b11, b12
def fonk7(b69, b11, F):
    b13 = []
    for p in b69:
        b19 = [Li[0] for Li in b11 if (Li[2] == 1 and Li[1] == p)]
        b21, b20 = 0, 0
        for seg in b19:
            b21 = b21 + fonk12(seg)
        for a2 in range(len(b69[p])-1):
            b14 = [b69[p][a2], b69[p][a2+1]]
            b20 = b20 + fonk12(b14)
        if b21/b20 > F:
            b13.append(p)
    return b13
def fonk8(b69, b11, b58):
    b16 = []
    for Li in b11:
        a4 = 0
        for p in b69:
            if p != Li[1]:
                a5 = 0
                for a2 in range(len(b69[p])-1):
                    b14 = [b69[p][a2], b69[p][a2+1]]
                    b17 = fonk11(Li[0], b14)
                    if not math.isnan(b17):
                        b16.append(b17)
    b15 = fonk9(b16)
    a6 = 0
    for Li in b11:
        b16 = []
        for p in b69:
            if p != Li[1]:
                for a2 in range(len(b69[p])-1):
                    b14 = [b69[p][a2], b69[p][a2+1]]
                    b17 = fonk11(Li[0], b14)
                    b16.append(b17)
                a6 = a6+(len([a8 for a8 in b16 if a8 <= b15]) + 1)
    return a6 , b15
def fonk9(b16):
    b22 = np.b22(np.array(b16))
    print("Mean Distance: ", np.mean(np.array(b16)))
    print("Minimum Distance: ", np.min(np.array(b16)))
    print("Maximum Distance: ", np.max(np.array(b16)))
    print("Standard Deviation of Distances: ", b22)
    return b22
def fonk10(point, line_2pt):
    b23 = [1, 1, 1, 1]
    b23[0] = line_2pt[0]
    b23[1] = line_2pt[1];
    b23[2] = line_2pt[2]-line_2pt[0];
    b23[3] = line_2pt[3]-line_2pt[1];
    b24 = b23[2];
    b25 = b23[3];
    b26 = point[0] - b23[0];
    b27 = point[1] - b23[1];
    b28 = (b26 * b24 + b27 * b25) / (b24 * b24 + b25 * b25);
    point[0] = b23[0] + b28 * b24;
    point[1] = b23[1] + b28 * b25;
    return [point[0], point[1]]
def fonk11(b33, b32):
    w1, w2, w3, b29 = 1.0, 1.0, 1.0, 1.0
    b30 = abs((fonk12(b33)/b33[0][2])-(fonk12(b32)/b32[0][2]))
    if fonk12(b33) > fonk12(b32):
        b31 = deepcopy(b32)
        b32 = deepcopy(b33)
        b33 = deepcopy(b31)
    b34 = [b32[0][0], b32[0][1]]
    b35 = [b33[0][0], b33[0][1], b33[1][0], b33[1][1]]
    b36 = fonk10(b34, b35)
    b37 = [b33[0][0], b33[0][1]]
    b38 = [b32[0][0], b32[0][1], b32[1][0], b32[1][1]]
    b39 = fonk10(b37, b38)
    six, siy, eix, b40 = b33[0][0], b33[0][1], b33[1][0], b33[1][1]
    sjx, sjy, ejx, b41 = b32[0][0], b32[0][1], b32[1][0], b32[1][1]
    b42 = np.linalg.norm([sjy-b36[1], sjx-b36[0]])
    b43 = np.linalg.norm([siy-b39[1], six-b39[0]])
    b44 = (math.pow(b42, 2)+math.pow(b43, 2))/(b42+b43)
    b45 = min(np.linalg.norm([siy-b36[1], six-b36[0]]), np.linalg.norm([b40-b36[1], eix-b36[0]]))
    b46 = min(np.linalg.norm([siy-b39[1], six-b39[0]]), np.linalg.norm([b40-b39[1], eix-b36[0]]))
    b47 = min(b45, b46)
    b48 = ejx-sjx
    b8 = b41-sjy
    b49 = eix-six
    b50 = b40-siy
    b51 = b48*b49 + b8*b50
    b52 = b51/(np.linalg.norm([b48, b8])*np.linalg.norm([b49, b50]))
    if b52 < -1:
        b52 = -1
    elif b52 > 1:
        b52 = 1
    b53 = math.acos(b52)
    if b53 < (math.pi/2):
        b54 = math.sin(b53)*fonk12(b32)
    else:
        b54 = fonk12(b32)
    return w1*b44 + w2*b47 + w3*b54 + b29*b30
def fonk12(b14):
    sx, sy, ex, b55 = b14[0][0], b14[0][1], b14[1][0], b14[1][1]
    return np.linalg.norm([ex-sx, b55-sy])
def fonk13(b9, s, e):
    a7 = 2
    b56 = fonk12([b9[s], b9[e]])
    b48, b8, b49, b50 = b9[s][0], b9[s][1], b9[e][0], b9[e][1]
    Dx, b57 = b49-b48, b50-b8
    b58 = np.linalg.norm([Dx, b57])
    a8 = 0
    for a2 in range(s, e):
        x0, b59 = b9[a2][0], b9[a2][1]
        b60 = math.fabs((b57*x0 - Dx*b59 + b49*b8 - b50*b48)/b58)
        a8 = a8 + b60
    b61 = a8/a7
    b62 = b56+b61
    return b62
def fonk14(b9, s, e):
    b20 = 0
    for a2 in range(s,e):
        b20 = b20 + fonk12([b9[a2],b9[a2+1]])
    return b20
def fonk15(b9):
    b63 = [b9[0]]
    si, b64 = 1, 1
    while si + b64 <= len(b9):
        b65 = si + b64
        b66 = fonk13(b9,si,b65)
        b67 = fonk14(b9, si,b65)
        if b66 > b67:
            b63.append(b9[b65-1])
            si, b64 = b65-1, 1
        else:
            b64 = b64 + 1
    b63.append(b9[-1])
b68 = 'b3/csv/al_position2013-02-06.csv'
b69 = fonk2(b68, 10)
b70 = fonk4(b69, 37, 0.01, 0.4)
print("Outliers: ", b70)
for p in b69:
    fonk3(b69[p], p)
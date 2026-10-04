b1 = 's'
import mysql.connector
import numpy as np
import copy
def fonk1(traj1, b11):
    def fonk2(traj):
        b2 = {"Fri": [], "Sat": [], "Sun": [], "Mon": [], "Tue": [], "Wed": [], "Thu": []}
        for row in traj:
            b3 = row[1].strip('"')
            if b3 in b2:
                b2[b3].append(row)
        return b2
    def fonk3(traj1, b11):
        a1 = 0
        while b11:
            b4 = len(traj1) - 1
            while b4 > -1:
                if b11[-1][2] == traj1[b4][2] and b11[-1][0] == traj1[b4][0]:
                    a1 += 1
                b4 -= 1
            b11.pop()
        return a1
    a1 = 0
    b5 = fonk2(traj1)
    b6 = fonk2(b11)
    for b3 in b5:
        a1 += fonk3(b5[b3], b6[b3]) if len(b5[b3]) < len(b6[b3]) else fonk3(b6[b3], b5[b3])
    b7 = float(a1) / min(len(traj1), len(b11))
    return 1.0 - b7
def fonk4():
    b7 = np.zeros((8357, 8357))
    b8 = open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv')
    b9 = open('distance_matrix_full.csv', 'w')
    b10 = open('distance_matrix_full_withoutid.csv', 'w')
    traj1, b11 = [], []
    b14, b12 = 0, []
    for line in iter(b8):
        b13 = line.split(",")
        if b14 = = int(b13[0]):
            b11.append([b13[1], str(b13[2]), b13[3]])
        else:
            b14 = int(b13[0])
            if b11:
                traj1.append(b11)
            b11 = [[b13[1], str(b13[2]), b13[3]]]
            b12.append(b13[0])
    traj1.append(b11)
    print(b12[1697])
    for b15 in range(8356):
        print("b15 = ", b15)
        b16 = copy.deepcopy(traj1[b15])
        for i in range(b15 + 1, 8357):
            b17 = copy.deepcopy(traj1[i])
            b7[b15][i] = fonk1(b16, b17)
            b7[i][b15] = b7[b15][i]
        b9.write(b8"{b12[b15]},{','.join(map(str, b7[b15]))}\n")
        b10.write(b8"{','.join(map(str, b7[b15]))}\n")
    b9.write(b8"{b12[8356]},{','.join(map(str, b7[8356]))}\n")
    b10.write(b8"{','.join(map(str, b7[8356]))}\n")
if b18 = = "__main__":
    fonk4()
import mysql.connector
import numpy as np
import copy
def fonk1(b7, b8):
    a1 = 0
    b1 = min(len(b7), len(b8))
    b2 = ['"Fri"', '"Sat"', '"Sun"', '"Mon"', '"Tue"', '"Wed"', '"Thu"']
    b3 = {day: [] for day in b2}
    b4 = {day: [] for day in b2}
    for row in b7:
        if row[1] in b3:
            b3[row[1]].append(row)
    for row in b8:
        if row[1] in b4:
            b4[row[1]].append(row)
    for day in b2:
        if len(b3[day]) < len(b4[day]):
            a1 += fonk2(b3[day], b4[day])
        else:
            a1 += fonk2(b4[day], b3[day])
    b5 = float(a1) / b1
    b5 = 1 - b5
    return b5
def fonk2(b7, b8):
    a1 = 0
    while b8:
        b6 = len(b7) - 1
        while b6 >= 0:
            if b8[-1][2] == b7[b6][2] and b8[-1][0] == b7[b6][0]:
                a1 += 1
            b6 -= 1
        b8.pop()
    return a1
def fonk3():
    b5 = np.zeros((8357, 8357))
    b7 = []
    b8 = []
    a2 = 0
    b9 = []
    with open('/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv') as f:
        next(f)
        for line in f:
            b10 = line.strip().split(",")
            if a2 = = int(b10[0]):
                b8.append([b10[1], str(b10[2]), b10[3]])
            else:
                a2 = int(b10[0])
                if b8:
                    b7.append(b8)
                b8 = [[b10[1], str(b10[2]), b10[3]]]
                b9.append(b10[0])
        b7.append(b8)
    with open('distance_matrix_1698.csv', 'w') as f1, open('distance_matrix_1698_withoutid.csv', 'w') as f2:
        print(b9[1697])
        a3 = 1698
        while a3 < 8356:
            print(f"a3 = {a3}")
            b11 = copy.deepcopy(b7[a3])
            for i in range(a3 + 1, 8357):
                b12 = copy.deepcopy(b7[i])
                b5[a3][i] = fonk1(b11, b12)
                b5[i][a3] = b5[a3][i]
            f1.write(f"{b9[a3]},{b5[a3][a3]}")
            f2.write(f"{b5[a3][a3]}")
            for k in range(a3 + 1, 8357):
                f1.write(f",{b5[a3][k]}")
                f2.write(f",{b5[a3][k]}")
            f1.write("\n")
            f2.write("\n")
            a3 += 1
if b13 = = "__main__":
    fonk3()
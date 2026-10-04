import numpy as np
import copy
def fonk1(b10, b15):
    a1 = 0
    b1 = min(len(b10), len(b15))
    b2 = ["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]
    b3 = {day: [] for day in b2}
    b4 = {day: [] for day in b2}
    for row in b10:
        b3[row[1]].append(row)
    for row in b15:
        b4[row[1]].append(row)
    for day in b2:
        if len(b3[day]) < len(b4[day]):
            a1 += fonk2(b3[day], b4[day])
        else:
            a1 += fonk2(b4[day], b3[day])
    b5 = 1 - (float(a1) / b1)
    return b5
def fonk2(b10, b15):
    a1 = 0
    for point in b10:
        if any(traj2_point[2] == point[2] and traj2_point[0] == point[0] for traj2_point in b15):
            a1 += 1
    return a1
def fonk3():
    a2 = 8357
    b6 = np.zeros((a2, a2))
    b7 = 'v01_anonymized_mobility.csv'
    b8 = 'distance_matrix_1698.csv'
    b9 = 'distance_matrix_1698_withoutid.csv'
    b10 = []
    b11 = []
    with open(b7, 'r') as f:
        next(f)
        for line in f:
            b12 = line.strip().split(",")
            b13 = int(b12[0])
            b14 = [b12[1], b12[2], b12[3]]
            if b11 and b13 = = int(b11[-1]):
                b15.append(b14)
            else:
                if b15:
                    b10.append(b15)
                b15 = [b14]
                b11.append(b12[0])
        if b15:
            b10.append(b15)
    print(b11[1697])
    with open(b8, 'w') as f1, open(b9, 'w') as f2:
        for j in range(1698, a2 - 1):
            print(f"Processing user {j}...")
            b16 = copy.deepcopy(b10[j])
            for i in range(j + 1, a2):
                b17 = copy.deepcopy(b10[i])
                b6[j][i] = fonk1(b16, b17)
                b6[i][j] = b6[j][i]
            f1.write(f"{b11[j]},{','.join(map(str, b6[j][j:]))}\n")
            f2.write(f"{','.join(map(str, b6[j][j:]))}\n")
if b18 = = "__main__":
    fonk3()
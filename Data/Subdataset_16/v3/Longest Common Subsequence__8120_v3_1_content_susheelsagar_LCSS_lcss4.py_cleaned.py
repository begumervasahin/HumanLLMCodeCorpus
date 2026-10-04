import numpy as np
import copy
def fonk1(b6, b8):
    a1 = 0
    b1 = min(len(b6), len(b8))
    b2 = ["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]
    b3 = {day: [] for day in b2}
    b4 = {day: [] for day in b2}
    for row in b6:
        b3[row[1]].append(row)
    for row in b8:
        b4[row[1]].append(row)
    for day in b2:
        if len(b3[day]) < len(b4[day]):
            a1 += fonk2(b3[day], b4[day])
        else:
            a1 += fonk2(b4[day], b3[day])
    b5 = 1 - (float(a1) / b1)
    return b5
def fonk2(b6, b8):
    a1 = 0
    for point in b6:
        if any(traj2_point[2] == point[2] and traj2_point[0] == point[0] for traj2_point in b8):
            a1 += 1
    return a1
def fonk3(b14):
    b6 = []
    b7 = []
    b8 = []
    with open(b14, 'r') as f:
        next(f)
        for line in f:
            b9 = line.strip().split(",")
            b10 = int(b9[0])
            b11 = [b9[1], b9[2], b9[3]]
            if b7 and b10 = = int(b7[-1]):
                b8.append(b11)
            else:
                if b8:
                    b6.append(b8)
                b8 = [b11]
                b7.append(b9[0])
        if b8:
            b6.append(b8)
    return b6, b7
def fonk4(b14, b7, b13, b12 = 1698):
    with open(b14, 'w') as f:
        for j in range(b12, len(b7) - 1):
            f.write(f"{b7[j]},{','.join(map(str, b13[j][j:]))}\n")
def fonk5():
    a2 = 8357
    b12 = 1698
    b13 = np.zeros((a2, a2))
    b14 = 'v01_anonymized_mobility.csv'
    b15 = 'distance_matrix_1698.csv'
    b16 = 'distance_matrix_1698_withoutid.csv'
    b6, b7 = fonk3(b14)
    print(b7[1697])
    for j in range(b12, a2 - 1):
        print(f"Processing user {j}...")
        b17 = copy.deepcopy(b6[j])
        for i in range(j + 1, a2):
            b18 = copy.deepcopy(b6[i])
            b13[j][i] = fonk1(b17, b18)
            b13[i][j] = b13[j][i]
    fonk4(b15, b7, b13, b12)
    fonk4(b16, b7, b13, b12)
if b19 = = "__main__":
    fonk5()
import numpy as np
import copy
def fonk1(b8, b9):
    def fonk2(b8, b9):
        a1 = 0
        while len(b9) > 0:
            b1 = len(b8) - 1
            while b1 > -1:
                if b9[-1][2] == b8[b1][2]:
                    if b9[-1][0] == b8[b1][0]:
                        a1 += 1
                b1 -= 1
            b9.pop()
        return a1
    b2 = ["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]
    b3 = {day: [] for day in b2}
    b4 = {day: [] for day in b2}
    for row in b8:
        b3[row[1].strip('"')].append(row)
    for row in b9:
        b4[row[1].strip('"')].append(row)
    a1 = 0
    b5 = min(len(b8), len(b9))
    for day in b2:
        if len(b3[day]) < len(b4[day]):
            a1 += fonk2(b3[day], b4[day])
        else:
            a1 += fonk2(b4[day], b3[day])
    b6 = float(a1) / b5
    return 1.0 - b6
def fonk3(file_path):
    with open(file_path, 'r') as f:
        next(f)
        b7 = f.readlines()
    return b7
def fonk4(b7):
    b8 = []
    b9 = []
    a2 = 0
    b10 = []
    for line in b7:
        b11 = line.split(",")
        if a2 = = int(b11[0]):
            b9.append([b11[1], b11[2], b11[3].strip()])
        else:
            a2 = int(b11[0])
            if b9:
                b8.append(b9)
            b9 = [[b11[1], b11[2], b11[3].strip()]]
            b10.append(b11[0])
    b8.append(b9)
    return b8, b10
def fonk5(b16, b10, b13, b14):
    with open(b13, 'w') as f1, open(b14, 'w') as f2:
        for j in range(len(b16)):
            f1.write(f"{b10[j]},{','.join(map(str, b16[j]))}\n")
            f2.write(f"{','.join(map(str, b16[j]))}\n")
def fonk6():
    b12 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
    b13 = 'distance_matrix_full.csv'
    b14 = 'distance_matrix_full_withoutid.csv'
    b7 = fonk3(b12)
    b8, b10 = fonk4(b7)
    b15 = len(b8)
    b16 = np.zeros((b15, b15))
    for j in range(b15 - 1):
        print(f"Processing user {j}")
        b17 = copy.deepcopy(b8[j])
        for i in range(j + 1, b15):
            b18 = copy.deepcopy(b8[i])
            b16[j][i] = fonk1(b17, b18)
            b16[i][j] = b16[j][i]
    fonk5(b16, b10, b13, b14)
if b19 = = "__main__":
    fonk6()
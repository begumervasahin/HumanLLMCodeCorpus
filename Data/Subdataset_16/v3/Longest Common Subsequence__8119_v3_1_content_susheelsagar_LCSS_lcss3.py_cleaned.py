import numpy as np
import copy
def fonk1(b8, b9):
    def fonk2(b8, b9):
        a1 = 0
        while b9:
            b1 = len(b8) - 1
            while b1 > -1:
                if b9[-1][2] == b8[b1][2] and b9[-1][0] == b8[b1][0]:
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
    b10 = []
    b11 = None
    for line in b7:
        b12 = line.split(",")
        b13 = int(b12[0])
        if b11 = = b13:
            b9.append([b12[1], b12[2], b12[3].strip()])
        else:
            b11 = b13
            if b9:
                b8.append(b9)
            b9 = [[b12[1], b12[2], b12[3].strip()]]
            b10.append(b12[0])
    if b9:
        b8.append(b9)
    return b8, b10
def fonk5(b18, b10, b15, b16):
    with open(b15, 'w') as f1, open(b16, 'w') as f2:
        for j in range(len(b18)):
            f1.write(f"{b10[j]},{','.join(map(str, b18[j]))}\n")
            f2.write(f"{','.join(map(str, b18[j]))}\n")
def fonk6():
    b14 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
    b15 = 'distance_matrix_full.csv'
    b16 = 'distance_matrix_full_withoutid.csv'
    b7 = fonk3(b14)
    b8, b10 = fonk4(b7)
    b17 = len(b8)
    b18 = np.zeros((b17, b17))
    for j in range(b17 - 1):
        print(f"Processing user {j}")
        b19 = copy.deepcopy(b8[j])
        for i in range(j + 1, b17):
            b20 = copy.deepcopy(b8[i])
            b18[j][i] = fonk1(b19, b20)
            b18[i][j] = b18[j][i]
    fonk5(b18, b10, b15, b16)
if b21 = = "__main__":
    fonk6()
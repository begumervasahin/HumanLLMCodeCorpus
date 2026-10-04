import numpy as np
def fonk1(filepath):
    with open(filepath, 'r') as f:
        b1 = []
        b2 = []
        b3 = None
        b4 = []
        for b5, line in enumerate(f):
            if b5 = = 0:
                continue
            b6 = line.strip().split(",")
            b7 = int(b6[0])
            if b3 = = b7:
                b2.append([b6[1], b6[2], b6[3]])
            else:
                if b2:
                    b1.append(b2)
                b2 = [[b6[1], b6[2], b6[3]]]
                b4.append(b6[0])
                b3 = b7
        b1.append(b2)
    print("Loading done")
    return b1, b4
def fonk2(filepath, b4):
    with open(filepath, 'r') as f:
        b8 = len(b4)
        b9 = np.zeros((b8, b8))
        for i, line in enumerate(f):
            b10 = line.strip().split(",")
            if b4[i] != b10[0]:
                print('Error: Mismatch in user IDs at index', i)
            for j, val in enumerate(b10[1:], b11 = 0):
                b9[i][j] = float(val)
                if float(val) == 0.0 and i != j:
                    print("Error at", i, j)
    return b9
def fonk3(b9):
    b8 = b9.shape[0]
    for i in range(b8):
        for j in range(b8):
            if b9[i][j] != b9[j][i]:
                print("Error at", i, j)
def fonk4():
    b12 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
    b13 = 'distance_matrix_final.csv'
    b1, b4 = fonk1(b12)
    b9 = fonk2(b13, b4)
    fonk3(b9)
if b14 = = "__main__":
    fonk4()
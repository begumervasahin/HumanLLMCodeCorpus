import numpy as np
def fonk1(filepath):
    b1 = []
    b2 = []
    b3 = []
    b4 = None
    with open(filepath, 'r') as file:
        for b5, line in enumerate(file):
            if b5 = = 0:
                continue
            b6 = line.strip().split(",")
            b7 = int(b6[0])
            if b7 = = b4:
                b2.append([b6[1], b6[2], b6[3]])
            else:
                if b2:
                    b1.append(b2)
                b2 = [[b6[1], b6[2], b6[3]]]
                b3.append(b6[0])
                b4 = b7
        if b2:
            b1.append(b2)
    print("Loading done")
    return b1, b3
def fonk2(filepath, b3):
    b8 = len(b3)
    b9 = np.zeros((b8, b8))
    with open(filepath, 'r') as file:
        for i, line in enumerate(file):
            b6 = line.strip().split(",")
            if b3[i] != b6[0]:
                print(f'Error: Mismatch in user IDs at index {i}')
            for j, value in enumerate(b6[1:]):
                b9[i][j] = float(value)
                if float(value) == 0.0 and i != j:
                    print(f"Error at {i}, {j}")
    return b9
def fonk3(b9):
    b8 = b9.shape[0]
    for i in range(b8):
        for j in range(b8):
            if b9[i][j] != b9[j][i]:
                print(f"Error at {i}, {j}")
def fonk4():
    b10 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
    b11 = 'distance_matrix_final.csv'
    b1, b3 = fonk1(b10)
    b9 = fonk2(b11, b3)
    fonk3(b9)
if b12 = = "__main__":
    fonk4()
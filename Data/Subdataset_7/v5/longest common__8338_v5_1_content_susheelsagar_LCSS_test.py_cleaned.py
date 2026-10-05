import numpy as np
def fonk1(file_path):
    b1 = []
    b2 = []
    b3 = []
    with open(file_path) as f:
        next(f)
        for line in f:
            b4 = line.strip().split(",")
            b5 = int(b4[0])
            if b5 = = b2[-1][0] if b2 else None:
                b2.append([b5, str(b4[1]), b4[2]])
            else:
                if b2:
                    b1.append(b2)
                b2 = [[b5, str(b4[1]), b4[2]]]
                b3.append(b5)
        b1.append(b2)
    print("Mobility b4 loaded successfully.")
    return b1, b3
def fonk2(file_path, b3):
    b6 = np.zeros((len(b3), len(b3)))
    with open(file_path) as f:
        for idx, line in enumerate(f):
            b4 = line.strip().split(",")
            if b3[idx] != int(b4[0]):
                print('Error: Mismatch in user IDs at index', idx)
            for j, b7 in enumerate(b4[1:]):
                b7 = float(b7)
                if b7 = = 0 and idx != j:
                    print("Error: Zero distance found at index", idx, j)
                b6[idx][j] = b7
    print("Distance matrix loaded successfully.")
    return b6
def fonk3(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] != matrix[j][i]:
                print("Error: Asymmetric distance found at indices", i, j)
def fonk4():
    b8 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
    b9 = 'distance_matrix_final.csv'
    b1, b3 = fonk1(b8)
    b6 = fonk2(b9, b3)
    fonk3(b6)
if b10 = = "__main__":
    fonk4()
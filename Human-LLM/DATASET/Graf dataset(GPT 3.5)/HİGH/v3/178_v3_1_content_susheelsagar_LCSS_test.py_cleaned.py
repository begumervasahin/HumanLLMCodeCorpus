import numpy as np
def fonk1(file_path):
    b1 = []
    with open(file_path) as mobility_file:
        next(mobility_file)
        b2 = None
        b3 = []
        for line in mobility_file:
            b5, timestamp, latitude, b4 = line.strip().split(",")
            if b5 = = b2:
                b3.append((timestamp, latitude, b4))
            else:
                if b3:
                    b1.append(b3)
                b2 = b5
                b3 = [(timestamp, latitude, b4)]
        if b3:
            b1.append(b3)
    print("Mobility b8 loaded successfully.")
    return b1
def fonk2(file_path):
    b6 = np.zeros((8357, 8357))
    b7 = []
    with open(file_path) as distance_file:
        for line in distance_file:
            b8 = line.strip().split(",")
            b5 = b8[0]
            if b7 and b7[-1] != b5:
                print('Error: Mismatch in user IDs at index', len(b7) - 1)
            b7.append(b5)
            b9 = [float(x) for x in b8[1:]]
            for j, b10 in enumerate(b9):
                if b10 = = 0:
                    if i != j:
                        print("Error: Zero distance found at index", i, j)
                b6[len(b7) - 1][j] = b10
    print("Distance matrix loaded successfully.")
    return b6
b11 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
b1 = fonk1(b11)
b12 = 'distance_matrix_final.csv'
b6 = fonk2(b12)
for i in range(8357):
    for j in range(8357):
        if b6[i][j] != b6[j][i]:
            print("Error: Asymmetric distance found at indices", i, j)
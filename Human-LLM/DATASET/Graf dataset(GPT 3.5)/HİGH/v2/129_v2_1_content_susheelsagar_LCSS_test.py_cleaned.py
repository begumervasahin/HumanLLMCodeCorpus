import numpy as np
b1 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
b2 = []
with open(b1) as mobility_file:
    b3 = False
    b4 = None
    b5 = []
    for line in mobility_file:
        if not b3:
            b3 = True
            continue
        b7, timestamp, latitude, b6 = line.strip().split(",")
        if b7 = = b4:
            b5.append((timestamp, latitude, b6))
        else:
            if b5:
                b2.append(b5)
            b4 = b7
            b5 = [(timestamp, latitude, b6)]
    if b5:
        b2.append(b5)
print("Mobility b11 loaded successfully.")
b8 = 'distance_matrix_final.csv'
b9 = np.zeros((8357, 8357))
with open(b8) as distance_file:
    b10 = []
    for line in distance_file:
        b11 = line.strip().split(",")
        b7 = b11[0]
        if b10 and b10[-1] != b7:
            print('Error: Mismatch in user IDs at index', len(b10) - 1)
        b10.append(b7)
        b12 = [float(x) for x in b11[1:]]
        for j, b13 in enumerate(b12):
            if b13 = = 0:
                if i != j:
                    print("Error: Zero distance found at index", i, j)
            b9[len(b10) - 1][j] = b13
print("Distance matrix loaded successfully.")
for i in range(8357):
    for j in range(8357):
        if b9[i][j] != b9[j][i]:
            print("Error: Asymmetric distance found at indices", i, j)
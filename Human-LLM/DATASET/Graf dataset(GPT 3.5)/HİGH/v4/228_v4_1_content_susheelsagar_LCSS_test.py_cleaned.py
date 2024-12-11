import numpy as np
b1 = '/home/s/Dropbox/Thesis/Telenor/fwdtelenordata/v01_anonymized_mobility.csv'
with open(b1) as f:
    b2 = []
    b3 = []
    a1 = 0
    b4 = []
    for b5, line in enumerate(f):
        if b5 = = 0:
            continue
        else:
            b6 = line.split(",")
            if a1 = = int(b6[0]):
                b3.append([b6[1], str(b6[2]), b6[3]])
            else:
                a1 = int(b6[0])
                if b3:
                    b2.append(b3)
                b3 = [[b6[1], str(b6[2]), b6[3]]]
                b4.append(b6[0])
    b2.append(b3)
print("Mobility b6 loading done.")
b7 = 'distance_matrix_final.csv'
b8 = np.zeros((8357, 8357))
with open(b7) as f1:
    for b5, line in enumerate(f1):
        b6 = line.split(",")
        if b4[b5] != b6[0]:
            print('Error: Mismatch in user IDs at index', b5)
        for j, dist in enumerate(b6[1:]):
            if float(dist) == 0 and b5 != j:
                print("Error: Zero b8 found at index", b5, j)
            b8[b5][j] = float(dist)
print("Distance matrix loading done.")
for i in range(8357):
    for j in range(8357):
        if b8[i][j] != b8[j][i]:
            print("Error: Asymmetric b8 found at indices", i, j)